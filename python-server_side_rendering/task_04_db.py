from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON oxuyan funksiya
def load_json():
    with open('products.json', 'r') as file:
        return json.load(file)

# CSV oxuyan funksiya
def load_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# SQL oxuyan funksiya
def load_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        return products

    except Exception as e:
        return None


@app.route('/products')
def display_products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    # mənbə düzgün deyil
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # mənbəyə görə data oxu
    if source == "json":
        data = load_json()
    elif source == "csv":
        data = load_csv()
    else:  # sql
        data = load_sql()
        if data is None:
            return render_template("product_display.html", error="Database error", products=None)

    # id varsa → filtr
    if product_id:
        try:
            pid = int(product_id)
            filtered = [p for p in data if p["id"] == pid]

            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)

            objects = [type("obj", (object,), p) for p in filtered]
            return render_template("product_display.html", products=objects)

        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=None)

    # bütün məhsullar
    objects = [type("obj", (object,), p) for p in data]
    return render_template("product_display.html", products=objects)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

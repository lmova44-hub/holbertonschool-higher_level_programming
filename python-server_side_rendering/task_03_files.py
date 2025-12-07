from flask import Flask, request, render_template
import json
import csv

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


@app.route('/products')
def display_products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    # 1️⃣ Yanlış source varsa → error
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # 2️⃣ Düzgün source-a görə data yüklə
    data = load_json() if source == "json" else load_csv()

    # 3️⃣ Əgər id verilibsə, filtr et
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)

            # JSON .key() işlətmir, Jinja üçün obyektə çevirmək yaxşıdır
            filtered_objects = [
                type('obj', (object,), p) for p in filtered
            ]

            return render_template("product_display.html", products=filtered_objects)

        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=None)

    # 4️⃣ ID verilməyibsə → bütün məhsullar
    all_objects = [type('obj', (object,), p) for p in data]
    return render_template("product_display.html", products=all_objects)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

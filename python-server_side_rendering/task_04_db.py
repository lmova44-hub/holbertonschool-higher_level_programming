from flask import Flask, render_template, request, abort
import sqlite3

app = Flask(__name__)

# ... JSON, CSV, SQL funksiyaları burada ...

@app.route('/products')
def show_products():
    source = request.args.get('source', 'json')

    if source == 'json':
        products = products_json
    elif source == 'csv':
        products = products_csv
    elif source == 'sql':
        products = get_products_from_db()
        if products is None:
            return "<h1>Database error</h1>", 500
    else:
        # Burada status kodunu da qaytarırıq
        return "<h1>Wrong source</h1>", 400

    return render_template('product_display.html', products=products)

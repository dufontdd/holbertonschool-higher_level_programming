#!/usr/bin/python3
"""
Flask app to display products from JSON or CSV
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv():
    """Read products from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []

    return products


@app.route('/products')
def products():
    """
    Display products from JSON or CSV
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    # Choose source
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

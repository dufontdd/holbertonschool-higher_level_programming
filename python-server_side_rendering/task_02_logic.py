#!/usr/bin/python3
"""
Flask app with dynamic items from JSON
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """Home route"""
    return render_template('index.html')


@app.route('/items')
def items():
    """
    Display items from items.json
    """
    items_list = []

    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

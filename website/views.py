from flask import Blueprint, render_template, request
from .load_data import load_data
from .sort import sort_items
import pandas as pd

views = Blueprint('view', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        search_key = request.form.get('search_key')
        items = load_data(search_key)
        print(items)
        items.to_csv('prdataframe.csv', index=False)
        items = sort_items(items) 
        print(items)
        items.to_csv('mydata.csv', index=False)
        return render_template('items.html', items=items, title=search_key)
    else:
        return render_template('base.html')
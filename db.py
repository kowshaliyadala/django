import json
from pymongo import MongoClient

userData = [
    {
        'name': 'aowshali',
        'email': 'kowshali@gmail.com',
        'password': 'Kowshali'

    },
    {
        'name': 'ananya',
        'email': 'ananya@gmail.com',
        'password': 'ananyaa'
    },
    {
        'name': 'pinky',
        'email': 'pinky123@gmail.com',
        'password': 'pinky',
    }
]
with open('db.json', 'w') as f:
    json.dump(userData, f, indent=4)

product = [
    {
        'id': '1',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'Levis Shirt',
        'op': '1490',
        'price': '999',
        'brand': 'Levis',
        'Material': 'Cotton',
        'Pattern': 'Checkered Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/1.jpg',
        'desc': 'this is the best tshirt'
    },
    {
        'id': '2',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'Allen Solly shirt',
        'op': '2300',
        'price': '1999',
        'brand': 'Allen Solly',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/2.jpg'
    },
    {
        'id': '3',
        'detailPageUrl': 't-shirts',
        'type': 'tshirt',
        'name': 'Forever21 shirt',
        'op': '2300',
        'price': '1999',
        'brand': 'Forever21',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/3.jpg'
    },
    {
        'id': '4',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'Allen Solly shirt',
        'op': '2300',
        'price': '1999',
        'brand': 'Allen Solly',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/4.jpg'
    },
    {
        'id': '5',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'Levis shirt',
        'op': '2300',
        'price': '1999',
        'brand': 'Levis',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/5.jpg'
    },
{
        'id': '6',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'US Polo shirt',
        'op': '2999',
        'price': '2699',
        'brand': 'US Polo',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/6.jpg'
    },
{
        'id': '7',
        'detailPageUrl': 't-shirts',
        'type': 't-shirt',
        'name': 'US Polo t-shirt',
        'op': '2999',
        'price': '2699',
        'brand': 'US Polo',
        'Material': 'Cotton',
        'Pattern': 'Short Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/7.jpg'
    },
{
        'id': '8',
        'detailPageUrl': 'shirts',
        'type': 'shirt',
        'name': 'Diverse Shirt',
        'op': '2000',
        'price': '1300',
        'brand': 'Diverse',
        'Material': 'Cotton',
        'Pattern': 'Long Sleeve',
        'image': 'http://127.0.0.1:8000/static/images/8.jpg'
    },
]
with open('productDB.json', 'w') as f:
    json.dump(product, f, indent=4)

import pymongo
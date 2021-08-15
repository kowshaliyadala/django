import json
from bson import json_util
from django.conf import settings
from django.http import JsonResponse

from helloworld.settings import PRODUCT_COLLECTION
from products.utils import requireLogin
from auth import utils


def product(request):

    if request.method == 'GET':

       products = [i for i in PRODUCT_COLLECTION.find({})]
       prod = json.loads(json_util.dumps(products))
       print(prod)
       return JsonResponse({'products': prod})
    if request.method == 'POST':
        data = json.loads(request.body)
        status = PRODUCT_COLLECTION.insert_many(data)
        print(status)
        return JsonResponse({'status': True})

@utils.requireLogin
def cartdetails(request):
    if request.method == "POST":
        data = json.loads(request.body)
        status = settings.CART_COLLECTION.insert_one(data)
        print(status)
        return JsonResponse({"data": "Added to cart successfully!"})
    if request.method == "GET":
        '''str = request.GET.get("$oid")
        pdt = settings.CART_COLLECTION.find_one({"_id": ObjectId(str)})
        items = json.loads(str(pdt))'''
        cartitems = [i for i in settings.CART_COLLECTION.find({})]
        items = json.loads(json_util.dumps(cartitems))
        print(items)

        return JsonResponse({"items": items})
    if request.method == "DELETE":
        deleted = settings.CART_COLLECTION.delete_many({})
        print(deleted)
        return JsonResponse({"deleted": str(deleted)})

def men(request):
    if request.method == "POST":
        res = PRODUCT_COLLECTION.find_one({'idealfor': 'men' })
        items = json.loads(json_util.dumps(res))
        print(items)
        return JsonResponse({'idealfor': items})
    if request.method == "GET":
        res = PRODUCT_COLLECTION.find({'_id': 0,'idealfor': 1})
        items = json.loads(json_util.dumps(res))
        print(items)
        return JsonResponse({'idealfor': items})
import jwt
from bson import json_util
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

from helloworld.settings import USER_COLLECTION


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = settings.USER_COLLECTION.insert_one(data)
        print(status)
        return JsonResponse({'status': True})
def fetchUsers(request):
    if request.method == 'GET':
        users = [i for i in settings.USER_COLLECTION.find({})]
        user = json.loads(json_util.dumps(users))
        return JsonResponse({'users': user})
def login(request, **kwargs):
    if request.method == "POST":
        req_user = json.loads(request.body)
        for userObj in USER_COLLECTION.find({'email': req_user['email'],'password': req_user['password']}):
            """if userObj['email'] != req_user['email'] or userObj['password'] != req_user['password'] :
                '''for x in settings.USER_COLLECTION.find({}, {"_id": 0, "email": 1, "password": 1}):
            print(x)
            print(x['email'])
        if req_user['email'] != x['email'] or req_user['password'] != x['password']:'''
                return HttpResponse('Unauthorized', status = 401)
            if userObj['email'] == req_user['email'] or userObj['password'] != req_user['password']
        #create a token"""
            if userObj['email'] == req_user['email'] and userObj['password'] == req_user['password']:
                token = jwt.encode(
                    {'email': req_user['email']
                     },
                    settings.SECRET_KEY,
                    algorithm="HS256")
                return JsonResponse({'token': token})
            return HttpResponse('Unauthorized', status =401 )
    return ({'status': True})
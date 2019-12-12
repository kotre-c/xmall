from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.generic.base import View

from account.models import User
from account.serializers import DateEncoder


class UserListView(View):
    # def get(self, response, username):
    #     user = User.objects.get(username=username)
    #     u = user.to_json()
    #     u['image'] = str(u['image'])
    #     return HttpResponse(json.dumps(u, cls=DateEncoder), content_type='application/json')
    pass
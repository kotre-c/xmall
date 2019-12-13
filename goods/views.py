import decimal
import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.generic.base import View
from rest_framework import generics, request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Good, GoodImage

# Create your views here.
from goods.serializers import DateEncoder, GoodListSerializer, GoodImageListSerializer, GoodDetailSerializer


# class GoodListView(View):
#     def get(self, request):
#         good = Good.objects.all()
#         json_data = serializers.serialize('json', good)
#
#         # return HttpResponse(json_data, content_type='application/json')
#         # 对于json类型的响应对象，需要指定content_type为“application/json”
#
#         json_data = json.loads(json_data)
#         return JsonResponse(json_data, safe=False)  # 可将一个字典或者其它的可序列化的python数据结构转换成json响应对象
# class GoodDetailView(View):
#     def get(self, request, pk):
#         good = Good.objects.get(pk=pk)
#         good = model_to_dict(good)
#         good['productImageBig'] = 'http://127.0.0.1:8000/media/' + str(good['productImageBig'])
#         json_data = json.dumps(good, cls=DateEncoder)
#         return HttpResponse(json_data, content_type='application/json')


class LargeResultsSetPagination(PageNumberPagination):  # 继承
    page_size = 20  # 记住这几个可以配置的属性的名字
    page_size_query_param = 'size'
    max_page_size = 80


class GoodListView(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodListSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.query_params.get('sort')
        priceGt = self.request.GET.get('priceGt')
        priceLte = self.request.GET.get('priceLte')
        cid = self.request.GET.get('cid')
        # print(priceGt, priceLte)
        if sort == '1':
            queryset = queryset.order_by('salePrice')
        elif sort == '-1':
            queryset = queryset.order_by('-salePrice')
        elif priceGt != '':
            queryset = queryset.filter(salePrice__gt=priceGt)
        elif priceLte != '':
            queryset = queryset.filter(salePrice__let=priceLte)
        elif cid:
            queryset = queryset.filter(category_id=cid)
        return queryset


class GoodDetailView(generics.RetrieveAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodDetailSerializer



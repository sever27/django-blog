# -*- coding: utf-8 -*-


from rest_framework.views import APIView    # 导入APIView

from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(http_method_names=['post'])  # 只允许post
# @permission_classes((permissions.AllowAny,))
def add_user(request):
    # print(request.data['data'])

    # res = {
    #     "code": 1,
    #     "data": 'data',
    #     "msg": "success"
    # }
    # return Response(res)
    print('==========')

    parameter = request.data
    id = parameter['data']
    print(id)
    if id == 1:
        data = 'There are three dogs'
    elif id == 2:
        data = 'There are two dogs'
    else:
        data = 'nothing'
    return Response({'data': data})

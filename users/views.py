from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from users.models import Users
from rest_framework.views import APIView
from django.core.serializers import serialize
from rest_framework import serializers


class OrderNoSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=64, required=False)
    user_password = serializers.CharField(max_length=15, required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_password', 'user_email')


class Authors_view(APIView):
    def get(self, request):
        serializer = OrderNoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = Users.objects.get(user_name=data.get('user_name'))
        res_data = UserSerializer(user).data
        print(res_data)
        if user and res_data['user_password'] == data['user_password']:
            res = {
                "code": 1,
                "data": res_data,
                "msg": "success"
            }
            return JsonResponse(res)
        else:
            res = {
                "code": 0,
                "data": {},
                "msg": "账号或密码错误"
            }
            return JsonResponse(res)


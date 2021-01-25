from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from users.models import Articles
from rest_framework.views import APIView
from django.core.serializers import serialize
from rest_framework import serializers


class OrderNoSerializer(serializers.Serializer):
    user = serializers.CharField()
    article_title = serializers.CharField()
    article_content = serializers.CharField()
    article_views = serializers.CharField()
    article_comment_count = serializers.CharField()
    article_date = serializers.CharField()
    article_like_count = serializers.CharField()

    class Meta:
        model = Articles

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('user', 'article_title', 'article_content', 'article_views', 'article_views', 'article_comment_count',
                  'article_date', 'article_like_count')



class add_articles(APIView):
    def post(self, request):
        serializer = OrderNoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # data = serializer.validated_data
        if serializer.is_valid():
            serializer.save()
            res = {
                "code": 1,
                "msg": "success"
            }
            return JsonResponse(res)


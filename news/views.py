from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from news.models import News
from news.serializers import NewsListeSrializers, NewsCreateSerializers

class NewsLCView(ListCreateAPIView):
    queryset = News
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NewsCreateSerializers

        else:
            return NewsListeSrializers
            
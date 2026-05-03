from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from news.models import News
from news.serializers import NewsListeSrializers, NewsCreateSerializers
from rest_framework import viewsets

class NewsLCView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    
    serializer_class = NewsListeSrializers
    
    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListeSrializers
        elif self.action == 'create':
            return NewsCreateSerializers 
    
            
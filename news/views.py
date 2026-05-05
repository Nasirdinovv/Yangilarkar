from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from news.models import News, User_profile, Likes
from news.serializers import NewsListeSrializers, NewsCreateSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class NewsLCView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListeSrializers

    @action(detail=False, methods=['get'])
    def get_lastest_10_news(self, request):
        latest_news = self.get_queryset().order_by('-time')[:10]
        news_serializer = self.get_serializer(latest_news, many=True)
        return Response(data={"msg":"yangiliklar", "news": news_serializer.data})

    
    @action(detail=True, methods=['post'])
    def user_like(self, request, pk=None):
        news = self.get_object()
        user = User_profile.objects.get(user=request.user)
        
        try:
            like = Likes.objects.create(
                news = news,
                user = user,
            )
            return Response(data="Like bosildi")
        
        except Exception as e:
            print(f"error has been found error -> {e}")
            
            return Response(data="Like bosilmadi")
    
    
            
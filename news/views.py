from news.models import News, User_profile, Likes
from news.serializers import NewsListeSrializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema, no_body



class NewsLCView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListeSrializers

    @action(detail=False, methods=['get'])
    def get_lastest_10_news(self, request):
        news = self.get_queryset().order_by('-time')[:10]
        news_serializer = self.get_serializer(news, many=True)
        return Response(data={"msg":"yangiliklar", "news": news_serializer.data})

    
    @swagger_auto_schema(request_body=no_body)
    @action(detail=True, methods=['post'])
    def user_like(self, request, pk=None):
        news = self.get_object()

        if not request.user.is_authenticated:
            return Response(
                data={"msg": "Avval login qiling"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = User_profile.objects.get(user=request.user)
        
        try:
            Likes.objects.create(
                news=news,
                user=user,
            )
            return Response(data={"msg": "Like bosildi"})
        
        except Exception:
            return Response(
                data={"msg": "Bu yangilikka oldin like bosilgan"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    
            

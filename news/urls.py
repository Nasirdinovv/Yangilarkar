from django.urls import path
from news.views import NewsLCView


urlpatterns = [
    path('', NewsLCView.as_view(), name='news_create_and_list')
]

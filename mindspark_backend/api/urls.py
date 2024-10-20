# urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()

router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/<int:article_id>/', SummaryAPIView.as_view(), name='article-summary'),
    path('sentiment-analysis/<int:article_id>/', SentimentAnalysisAPIView.as_view(), name='sentiment-analysis'),
    path('wordcloud/<int:article_id>/', WordCloudAPIView.as_view(), name='wordcloud'),
    path('recommendation/', RecommendationArticlesAPIView.as_view(), name='qdrant'),
    path('fake-news/<int:article_id>/', FakeNewsAPIView.as_view(), name='fake-news'),
    path('similar-article/<int:article_id>/', SimilarArticlesAPIView.as_view(), name='similar-article'),
    path('chrome-extension/', ChromeExtensionAPIView.as_view(), name='chrome-extension'),
]
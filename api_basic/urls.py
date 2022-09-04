from django.urls import path,include
from .views import articale_detail, ArticleApiView,ArticleDetails,GenericAPIView,ArticleViewSet,ArticleGenericViewSet,ArticleModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
router.register('genricviewset',ArticleGenericViewSet,basename='genricviewset')
router.register('modelviewset',ArticleModelViewSet,basename='modelviewsets')

urlpatterns = [
    path('viewset/',include(router.urls)),#viewset
    path('viewset/<int:pk>/',include(router.urls)),
    # path('viewset-genric/',include(router.urls)),#genric viewset
    # path('viewset-genric/<int:pk>',include(router.urls)),
    # path('article/',views.article_list),
    path('article/',ArticleApiView.as_view()),
    # path('detail/<int:pk>/',articale_detail),
    path('detail/<int:id>/',ArticleDetails.as_view()),
    path('genric/article/',GenericAPIView.as_view()),

]
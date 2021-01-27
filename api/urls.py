from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('article',views.ArticleView)

urlpatterns = [
    # path('article/',views.ArticleListView.as_view(),name="list"),
    # path('article/<int:pk>/',views.ArtileListDetailView.as_view(),name="detail"),
    path('',include(router.urls))
]

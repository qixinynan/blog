from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search', views.search_view, name='search'),
    path('post', views.post_view, name='post'),
    path('<int:post_id>', views.post_detail_view, name='detail'),
]

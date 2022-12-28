from django.urls import path

from . import views

# todo register
urlpatterns = [
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name='logout'),
    path('logout/?P<next>', views.logout_view, name='logout'),
    path('<int:user_id>', views.detail_view, name="detail"),
]

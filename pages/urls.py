from django.urls import path
from .views import home, post_detail, about

urlpatterns = [
    path('', home, name='Home'),
    path('post/<int:post_id>/', post_detail, name='PostDetail'),
    path('about/', about, name='About'),
]
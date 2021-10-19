from django.urls import path, re_path
from django.conf.urls import url
from . import views
urlpatterns = [
        path('', views.ProductListView.as_view(), name="home"),
        path('product/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    ]

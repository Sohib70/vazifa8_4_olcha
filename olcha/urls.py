from .views import CategoryListApiView,SubcategoryListApiView
from django.urls import path

urlpatterns = [
    path('',CategoryListApiView.as_view()),
    path('category/<slug:parent_slug>/',SubcategoryListApiView.as_view())
]
# urls.py
from django.urls import path
from .views import UploadAndSearchView

urlpatterns = [
    path("search-image", UploadAndSearchView.as_view(), name="seach_image"),
]

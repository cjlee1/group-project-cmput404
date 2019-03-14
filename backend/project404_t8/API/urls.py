from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

# from . import views
from .viewsets import PostViewSet, uploadView, postView, profileView

urlpatterns =[
    # path('',uploadView, name="post_list"),
    path("upload/", uploadView, name="upload"),
    path("post/<int:id>", postView, name="Post"),
    path("profile/<>", profileView, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

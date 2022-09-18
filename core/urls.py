"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from apps.postsapp.views import PersonalPostViewSet, PostViewSet
from apps.accountsapp.views import UserDetail, RegisterUserAPIView, CustomAuthToken, AccountViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'personalposts', PersonalPostViewSet, basename='personalposts')
router.register(r'users', AccountViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('account/<pk>/detail', UserDetail.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    path('login/', CustomAuthToken.as_view()),
]

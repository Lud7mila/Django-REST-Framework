"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from lit_works.views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import routers
# router = routers.SimpleRouter()
# router.register(r'lit_works', LitWorkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    #path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/lit_works/
    # path('api/v1/lit_works/', LitWorkViewSet.as_view({'get': 'list'})),
    # path('api/v1/lit_works/<int:pk>/', LitWorkViewSet.as_view({'put': 'update'})),
    # path('api/v1/lit_works_detail/<int:pk>/', LitWorkAPIDetailView.as_view()),

    path('api/v1/lit_works/', LitWorksListAPIView.as_view()),
    path('api/v1/lit_works_create/', LitWorksCreateAPIView.as_view()),
    path('api/v1/lit_works/<int:pk>/', LitWorkAPIDetailView.as_view()),
    #path('api/v1/lit_works_detail/<int:pk>/', LitWorkAPIUpdate.as_view()),

    path('api/v1/authors/<int:pk>/', AuthorAPIDetailView.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

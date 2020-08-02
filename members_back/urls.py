from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewset import MemberViewSet


router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

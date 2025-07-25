from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, register_user

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
]
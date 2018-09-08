from django.urls import path
from rest_framework.routers import DefaultRouter

from reviews.views import ReviewViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, base_name='review')
router.register(r'companies', CompanyViewSet, base_name='company')
router.root_view_name

urlpatterns = router.urls

from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from ipware import get_client_ip

from reviews.models import Company, Review
from reviews.serializers import ReviewCreateSerializer, ReviewListSerializer, CompanySerializer, \
    ReviewDetailSerializer, CompanyDetailSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action in ('list', 'retrieve'):
            return Review.objects.filter(author=self.request.user)
        return Review.objects

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'create'):
            return IsAuthenticated(),
        return IsAdminUser(),  # root can update/delete any record

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ReviewCreateSerializer
        elif self.action == 'list':
            return ReviewListSerializer
        return ReviewDetailSerializer

    def save_serializer(self, serializer):
        ip, is_routable = get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)

    def perform_create(self, serializer):
        self.save_serializer(serializer)

    def perform_update(self, serializer):
        self.save_serializer(serializer)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return AllowAny(),
        elif self.action == 'create':
            return IsAuthenticated(),
        return IsAdminUser(),

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanyDetailSerializer
        return CompanySerializer


class IndexView(TemplateView):
    template_name = 'reviews/index.html'

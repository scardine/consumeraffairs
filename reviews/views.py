from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from ipware import get_client_ip

from reviews.models import Company
from reviews.serializers import ReviewCreateSerializer, ReviewListSerializer, CompanySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.review_set.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ReviewCreateSerializer
        return ReviewListSerializer

    def save_serializer(self, serializer):
        ip, is_routable = get_client_ip(self.request)
        serializer.save(user=self.request.user, ip=ip)

    def perform_create(self, serializer):
        self.save_serializer(serializer)

    def perform_update(self, serializer):
        self.save_serializer(serializer)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return AllowAny(),
        elif self.action == 'create':
            return IsAuthenticated(),
        return IsAdminUser(),

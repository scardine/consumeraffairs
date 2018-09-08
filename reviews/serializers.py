from rest_framework import serializers
from reviews.models import Review, Company


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['ip', 'author']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = Review
        fields = "__all__"
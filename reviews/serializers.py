from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Review, Company


class CompanyDetailSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return obj.review_set.aggregate(avg=Avg('rating')).get('avg')

    class Meta:
        model = Company
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['ip', 'author',]


class ReviewListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = Review
        exclude = ["author", "summary", "ip"]


class ReviewDetailSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer(many=False)

    class Meta:
        model = Review
        exclude = ["author",]

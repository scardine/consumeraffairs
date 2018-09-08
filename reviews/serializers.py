from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Review, Company


class CompanyDetailSerializer(serializers.ModelSerializer):
    """This serializer is used for the retrieve endpoint. It has a "rating" field
    containing the average rating for this company which is potentially expensive."""
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return obj.review_set.aggregate(avg=Avg('rating')).get('avg')

    class Meta:
        model = Company
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """This is a lighter Serializer used in most methods"""
    class Meta:
        model = Company
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    """This serializer is used for creation/update, since we always take user_id and IP
    from the request instead of trusting the user.
    """
    class Meta:
        model = Review
        exclude = ['ip', 'author',]


class ReviewListSerializer(serializers.ModelSerializer):
    """This is a lighter serializer for use in the list views"""
    company = CompanySerializer(many=False)

    class Meta:
        model = Review
        exclude = ["author", "summary", "ip"]


class ReviewDetailSerializer(serializers.ModelSerializer):
    """This is a heavier serializer used on the detail endpoints"""
    company = CompanyDetailSerializer(many=False)

    class Meta:
        model = Review
        exclude = ["author",]

from django.contrib.auth.models import User
from django.urls import path, include, reverse
from rest_framework.test import APITestCase

from reviews.models import Company, Review

LOREM = (
    "Tagclouds, applications engineer compelling seamless communities share "
    "syndicate enable user-centric, utilize envisioneer orchestrate integrate."
    " Seamless out-of-the-box brand user-centred 24/365 scalable extensible,"
    " expedite reinvent extend paradigms. Recontextualize vertical, engage "
    "innovate standards-compliant world-class incubate plug-and-play "
    "experiences. One-to-one ecologies reintermediate, synthesize: users "
    "transition web services wikis. Cross-media blogging incentivize, "
    "reinvent end-to-end iterate; portals eyeballs e-services enable "
    "synergies mission-critical matrix: granular e-services networks "
    "open-source."
)


class ReviewsAPITestCase(APITestCase):
    urlpatterns = [
        path('api/v1/', include('reviews.urls')),
    ]

    def setUp(self):
        self.root = User.objects.create_superuser("root", "root@eruditorun.org", "cacc")
        self.user = User.objects.create_user("john", "john@eruditorun.org", "cacc")
        self.company = Company.objects.create(name="ConsumerAffairs")
        Review.objects.create(
            author=self.root,
            title="Root's Review",
            summary=LOREM,
            rating=5,
            company=self.company,
            ip="127.0.0.1",
        )
        Review.objects.create(
            author=self.user,
            title="John's Review",
            summary=LOREM,
            rating=3,
            company=self.company,
            ip="127.0.0.1",
        )

    def test_create_review(self):
        url = reverse('review-list')
        self.client.login(username='root', password='cacc')
        response = self.client.post(url, data={
            "title": "Best Company Ever",
            "summary": LOREM,
            "rating": 5,
            "company": 1,
        })
        self.assertEqual(response.status_code, 201)

    def test_user_cant_read_others_review(self):
        url = reverse('review-detail', kwargs={"pk": 1})
        self.client.login(username='john', password='cacc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        url = reverse('review-detail', kwargs={"pk": 2})
        self.client.login(username='root', password='cacc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_user_cant_read_own_review(self):
        url = reverse('review-detail', kwargs={"pk": 2})
        self.client.login(username='john', password='cacc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('review-detail', kwargs={"pk": 1})
        self.client.login(username='root', password='cacc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


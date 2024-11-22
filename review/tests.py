from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from .models import Review

User = get_user_model()


# Create your tests here.
class ReviewModelTest(TestCase):
    def setUp(self):
        """
        Set up test data for the Review model.
        """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=99.99,
            quantity=10
        )
        self.review_text = "This is a test review."

    def test_create_review(self):
        """
        Test that a review can be successfully created.
        """
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            review=self.review_text
        )
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.review, self.review_text)
        self.assertIsNotNone(review.created_at)

    def test_review_str_method(self):
        """
        Test the __str__ method of the Review model.
        """
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            review=self.review_text
        )
        expected_str = f"Review by {self.user.username} on {self.product.name}"
        self.assertEqual(str(review), expected_str)

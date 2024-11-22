from django.test import TestCase
from product.models import Product


# Create your tests here.
class ProductModelTest(TestCase):
    def setUp(self):
        """
        Set up test data for the Product model.
        """
        self.product = Product.objects.create(
            name="Test Product",
            description="A sample product for testing purposes.",
            price=199.99,
            quantity=50,
            stock_status='in_stock',
        )

    def test_product_creation(self):
        """
        Test that a Product instance can be created successfully.
        """
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "A sample product for testing purposes.")
        self.assertEqual(self.product.price, 199.99)
        self.assertEqual(self.product.quantity, 50)
        self.assertEqual(self.product.stock_status, 'in_stock')
        self.assertIsNotNone(self.product.id)

    def test_product_str_method(self):
        """
        Test the __str__ method of the Product model.
        """
        self.assertEqual(str(self.product), "Test Product")

    def test_default_stock_status(self):
        """
        Test that the default stock_status is set to 'in_stock'.
        """
        new_product = Product.objects.create(
            name="New Product",
            description="Another test product.",
            price=50.00,
            quantity=10,
        )
        self.assertEqual(new_product.stock_status, 'in_stock')

    def test_image_field_can_be_blank(self):
        """
        Test that the image field can be left blank or null.
        """
        self.assertIsNone(self.product.image)

    def test_stock_status_choices(self):
        """
        Test that the stock_status field only accepts valid choices.
        """
        with self.assertRaises(ValueError):
            self.product.stock_status = 'invalid_status'
            self.product.full_clean()

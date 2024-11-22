"""
1. CartItemAddSerializer
2. CartItemSerializer
3. CartSerializer
4. CheckoutSerializer
5. OrderItemSerializer
6. OrderSerializer
7. OrderTrackingSerializer
"""
from rest_framework import serializers
from product.models import Product
from .models import Order, OrderItem, Cart, CartItem


# =================== 1. CartItemAddSerializer ===================
class CartItemAddSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=0)

    def validate(self, attrs):
        product = attrs['product']
        quantity = attrs['quantity']

        if product.quantity < quantity:
            raise serializers.ValidationError("We don't have that much quantity. Would you please mind to take less.")
        return attrs


# ======================= 2. CartItemSerializer ===================
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'product_name', 'unit_price', 'quantity', 'total_price']


# =================== 3. CartSerializer =================================
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items', 'grand_total', 'status', 'created_at']


# ========================== 4. CheckoutSerializer ==============================
class CheckoutSerializer(serializers.Serializer):
    shipping_address = serializers.CharField()

    def validate(self, attrs):
        cart = Cart.objects.filter(user=self.context['request'].user, status='active').first()
        if not cart or not cart.cart_items.exists():
            raise serializers.ValidationError("Nothing added. Please add items")
        return attrs


# ========================== 5. OrderItemSerializer ===================================
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'quantity', 'unit_price', 'total_price']


# ========================= 6. OrderSerializer ===========================
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'updated_at', 'status', 'order_items',
                  'grand_total', 'payment_status', 'shipping_address', 'created_at']


# =========================== 7. OrderTrackingSerializer ============================
class OrderTrackingSerializer(serializers.Serializer):
    order_number = serializers.CharField()

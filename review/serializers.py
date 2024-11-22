from rest_framework import serializers

from .models import Review
from order.models import Order, OrderItem


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'review', 'product', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def validate(self, attrs):
        user = self.context['request'].user
        product = attrs['product']
        exists = OrderItem.objects.filter(order__user=user, product=product, order__status='completed').exists()
        if not exists:
            raise serializers.ValidationError({'product': 'This product is not supposed to take review'})
        return attrs

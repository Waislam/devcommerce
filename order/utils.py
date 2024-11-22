from .models import Order, OrderItem
from product.tasks import check_product_stock


def converting_cart_to_order(cart, target_address):
    """  Converts a shopping cart into an order and updates product stock. """
    order = Order.objects.create(
        user=cart.user,
        grand_total=cart.grand_total,
        status='processing',
        shipping_address=target_address
    )
    for cart_item in cart.cart_items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            unit_price=cart_item.unit_price,
            total_price=cart_item.total_price
        )
        product = cart_item.product
        product.quantity -= cart_item.quantity
        product.save()
        check_product_stock.apply_async(args=[product.id])
    cart.status = 'ordered'
    cart.save()

    return order

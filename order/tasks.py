from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from order.models import Order


@shared_task(name='order_confirmation_email')
def send_order_confirmation_email(batch_size=10):
    for order in Order.objects.filter(status='completed', is_send_email=False).order_by('created_at')[:batch_size]:
        if order.user.email:
            send_mail(
                subject='Payment Confirmation for Order @{0}'.format(order.id),
                message='Thanks for your payment. Your order @{0} has been processed.'.format(order.id),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.user.email],
                fail_silently=False,
            )
            order.is_send_email = True
            order.save()

# try:
#     send_mail(
#         subject='Payment Confirmation for Order @{0}'.format(order.id),
#         message='Thanks for your payment. Your order @{0} has been processed.'.format(order.id),
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[order.user.email],
#         fail_silently=False,
#     )
#     order.is_send_email = True
#     order.save()
# except Exception as e:
#     # Log the error
#     print(f"Error sending email for order {order.id}: {e}")

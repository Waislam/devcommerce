from django.conf import settings
from django.core.mail import send_mail


def send_stock_alert_email(self, stock_status):
    send_mail(
        subject='Alert: {0} is {1}'.format(self.name, stock_status),
        message='The product "{0}" is currently {1}.Please review the stock level and consider restocking.'.format(
            self.name, stock_status),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['stock@devcommerce.com'],
        fail_silently=False,
    )

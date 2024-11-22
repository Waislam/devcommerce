from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devcommerce.settings')

app = Celery('devcommerce')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send_order_confirmation': {
        'task': 'order_confirmation_email',
        'schedule': crontab(minute='*/1'),
        'options': {
            'expires': 1 * 60,
        },
    },
}

app.autodiscover_tasks()



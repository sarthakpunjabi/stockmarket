from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE','stockmarket.settings')
app = Celery('stockmarket')
app.conf.enable_utc = False
app.conf.update(timezone = 'Europe/Dublin')

app.config_from_object(settings,namespace='CELERY')
app.conf.beat_schedule = {
    # 'every-10-seconds': {
    #     'task': 'stockapp.tasks.update_stock',
    #     'schedule':10,
    #     'args':(['RELIANCE.NS','BAJAJFINSV.NS'],)

    # }
}

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')
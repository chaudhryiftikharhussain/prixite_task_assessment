import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prixite_task_assessment.settings')

application = get_wsgi_application()

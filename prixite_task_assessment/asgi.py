import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prixite_task_assessment.settings')

application = get_asgi_application()


from django.conf.urls import url

from custom_templates import views

urlpatterns = [
    url('', views.template_1, name='template_1'),
]
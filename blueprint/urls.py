from django.conf.urls import url
from .views import ExecuteBluePrintView, generate_blueprint

urlpatterns = [
    url(r'^$', ExecuteBluePrintView.as_view(), name='exec_blueprint'),
    url(r'^generate/', generate_blueprint, name='generate'),

]

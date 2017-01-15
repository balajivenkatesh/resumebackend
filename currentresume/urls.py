from django.conf.urls import url
from currentresume.views import CurrResumeView

urlpatterns = [
    url(r'^$', CurrResumeView.as_view(), name='index')
]
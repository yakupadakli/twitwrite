from django.conf.urls import url
from tweet.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
]

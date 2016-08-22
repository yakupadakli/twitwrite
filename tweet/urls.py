from django.conf.urls import url
from tweet.views import IndexView, PostTweetView, TweetSuccessView, TweetErrorView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^tweet/$', PostTweetView.as_view(), name="post-tweet"),
    url(r'^tweet/success/$', TweetSuccessView.as_view(), name="tweet-success"),
    url(r'^tweet/error/$', TweetErrorView.as_view(), name="tweet-error"),
]

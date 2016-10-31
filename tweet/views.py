import logging
import twitter

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormMixin

from tweet.forms import TweetForm


logger = logging.getLogger(__name__)


class IndexView(FormMixin, TemplateView):
    template_name = "tweet/index.html"
    form_class = TweetForm


class PostTweetView(View):
    success_url = reverse_lazy("tweet-success")
    error_url = reverse_lazy("tweet-error")

    def post(self, request, *args, **kwargs):
        context = {"status": True, "success_url": self.success_url.lower(), "error_url": self.error_url.lower()}
        social_auth = request.user.social_auth.first()
        oauth_token = social_auth.access_token.get("oauth_token")
        oauth_token_secret = social_auth.access_token.get("oauth_token_secret")
        twitter_consumer_key = getattr(settings, "SOCIAL_AUTH_TWITTER_KEY", "")
        twitter_consumer_secret = getattr(settings, "SOCIAL_AUTH_TWITTER_SECRET", "")
        try:
            t = twitter.Twitter(
                auth=twitter.OAuth(oauth_token, oauth_token_secret, twitter_consumer_key, twitter_consumer_secret)
            )
            t_up = twitter.Twitter(
                domain="upload.twitter.com",
                auth=twitter.OAuth(oauth_token, oauth_token_secret, twitter_consumer_key, twitter_consumer_secret)
            )

            image_data = request.POST.get("image")
            image_data = image_data.replace("data:image/png;base64,", "")
            image = open("tmp/image.png", "wb")
            image.write(image_data.decode('base64'))
            image.close()
            with open("tmp/image.png", "rb") as imagefile:
                imagedata = imagefile.read()
                image_id = t_up.media.upload(media=imagedata)["media_id_string"]
            t.statuses.update(status="", media_ids=",".join([image_id]))
        except Exception, e:
	    logger.error("Error: %s" % e)
            context["status"] = False
        return JsonResponse(context)


class TweetSuccessView(TemplateView):
    template_name = "tweet/success.html"


class TweetErrorView(TemplateView):
    template_name = "tweet/error.html"

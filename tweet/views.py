from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin

from tweet.forms import TweetForm


class IndexView(FormMixin, TemplateView):
    template_name = "tweet/index.html"
    form_class = TweetForm

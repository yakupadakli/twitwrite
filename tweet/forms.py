from django import forms

from tweet.models import Tweet


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ("title", "body", "signature")

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            field.widget.attrs["title"] = field.label
            field.widget.attrs["class"] = "form-control"

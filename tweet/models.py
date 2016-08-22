from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Tweet(models.Model):
    title = models.CharField(_(u"Title"), max_length=64, null=True, blank=True)
    body = models.TextField(_(u"Tweet"), null=True, blank=True)
    signature = models.CharField(_(u"Signature"), max_length=32, null=True, blank=True)

    def __unicode__(self):
        return self.title or self.body[:100]

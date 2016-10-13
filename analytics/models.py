from django.db import models

from zerver.models import Realm, UserProfile, Stream, Recipient
from zerver.lib.str_utils import ModelReprMixin
import datetime

from six import text_type
from typing import Optional, Tuple, Union

from analytics.lib.interval import MIN_TIME

# would only ever make entries here by hand
class Anomaly(ModelReprMixin, models.Model):
    info = models.CharField(max_length=1000) # type: text_type

    def __unicode__(self):
        # type: () -> text_type
        return u"<Anomaly: %s... %s>" % (self.info, self.id)

class BaseCount(ModelReprMixin, models.Model):
    # Note: When inheriting from BaseCount, you may want to rearrange
    # the order of the columns in the migration to make sure they
    # match how you'd like the table to be arranged.
    property = models.CharField(max_length=40) # type: text_type
    end_time = models.DateTimeField() # type: datetime.datetime
    interval = models.CharField(max_length=20) # type: text_type
    value = models.BigIntegerField() # type: int
    anomaly = models.ForeignKey(Anomaly, null=True) # type: Optional[Anomaly]

    class Meta(object):
        abstract = True

    @staticmethod
    def extended_id():
        # type: () -> Tuple[str, ...]
        raise NotImplementedError

    @staticmethod
    def key_model():
        # type: () -> models.Model
        raise NotImplementedError

class InstallationCount(BaseCount):

    class Meta(object):
        unique_together = ("property", "end_time", "interval")

    @staticmethod
    def extended_id():
        # type: () -> Tuple[str, ...]
        return ()

    @staticmethod
    def key_model():
        # type: () -> models.Model
        return None

    def __unicode__(self):
        # type: () -> text_type
        return u"<InstallationCount: %s %s>" % (self.property, self.value)

class RealmCount(BaseCount):
    realm = models.ForeignKey(Realm)

    class Meta(object):
        unique_together = ("realm", "property", "end_time", "interval")

    @staticmethod
    def extended_id():
        # type: () -> Tuple[str, ...]
        return ('realm_id',)

    @staticmethod
    def key_model():
        # type: () -> models.Model
        return Realm

    def __unicode__(self):
        # type: () -> text_type
        return u"<RealmCount: %s %s %s>" % (self.realm, self.property, self.value)

class UserCount(BaseCount):
    user = models.ForeignKey(UserProfile)
    realm = models.ForeignKey(Realm)

    class Meta(object):
        unique_together = ("user", "property", "end_time", "interval")

    @staticmethod
    def extended_id():
        # type: () -> Tuple[str, ...]
        return ('user_id', 'realm_id')

    @staticmethod
    def key_model():
        # type: () -> models.Model
        return UserProfile

    def __unicode__(self):
        # type: () -> text_type
        return u"<UserCount: %s %s %s>" % (self.user, self.property, self.value)

class StreamCount(BaseCount):
    stream = models.ForeignKey(Stream)
    realm = models.ForeignKey(Realm)

    class Meta(object):
        unique_together = ("stream", "property", "end_time", "interval")

    @staticmethod
    def extended_id():
        # type: () -> Tuple[str, ...]
        return ('stream_id', 'realm_id')

    @staticmethod
    def key_model():
        # type: () -> models.Model
        return Stream

    def __unicode__(self):
        # type: () -> text_type
        return u"<StreamCount: %s %s %s %s>" % (self.stream, self.property, self.value, self.id)

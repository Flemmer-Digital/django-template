from .mixins.timestamp_mixin import TimestampMixin


class BaseModel(TimestampMixin):
    class Meta:
        abstract = True

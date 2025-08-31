from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .middleware import _thread_locals
from mining_user.models import UserShift

DAY_SHIFT = (
    (100, _('Өдөр')),
    (200, _('Шөнө')),
)


user_model = settings.AUTH_USER_MODEL

ENTRY_TYPE_FACTORY = (
    (100, _('Төлөвлөгөө')),
    (200, _('Гүйцэтгэл')),
)

FACTORY_CONCENTRATOR_TYPE = (
    (100, _('БҮ-1')),
    (200, _('БҮ-2')),
)

FACTORY_CONCENTRATOR_LINE_TYPE = (
    (100, _('Шугам 1')),
    (200, _('Шугам 2')),
)


class BaseModel(models.Model):
    """
        Tracks instance creations, updates, and (soft) deletions.
    """

    created_by = models.ForeignKey(
        to=user_model,
        verbose_name=_("Бүртгэсэн"),
        null=True,
        blank=True,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Бүртгэсэн огноо"),
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    updated_by = models.ForeignKey(
        to=user_model,
        verbose_name=_("Зассан"),
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Зассан огноо"), auto_now=True, null=True, blank=True
    )

    class Meta:
        abstract = True

    # @property
    # def local_created_at(self):
    #     return timezone.localtime(self.created_at)
    #
    # @property
    # def local_updated_at(self):
    #     return timezone.localtime(self.updated_at) if self.updated_at else None


class AuditedOperatorModel(BaseModel):
    shift = models.IntegerField(null=True, choices=DAY_SHIFT)

    class Meta:
        abstract = True

class OpBaseShift(BaseModel):
    shift = models.IntegerField(choices=DAY_SHIFT, blank=True, null=True)
    operation_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, user=None, **kwargs):
        if user is None:
            user = getattr(_thread_locals, "user", None)

        try:
            user_shift = UserShift.objects.get(user=user)
        except UserShift.DoesNotExist:
            super(OpBaseShift, self).save(*args, **kwargs)
            return

        self.shift = user_shift.shift
        self.operation_date = user_shift.operation_date

        super(OpBaseShift, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} object (id={self.id})"


class FactoryBaseModel(OpBaseShift):
    entry_type = models.IntegerField(choices=ENTRY_TYPE_FACTORY, default=200)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} object (id={self.id})"


class ConcentratorBaseModel(FactoryBaseModel):
    concentrator_type = models.IntegerField(choices=FACTORY_CONCENTRATOR_TYPE, null=True)
    line_type = models.IntegerField(choices=FACTORY_CONCENTRATOR_LINE_TYPE, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} object (id={self.id})"

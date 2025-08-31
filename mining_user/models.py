from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

DAY_SHIFT = (
    (100, _('Өдөр')),
    (200, _('Шөнө')),
)




# Create your models here.

class UserShift(models.Model):
    FLOTATION_TYPE = ((100, _('1 дүгээр шугам')),
                      (200, _('2 дүгээр шугам')),)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shift = models.IntegerField(null=True, choices=DAY_SHIFT)
    operation_date = models.DateTimeField(null=True)
    flotation_type = models.IntegerField(null=True, choices=FLOTATION_TYPE)

    last_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'user_shifts'

    def __str__(self):
        return f'date: {self.operation_date}, shift:{self.shift}'


def get_user_shift_or_else_none(user):
    try:
        return UserShift.objects.get(user=user)
    except UserShift.DoesNotExist:
        return None

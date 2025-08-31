# Create your models here.
from django.core.validators import RegexValidator
from django.db import models

from base.models import ConcentratorBaseModel
from django.utils.translation import gettext_lazy as _
 
class ConcentratorOreFactory(ConcentratorBaseModel):
    """
        Үйлдвэр тэжээсэн хүдэр
    """
    # Regex to allow only capital letters (A-Z), numbers (0-9), and the colon (:) character
    uppercase_numeric_colon_validator = RegexValidator(
        # regex=r'^[A-Z0-9:]+$',
        regex=r'^([A-ZА-Я0-9]+)(:[A-ZА-Я0-9]+)*$',
        message='Зөвхөн том үсэг, тоо, болон (:) тэмдэгт ашиглана уу.'
    )

    numeric_colon_validator = RegexValidator(
        regex=r'^[0-9:]+$',
        message='Зөвхөн тоо болон (:) тэмдэгт ашиглана уу.'
    )
    block_number = models.CharField(null=True, blank=False, max_length=50,
                                    validators=[uppercase_numeric_colon_validator])
    mixed_ratio = models.CharField(null=True, blank=False, validators=[numeric_colon_validator])
    auto_pu_total_ore = models.FloatField(null=True)
    off_to_dump_ore = models.FloatField(null=True)  # буцааж овоолгод буулгасан хүдэр
    field_remaining = models.FloatField(null=True, blank=True)
    ore_moisture = models.FloatField(null=True)  # үйлдвэр тэжээсэн хүдрийн чийг
    description = models.TextField(null=True, blank=True)
    temp_factory_pu = 0.0

    class Meta:
        db_table = 'fc_concentrator_ore_factories'
        verbose_name = _('Үйлдвэр тэжээсэн хүдэр')

        permissions = [
            ('view_concentrator_dashboard', 'Can view concentrator dashboard')
        ]
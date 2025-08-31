from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ConcentratorOreFactory



class ConcentratorOreFactoryForm(forms.ModelForm):
    concentrator_type = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    line_type = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ConcentratorOreFactory
        fields = (
            'block_number',
            'mixed_ratio',
            'auto_pu_total_ore',
            'off_to_dump_ore',
            'field_remaining',
            'ore_moisture',
            'concentrator_type',
            'line_type',
            'description')

        labels = {
            'block_number': _('Овоолгын дугаар'),
            'mixed_ratio': _('Хольсон харьцаа'),
            'auto_pu_total_ore': _('Авто пүүгээр орсон нийт хүдэр (тн)'),
            'off_to_dump_ore': _('Буцааж овоолгод буулгасан хүдэр (тн)'),
            'field_remaining': _('Талбайн үлдэгдэл'),
            'ore_moisture': _('Үйлдвэр тэжээсэн хүдрийн чийг'),
            'description': _('Тайлбар'),
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }


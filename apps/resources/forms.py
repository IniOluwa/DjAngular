from django.forms import ModelForm
from models import Resources
from djng.forms import NgFormValidationMixin, NgModelFormMixin, AdPlaceHolderFormMixin
from crispy_forms import FormHelper


class ResourcesForm(NgModelFormMixin, ModelForm):
    """Form for Resources model"""
    def __init__(self, *args, **kwargs):
        super(ResourcesForm, self).__init__(*args, **kwargs)
        setup_bootstrap_helpers(self)

    class Meta(object):
        model = Resources
        fields = ('title', 'text')


def setup_bootstrap_helpers(object):
    object.helper = FormHelper()
    object.helper.form_class = 'form-horizontal'
    object.helper.label_class = 'col-lg-3'
    object.helper.field_class = 'col-lg-8'

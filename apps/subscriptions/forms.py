from django import forms
from django.utils.translation import override
from apps.subscriptions.models import Package, Feature
from modeltranslation.utils import get_translation_fields
from django_select2.forms import Select2MultipleWidget


class LanguageAwareModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        with override(self.lang):
            return str(obj)


class PackageAdminForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override both translated 'features' fields
        for lang in ['en', 'de']:
            field_name = f'features_{lang}'
            if field_name in self.fields:
                self.fields[field_name] = LanguageAwareModelMultipleChoiceField(
                    queryset=Feature.objects.all(),
                    lang=lang,
                    required=False,
                    widget=Select2MultipleWidget
                )

from django import forms
from apps.cms.models import Brand, Feature, HowItWork, Testimonial, Benefit
from django import forms
from django.utils.translation import override
from apps.cms.models import HowItWork, HowItWorkFeature
from django_select2.forms import Select2MultipleWidget

# Create a base form class to avoid repetition
class DropifyFormMixin:
    class Media:
        css = {
            'all': [
                'https://cdn.jsdelivr.net/npm/dropify/dist/css/dropify.min.css',
                '/static/admin/css/dropify-custom.css',
            ]
        }
        js = [
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdn.jsdelivr.net/npm/dropify/dist/js/dropify.min.js',
            '/static/admin/js/dropify-init.js',
        ]

class BrandForm(DropifyFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'logo': forms.ClearableFileInput(attrs={
                'class': 'dropify',
                'data-default-file': ''
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.logo:
            self.fields['logo'].widget.attrs['data-default-file'] = self.instance.logo.url

class FeatureForm(DropifyFormMixin, forms.ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
        widgets = {
            'logo': forms.ClearableFileInput(attrs={
                'class': 'dropify',
                'data-default-file': ''
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.logo:
            self.fields['logo'].widget.attrs['data-default-file'] = self.instance.logo.url

class TestimonialForm(DropifyFormMixin, forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'user_image': forms.ClearableFileInput(attrs={
                'class': 'dropify',
                'data-default-file': ''
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.user_image:
            self.fields['user_image'].widget.attrs['data-default-file'] = self.instance.user_image.url

class BenefitForm(DropifyFormMixin, forms.ModelForm):
    class Meta:
        model = Benefit
        fields = '__all__'
        widgets = {
            'logo': forms.ClearableFileInput(attrs={
                'class': 'dropify',
                'data-default-file': ''
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.logo:
            self.fields['logo'].widget.attrs['data-default-file'] = self.instance.logo.url


class HowItWorkDropifyFormMixin:
    class Media:
        css = {
            'all': [
                'https://cdn.jsdelivr.net/npm/dropify/dist/css/dropify.min.css',
                '/static/admin/css/dropify-custom.css',
            ]
        }
        js = [
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdn.jsdelivr.net/npm/dropify/dist/js/dropify.min.js',
            '/static/admin/js/dropify-init.js',
        ]
    def apply_dropify_widget(self):
        if 'side_image' in self.fields:
            self.fields['side_image'].widget = forms.ClearableFileInput(attrs={
                'class': 'dropify',
                'data-default-file': ''
            })




        if self.instance and self.instance.pk and getattr(self.instance, 'side_image', None):
            self.fields['side_image'].widget.attrs['data-default-file'] = self.instance.side_image.url

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_dropify_widget()



class LanguageAwareModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        with override(self.lang):
            return str(obj)


class HowItWorkForm(HowItWorkDropifyFormMixin, forms.ModelForm):
    class Meta:
        model = HowItWork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for lang in ['en', 'de']:
            field_name = f'features_{lang}'
            if field_name in self.fields:
                self.fields[field_name] = LanguageAwareModelMultipleChoiceField(
                    queryset=HowItWorkFeature.objects.all(),
                    lang=lang,
                    required=False,
                    widget=Select2MultipleWidget()
                )

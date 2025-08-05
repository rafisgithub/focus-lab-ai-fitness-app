from modeltranslation.translator import register, TranslationOptions
from .models import Feature, Package

@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Package)
class PackageTranslationOptions(TranslationOptions):
    fields = ('name','type','features')
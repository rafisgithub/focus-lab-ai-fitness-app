from modeltranslation.translator import register, TranslationOptions
from .models import (
    Brand,
    Feature,
    Page,
    Testimonial,
    Benefit,
    Faq,
    HeroSection,
    HowItWorkFeature,
    HowItWork,
    InterviewCoachSection,
    Footer,
    GlobalCta,
)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ("title", "short_description")


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "profession", "comment")


@register(Benefit)
class BenefitTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title")


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title")


@register(HowItWorkFeature)
class HowItWorkFeatureTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(HowItWork)
class HowItWorkTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title", "short_description", "features")


@register(InterviewCoachSection)
class InterviewCoachSectionTranslationOptions(TranslationOptions):
    fields = ("title", "short_description")


@register(Footer)
class FooterTranslationOptions(TranslationOptions):
    fields = ("content", "copyright_text")


@register(GlobalCta)
class GlobalCtaTranslationOptions(TranslationOptions):
    fields = ("title", "description", "button_text")

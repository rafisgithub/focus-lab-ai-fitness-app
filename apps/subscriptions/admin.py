from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.subscriptions.models import Feature, Package, Subscription, PaymentHistory
from django_select2.forms import Select2MultipleWidget
from apps.subscriptions.forms import PackageAdminForm
@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ('name',)  
    list_display_links = ('name',)
    search_fields = ('name',) 

    fieldsets = (
        (None, {
            "fields": (
                "name",  # This will show all language fields in the edit form
            )
        }),
    )


@admin.register(Package)
class PackageAdmin(ModelAdmin):

    model = Package
    form = PackageAdminForm

    list_display = ('id','name', 'stripe_price_id', 'stripe_product_id', 'price', 'type', 'enabled')
    list_display_links = ('id','name','price','type','enabled','stripe_price_id','stripe_product_id')
    list_filter = ('type', 'enabled')
    search_fields = ('name', 'stripe_product_id')
    ordering = ('id',)
    # filter_horizontal = ('features',)  # Use filter_horizontal for better UI with many-to-many fields


    fieldsets = (
        (None, {
            "fields": (
                "name",
                "price",
                "type",
                "enabled",
                "features",
            )
        }),
    )


@admin.register(Subscription)
class SubscriptionAdmin(ModelAdmin):
    list_display = ('id', 'user_first_name','user_last_name', 'user_email', 'package', 'status', 'start_date', 'end_date')
    list_display_links = ('id', 'user_first_name', 'user_last_name', 'user_email', 'package')
    search_fields = ('user__username', 'package__name')
    list_filter = ('status',)
    ordering = ('-start_date',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'package')
    
    def user_first_name(self, obj):
        return obj.user.profile.first_name if obj.user.profile else ''
    user_first_name.short_description = 'First Name'
    def user_last_name(self, obj):
        return obj.user.profile.last_name if obj.user.profile else ''
    user_last_name.short_description = 'Last Name'
    def user_email(self, obj):
        return obj.user.email if obj.user else ''
    user_email.short_description = 'Email'


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(ModelAdmin):
    list_display = (
        'id', 'user_first_name', 'user_last_name', 'package', 'user_email',
        'amount', 'payment_gateway', 'payment_status', 'paid_at'
    )
    list_display_links = (
        'id', 'user_first_name', 'user_last_name', 'package', 'user_email',
        'amount', 'payment_gateway', 'payment_status', 'paid_at'
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user__profile', 'package')

    def user_first_name(self, obj):
        return obj.user.profile.first_name
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.profile.last_name
    user_last_name.short_description = 'Last Name'

    def user_email(self, obj):
        return obj.user.email  # assuming email is still on the User model
    user_email.short_description = 'Email'

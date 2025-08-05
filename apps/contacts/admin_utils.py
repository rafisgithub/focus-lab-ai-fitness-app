# apps/contacts/admin_utils.py

from apps.contacts.models import Contact

def unread_contact_badge(request):
    if not request.user.is_superuser:
        return None  # Only show to superusers

    count = Contact.objects.filter(is_read=False).count()
    return str(count) if count > 0 else None

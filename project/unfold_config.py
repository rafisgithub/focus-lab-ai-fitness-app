from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from apps.system_setting.admin_profile import update_profile


def get_about_system():
    from apps.system_setting.models import AboutSystem
    return AboutSystem.objects.first()

def get_unfold_settings():
    return {
        "SITE_TITLE": lambda request: get_about_system().title,
        "SITE_HEADER": lambda request: get_about_system().title,
        "SITE_SUBHEADER": lambda request: get_about_system().title,
        "SITE_URL": "/",
        "SITE_ICON": {
            "light": lambda request: get_about_system().logo.url,  # light mode
            "dark": lambda request: get_about_system().logo.url,  # dark mode
        },
        "SITE_SYMBOL": "speed",  # symbol from icon set
        "SITE_FAVICONS": [
            {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: get_about_system().favicon.url,
            },
        ],
        "SHOW_HISTORY": True,  # show/hide "History" button, default: True
        "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
        "SHOW_BACK_BUTTON": True,  # show/hide "Back" button on changeform in header, default: False
        "THEME": "light",
        "LOGIN": {
            "image": lambda request: static("sample/login-bg.jpg"),
            "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
        },
        "BORDER_RADIUS": "6px",
        "SIDEBAR": {
            "show_search": True,  # Search in applications and models names
            "show_all_applications": True,  # Dropdown with all applications and models
            "navigation": [
                {
                   
                    "items": [
                        {
                            "title": _("Dashboard"),
                            "icon": "dashboard",
                            "link": reverse_lazy("admin:index"),
                            "permission": lambda request: request.user.is_superuser,
                        },
                    ],
                },
                {
                    "title": _("User Management"),
                    "separator": True,  # Top border
                    "collapsible": True,  # Collapsible group of links
                    "items": [
                        {
                            "title": _("Users"),
                            "icon": "people",
                            "link": reverse_lazy("admin:users_user_changelist"),
                        },
                    ],
                },

                 {
                    "title": _("Workouts"),
                    "separator": True, 
                    "collapsible": True, 
                    "items": [
                        {
                            "title": _("Categories"),
                            "icon": "category", 
                            "link": reverse_lazy("admin:workouts_category_changelist"),
                        },
                    
                        {
                            "title": _("All Workouts"),
                            "icon": "list",
                            "link": reverse_lazy("admin:workouts_workout_changelist"),
                        },
                        
                    ],
                },
               
                {
                    "title": _("System Setting"),
                    "separator": True,
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("Update Profile"),
                            "icon": "edit",
                            "link": lambda req: update_profile(req),
                        },
                        {
                            "title": _("About System"),
                            "icon": "info",
                            "link": reverse_lazy(
                                "admin:system_setting_aboutsystem_changelist"
                            ),
                        },
                        {
                            "title": _("Social Media"),
                            "icon": "share",
                            "link": reverse_lazy(
                                "admin:system_setting_socialmedia_changelist"
                            ),
                        },
                        {
                            "title": _("SMTP Settings"),
                            "icon": "email",
                            "link": reverse_lazy(
                                "admin:system_setting_smtpsetting_changelist"
                            ),
                        },
                    ],
                },
               
            ],
        },
}

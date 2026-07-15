from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "subscription",
        "country",
        "is_staff",
    )

    search_fields = (
        "email",
    )

    list_filter = (
        "subscription",
        "country",
    )
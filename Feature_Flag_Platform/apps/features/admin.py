from django.contrib import admin

from .models import (
    Feature,
    FeatureRule,
    FeatureSchedule,
    FeatureTarget,
)


class FeatureRuleInline(admin.TabularInline):

    model = FeatureRule

    extra = 0


class FeatureTargetInline(admin.TabularInline):

    model = FeatureTarget

    extra = 0


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):

    list_display = (

        "key",

        "enabled",

        "rollout_percentage",

        "created_at",

    )

    search_fields = (

        "key",

        "title",

    )

    list_filter = (

        "enabled",

    )

    inlines = [

        FeatureRuleInline,

        FeatureTargetInline

    ]
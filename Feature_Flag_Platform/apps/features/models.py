import uuid

from django.db import models

from .choices import (
    RuleType,
    Operator
)

class Feature(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    key = models.CharField(
        max_length=100,
        unique=True
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    enabled = models.BooleanField(
        default=False
    )

    rollout_percentage = models.PositiveSmallIntegerField(
        default=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["key"]

        indexes = [

            models.Index(fields=["key"]),

            models.Index(fields=["enabled"])

        ]

    def __str__(self):

        return self.key


class FeatureRule(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    feature = models.ForeignKey(

        Feature,

        on_delete=models.CASCADE,

        related_name="rules"

    )

    rule_type = models.CharField(

        max_length=30,

        choices=RuleType.choices

    )

    operator = models.CharField(

        max_length=10,

        choices=Operator.choices

    )

    value = models.CharField(

        max_length=200

    )

    priority = models.PositiveIntegerField(

        default=1

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        ordering = [

            "priority"

        ]


class FeatureTarget(models.Model):

    feature = models.ForeignKey(

        Feature,

        on_delete=models.CASCADE

    )

    user = models.ForeignKey(

        "accounts.User",

        on_delete=models.CASCADE

    )

    enabled = models.BooleanField(

        default=True

    )
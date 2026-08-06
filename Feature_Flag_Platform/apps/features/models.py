import uuid

from django.db import models


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
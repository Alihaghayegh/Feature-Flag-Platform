from django.db import models

class AuditLog(models.Model):

    action = models.CharField(
        max_length=100
    )

    feature = models.ForeignKey(

        "features.Feature",

        on_delete=models.CASCADE

    )

    user = models.ForeignKey(

        "accounts.User",

        on_delete=models.SET_NULL,

        null=True

    )

    payload = models.JSONField()

    created_at = models.DateTimeField(

        auto_now_add=True

    )
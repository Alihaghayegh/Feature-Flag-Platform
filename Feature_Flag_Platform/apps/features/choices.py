from django.db import models


class RuleType(models.TextChoices):
    COUNTRY = "country", "Country"
    AGE = "age", "Age"
    ROLE = "role", "Role"
    SUBSCRIPTION = "subscription", "Subscription"
    DEVICE = "device", "Device"
    PERCENTAGE = "percentage", "Percentage"
    TIME = "time", "Time"


class Operator(models.TextChoices):
    EQUAL = "eq", "="
    NOT_EQUAL = "neq", "!="
    GREATER = "gt", ">"
    LESS = "lt", "<"
    GREATER_EQUAL = "gte", ">="
    LESS_EQUAL = "lte", "<="
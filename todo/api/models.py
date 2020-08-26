from django.db import models

status = (("nc", "not_completed"),
          ("c", "completed"),
          )


class Todo(models.Model):
    """Models."""
    name = models.CharField(max_length=255, null=False)

    todo_status = models.CharField(max_length=2, choices=status, null=False)
    active_status = models.BooleanField(default=True, null=False)

    date_added = models.DateTimeField(editable=False, auto_now_add=True, null=False)
    date_updated = models.DateTimeField(editable=False, auto_now=True, null=False)

    user_id = models.UUIDField(null=False)

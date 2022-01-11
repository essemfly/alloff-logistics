import uuid
from django.db import models


class Payment(models.Model):

    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    # user info
    user_id = models.CharField(max_length=20)

    # payment info
    transaction_id = models.CharField(max_length=255)
    method = models.CharField(
        max_length=20,
    )
    bank_account_info = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

from django.db import models


class User(models.Model):

    name = models.CharField(max_length=20)
    shipping_address = models.ForeignKey('Address', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Address(models.Model):

    display_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=13)
    base_address = models.CharField(max_length=255)
    detail_address = models.CharField(null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Log(models.Model):

    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.DO_NOTHING)


# from backoffice-server
class Courier(models.Model):
    name = models.CharField(max_length=30)
    sweettracker_id = models.CharField(max_length=6)
    tracking_url_base = models.TextField(
        default="https://search.naver.com/search.naver?query=", blank=True)

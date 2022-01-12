from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=30)
    sweettracker_id = models.CharField(max_length=6)
    tracking_url_base = models.TextField(
        default="https://search.naver.com/search.naver?query=", blank=True
    )

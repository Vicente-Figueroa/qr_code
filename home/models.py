from operator import mod
from pyexpat import model
from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Establishment(models.Model):
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=100)
    commune = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    direction = models.CharField(max_length=100)
    commune = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class QRcode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qr_image = models.ImageField(blank=True, null=True)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.PROTECT,
    )
    contacs = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
    )
    qrcode = models.OneToOneField(
        QRcode,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.first_name

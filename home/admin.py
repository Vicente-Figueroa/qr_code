from django.contrib import admin
from home.models import Profile, QRcode, Establishment, Contact

# Register your models here.
admin.site.register(Profile)
admin.site.register(QRcode)
admin.site.register(Establishment)
admin.site.register(Contact)

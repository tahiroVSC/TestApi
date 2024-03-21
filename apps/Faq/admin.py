from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.Faq.models import Faq
admin.site.register(Faq)


admin.site.unregister(Group)
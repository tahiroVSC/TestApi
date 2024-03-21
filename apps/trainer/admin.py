from django.contrib import admin

from apps.trainer.models import Trainer, Type_of_trainer


admin.site.register(Trainer)
admin.site.register(Type_of_trainer)


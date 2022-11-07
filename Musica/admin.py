from django.contrib import admin
from .models import Comentarios


class ComentariosAdmin(admin.ModelAdmin):
	readonly_fields = ("created", )
# Register your models here.

admin.site.register(Comentarios, ComentariosAdmin)
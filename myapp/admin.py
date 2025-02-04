from django.contrib import admin
from .models import databs, education, experience, contact, project
# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display = ('nama','email','message','sendat')


admin.site.register(databs)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(contact, contactadmin)
admin.site.register(project)
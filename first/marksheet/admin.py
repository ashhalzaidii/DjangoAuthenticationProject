from django.contrib import admin
from marksheet.models import Marksheet

class MarksheetAdmin(admin.ModelAdmin):
    list_display=('name','subject1','subject2','subject3','subject4','subject5','subject6')


admin.site.register(Marksheet,MarksheetAdmin)
# Register your models here.

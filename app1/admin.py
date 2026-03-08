from django.contrib import admin
from .models import student,principle
from .models import PrincipalMessage
from .models import Teachers
# from.models import user

# Register your models here.
class apply(admin.ModelAdmin):
     list_display= ['name','F_name','dep_name','Roll_number','address','email','marks']
     # search_fields = ['name','F_name','dep_name','Roll_number','address','email']
     # list_filter = ['sent_at']
admin.site.register(student,apply)

#Register principle model
class princi(admin.ModelAdmin):
     list_display=['first_name','last_name','age','email']
admin.site.register(principle,princi)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@admin.register(PrincipalMessage)
class PrincipalMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message','sent_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)
    
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Cant_teachers(admin.ModelAdmin):
     list_display=['name','f_name','P_number','email','address','message',]
     search_fields=['name','f_name','P_number',]
     list_filter=['sent_at']
admin.site.register(Teachers,Cant_teachers)
from django.contrib import admin
from .models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("word", "meaning", )

admin.site.register(suggest,MemberAdmin)

class Feedbackdata(admin.ModelAdmin):
  list_display = ("Name", "Email","Subject", "Message", )
admin.site.register(Feedback,Feedbackdata)
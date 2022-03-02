from django.contrib import admin
from testjobs.models import Hyderabadjobs,Bangalorejobs,punejobs

# Register your models here.
class HyderabadjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','phonenumber']
admin.site.register(Hyderabadjobs,HyderabadjobsAdmin)


class BangalorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','phonenumber']
admin.site.register(Bangalorejobs,BangalorejobsAdmin)


class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','phonenumber']
admin.site.register(punejobs,PunejobsAdmin)

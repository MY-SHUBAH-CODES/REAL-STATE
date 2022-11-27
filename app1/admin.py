from django.contrib import admin
from.models import Addland,Addplot


class AddlandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Addland,AddlandAdmin)



class AddplotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Addplot,AddplotAdmin)
         
from django.contrib import admin

# Register your models here.

from .models import Item, Udm

admin.site.register(Item)
admin.site.register(Udm)



from .models import Produto

admin.site.register(Produto)


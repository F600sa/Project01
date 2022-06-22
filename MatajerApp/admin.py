from django.contrib import admin
from .models import CommentModel,Profile,Product_Model


class profileAdmin(admin.ModelAdmin):
  list_display = ('name', 'education','user')
  list_filter = ('user',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','description','user')
    list_filter = ('name',)
    search_fields = ['name']

class commentAdmin(admin.ModelAdmin):
    list_display = ('content','user')
    date_hierarchy = 'created_at'

admin.site.register(Profile,profileAdmin)
admin.site.register(Product_Model,ProductAdmin)
admin.site.register(CommentModel,commentAdmin)

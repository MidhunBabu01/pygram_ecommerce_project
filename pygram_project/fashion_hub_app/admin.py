from django.contrib import admin
from admin_app.models import AdminProducts
# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Category, CategoryAdmin)    


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # list_display = ['name','price','stock','available']
    # list_editable =['price','stock','available']
admin.site.register(AdminProducts,ProductsAdmin)    
    
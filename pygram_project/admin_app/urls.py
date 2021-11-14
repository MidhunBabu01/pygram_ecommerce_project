from django.urls import path
from admin_app import views


app_name='admin_app'

urlpatterns = [
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_home',views.admin_home, name="admin_home"),
    path('delete/<int:item_id>',views.delete, name="delete"),
    path('update/<int:item_id>',views.update, name="update")
]
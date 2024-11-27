from django.urls import path
from Newapp import views
urlpatterns = [
    path('index/',views.index,name="index"),
    path('add_category/',views.addcategory,name="add_category"),
    path('save_category/',views.savecategory,name="save_category"),
    path('display_category/',views.displaycategory,name="display_category"),
    path('edit_category/<int:catid>/',views.editcategory,name="edit_category"),
    path('update_category/<int:catid>/',views.updatecategory,name="update_category"),
    path('delete_category/<int:catid>/',views.deletecategory,name="delete_category"),
    path('add_product/',views.addproduct,name="add_product"),
    path('save_product/',views.saveproduct,name="save_product"),
    path('display_product/',views.displayproduct,name="display_product"),
    path('edit_product/<int:proid>/',views.editproduct,name="edit_product"),
    path('update_product/<int:proid>/',views.updateproduct,name="update_product"),
    path('delete_product/<int:proid>/',views.deleteproduct,name="delete_product"),
    path('admin_login/',views.Admin_login,name="admin_login"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_display/',views.contact_display,name="contact_display"),
    path('delete_contact/<int:con>/',views.delete_contact,name="delete_contact"),
]
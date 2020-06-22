from django.urls import path,include
from basicApp import views as basicApp_views
from django.contrib import admin

urlpatterns = [
    path('',basicApp_views.index,name='index'),
    path('donate/admin/', admin.site.urls),
    path('donate/',basicApp_views.donate,name='donate'),
    path('borrow_list/admin/', admin.site.urls),
    path('borrow_list/',basicApp_views.borrow_list,name='borrow_list'),
    path('help/',basicApp_views.help,name='help'),
    path('book_details/<int:my_id>',basicApp_views.dynamic_lookup_view, name='book_details'),
    path('book_details/',basicApp_views.dynamic_lookup_view, name='book_details'),
]

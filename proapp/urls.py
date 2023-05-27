from django.urls import path
from proapp import views

urlpatterns=[
    path('',views.home),
    path('login/',views.login),
    path('logout/',views.logout),
   
   

    path('add/',views.add),
    path('my/',views.myprop,name="my"),
    path('delete/<int:pk>',views.delete),
    path('buyer/',views.buyerreg_view),
    path('owner/',views.ownerreg_view),
    path('owner_home',views.ownerhome),
    path('prop_detail/<int:id>',views.prop_detail),
    path('book/<int:pk>',views.book),
    path('req/',views.requests),
    path('approve/<int:pk>',views.approve_booking),
    path('reject/<int:pk>',views.reject_booking),
    path('mybook/',views.mybook),
    path('property/search/', views.property_search, name='property_search'),
    path('all',views.all)

    

    

]
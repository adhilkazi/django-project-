from django.urls import path
from.import views
urlpatterns = [
    path("",views.home, name="h"), #home path

#staff register
    path("ssing",views.staf_signup,name="sin") ,#singup page 
    path('slog',views.login_staff,name="slog"),  #show login page
    path('staff_log/',views.staff_log,name="staff_log"),
    path('sdetail/',views.welcome_staff,name="sdetails"),

#staff aproovel
  path('approve/<int:user_id>/', views.approve_staff, name='approve_user') ,
  path('aprv/',views.aproov,name="aprv"),  


#customer registar  
    path('cusignup',views.user_singnup,name="cusignup"),
    path('cuslog',views.login_cust,name="cuslog"),
    path('cust_login/',views.cust_login,name="cust_login"),
    path('welcome/',views.welcome_user,name="welcome"),


#staff aproovel
  path('approve_cust/<int:user_id>/', views.approve_cust, name='approve_cust') ,
  path('aprv/',views.aproov,name="aprv"),  

#customer views
path('views/',views.views_cust,name="views"),
path('cust_views/<str:pk>',views.cust_views,name="cust_views"),
path('delete/<str:pk>',views.delete,name="delete"),
path('update_cust/<str:pk>',views.update_cust,name="update_cust"),

#image
path('up',views.uplode,name="up"),
path('imv/',views.image_vw,name='imv'),
# path('delete_img/<str:pk>',views.delete_img,name='delete_img'),
path('image/<str:pk>',views.image,name="image"),

#logout user
path('logoutstaf/',views.logoutstaf,name="logoutstaf"),
path('logoutuser/',views.logoutuser,name="logoutuser"),





    


]

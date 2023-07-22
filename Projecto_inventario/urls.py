from django.contrib import admin
from django.urls import path
from inventario import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('gestion_bodegas/', views.gestion_bodegas, name='gestion_bodegas'),
    path('crear_movimiento/', views.crear_movimiento, name='crear_movimiento'),
    path('lista_movimientos/', views.lista_movimientos, name='lista_movimientos'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('crear_detalle_movimiento/', views.crear_detalle_movimiento, name='crear_detalle_movimiento'), # Agregar esta línea
    path('crear_bodega/', views.crear_bodega, name='crear_bodega'),
    path('accounts/profile/', views.perfil_usuario, name='perfil_usuario'),
    path('', views.homepage, name='homepage'),
    
]


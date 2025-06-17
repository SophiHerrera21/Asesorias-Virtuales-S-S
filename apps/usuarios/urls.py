from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alias'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Recuperación de contraseña
    path('recuperar/', views.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('recuperar/codigo/', views.ingresar_codigo, name='ingresar_codigo'),
    path('recuperar/nueva/', views.nueva_contrasena, name='nueva_contrasena'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
    
    # Registro
    path('registro/seleccionar-rol/', views.seleccionar_rol, name='seleccionar_rol'),
    path('registro/aprendiz/', views.registro_aprendiz, name='registro_aprendiz'),
    path('registro/asesor/', views.registro_asesor, name='registro_asesor'),
    path('registro/coordinador/', views.registro_coordinador, name='registro_coordinador'),
    
    # Dashboards
    path('aprendiz/dashboard/', views.dashboard_aprendiz, name='dashboard_aprendiz'),
    path('aprendiz/componentes/', views.componentes_aprendiz, name='componentes_aprendiz'),
    path('aprendiz/grupos/', views.grupos_aprendiz, name='grupos_aprendiz'),
    path('aprendiz/pruebas/', views.pruebas_aprendiz, name='pruebas_aprendiz'),
    path('aprendiz/pqrs/', views.pqrs_aprendiz, name='pqrs_aprendiz'),
    path('aprendiz/notificaciones/', views.notificaciones_aprendiz, name='notificaciones_aprendiz'),
    path('aprendiz/reportes/', views.reportes_aprendiz, name='reportes_aprendiz'),
    
    path('asesor/dashboard/', views.dashboard_asesor, name='dashboard_asesor'),
    path('coordinador/dashboard/', views.dashboard_coordinador, name='dashboard_coordinador'),
    
    # Perfiles
    path('perfil/aprendiz/', views.perfil_aprendiz, name='perfil_aprendiz'),
    path('perfil/asesor/', views.perfil_asesor, name='perfil_asesor'),
    path('perfil/coordinador/', views.perfil_coordinador, name='perfil_coordinador'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    
    # Gestión de usuarios (Coordinador)
    path('coordinador/', views.lista_usuarios, name='lista_usuarios'),
    path('coordinador/crear/', views.crear_usuario, name='crear_usuario'),
    path('coordinador/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('coordinador/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('coordinador/toggle-estado/<int:usuario_id>/', views.toggle_estado_usuario, name='toggle_estado_usuario'),
    path('coordinador/configuracion/', views.configuracion_coordinador, name='configuracion_coordinador'),
    path('coordinador/entrada-unica-2024/', views.entrada_unica_coordinador, name='entrada_unica_coordinador'),
    
    # PQRS (Coordinador)
    path('pqrs/', views.pqrs_coordinador, name='pqrs_coordinador'),
    path('pqrs/<int:pqrs_id>/responder/', views.responder_pqrs, name='responder_pqrs'),
    path('pqrs/<int:pqrs_id>/cambiar-estado/', views.cambiar_estado_pqrs, name='cambiar_estado_pqrs'),
    path('pqrs/<int:pqrs_id>/detalles/', views.detalles_pqrs, name='detalles_pqrs'),
    
    # Reportes (Coordinador)
    path('reportes/', views.reportes_coordinador, name='reportes_coordinador'),
    path('exportar-reporte/', views.exportar_reporte, name='exportar_reporte'),
] 
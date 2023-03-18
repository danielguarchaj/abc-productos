from django.urls import path

from . import views

app_name = 'inventario'

urlpatterns = [
  path('', views.IndexView, name='index'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
  path('delete-product/<pk>', views.ProductDeleteView.as_view(), name='delete-product'),
  path('edit-product/<pk>', views.ProductUpdateView.as_view(), name='edit-product'),
  path('reportes/', views.ReportesView.as_view(), name='reportes'),
]
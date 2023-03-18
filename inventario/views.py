import json
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from inventario.models import Product, Category
from django.db.models import Sum, Count

from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

def IndexView(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('inventario:dashboard'))
    else:
        return redirect(reverse_lazy('inventario:login'))


class LoginView(auth_views.LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('inventario:dashboard'))
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(auth_views.LogoutView):
    pass


class DashboardView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard.html'
    model = Product
    fields = "__all__"
    success_url = '/dashboard/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/dashboard/'
    template_name = 'delete.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "edit.html"
    success_url = "/dashboard/"

  
class ReportesView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Category.objects.annotate(Count('category_products'))
        context['categories'] = json.dumps(
            [{"name": category.name, "products_count": category.category_products__count} for category in qs]
        )
        return context
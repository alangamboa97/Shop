from django.urls import path
from .views import MaterialView, ProductoView, Producto_MaterialView, CategoriaMView, CategoriaPView, TemporadaView

urlpatterns = [
    path('material', MaterialView.as_view()),
    path('producto', ProductoView.as_view()),
    path('productomaterial', Producto_MaterialView.as_view()),
    path('temporada', TemporadaView.as_view()),
    path('catM', CategoriaMView.as_view()),
    path('catP', CategoriaPView.as_view()),
]
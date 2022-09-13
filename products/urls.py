from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_alt_view),
    # path('',views.ProductListCreateView.as_view()),
    # path('',views.ProductCreateApiView.as_view()),
    # path('<int:pk>/update/',views.ProductDeleteApiView.as_view()),
    path('<int:pk>/update/',views.ProductUpdateApiView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteApiView.as_view()),
    path('<int:pk>/',views.product_alt_view)
]
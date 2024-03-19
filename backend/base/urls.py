from base import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin', admin.site.urls),

    path('register', views.register),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('refresh-token', views.refresh_token),

    path('products',views.products_public),
    path('products/<int:id>',views.products_public),
    path('authproducts', views.products),
    path('authproducts/<int:id>', views.products),

]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views  # Import views from your tasks app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Includes all task-related URLs
    
    # Auth URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Register URL (directly pointing to the view)
    path('register/', views.register, name='register'),
]
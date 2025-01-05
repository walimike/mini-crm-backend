from django.contrib import admin
from django.urls import path, include
from crm.views.auth import CustomTokenObtainPairView, register_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crm.urls')),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', register_user, name='register_user'),
]

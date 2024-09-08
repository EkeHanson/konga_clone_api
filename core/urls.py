from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenVerifyView,TokenRefreshView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', include('order.urls')),

     path('api/recharge/', include('recharge.urls')),  # Include the recharge URLs
     path('api/payment/', include('payment.urls')),
     path('api/withdraw/', include('withdraw.urls')),

    path('api/accounts/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

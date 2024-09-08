from rest_framework.routers import DefaultRouter
from .views import BankDetailViewSet

router = DefaultRouter()
router.register(r'bank-details', BankDetailViewSet)

urlpatterns = router.urls

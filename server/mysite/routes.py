from recongnition.views import PlantaView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'plantas', PlantaView)


urlpatterns = router.urls


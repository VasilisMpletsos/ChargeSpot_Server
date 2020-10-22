from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'history', views.ChargeHistoryViewSet)
router.register(r'charge_spots', views.ChargeSpotViewSet)
router.register(r'processor_points', views.ProcessorPointViewSet)
router.register(r'management', views.ManagementrViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PatientViewSet, DoctorViewSet, NurseViewSet, 
    AppointmentViewSet, MedicalRecordViewSet, DepartmentViewSet,
    register_user, get_current_user
)

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('nurses', NurseViewSet)
router.register('appointments', AppointmentViewSet)
router.register('records', MedicalRecordViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [
  
    path('auth/register/', register_user, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', get_current_user, name='user_me'),
    path('', include(router.urls)),
]
    
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Patient, Doctor, Nurse, Appointment, MedicalRecord, Department, User
from .serializers import (
    PatientSerializer, DoctorSerializer, NurseSerializer,
    AppointmentSerializer, MedicalRecordSerializer, DepartmentSerializer,
    UserSerializer, UserRegistrationSerializer
)
from .permissions import IsAdmin, IsDoctor, IsNurse

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    """Get the current user details"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsDoctor])
    def confirm(self, request, pk=None):
        """Allow a doctor to confirm an appointment"""
        try:
            appointment = self.get_object()
            
            # Check if the doctor is assigned to this appointment
            try:
                doctor = Doctor.objects.get(user=request.user)
                if appointment.doctor != doctor and not (request.user.is_superuser or request.user.role == 'admin'):
                    return Response(
                        {"detail": "You can only confirm your own appointments unless you're an admin."}, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            except Doctor.DoesNotExist:
                if not (request.user.is_superuser or request.user.role == 'admin'):
                    return Response(
                        {"detail": "Only doctors and admins can confirm appointments."}, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            
            # Check if the appointment is already confirmed or cancelled
            if appointment.status == 'confirmed':
                return Response(
                    {"detail": "This appointment is already confirmed."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif appointment.status == 'cancelled':
                return Response(
                    {"detail": "Cannot confirm a cancelled appointment."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update the appointment status
            appointment.status = 'confirmed'
            appointment.save()
            serializer = self.get_serializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"detail": f"Error confirming appointment: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsDoctor])
    def cancel(self, request, pk=None):
        """Allow a doctor to cancel an appointment"""
        try:
            appointment = self.get_object()
            
            # Check if the doctor is assigned to this appointment
            try:
                doctor = Doctor.objects.get(user=request.user)
                if appointment.doctor != doctor and not (request.user.is_superuser or request.user.role == 'admin'):
                    return Response(
                        {"detail": "You can only cancel your own appointments unless you're an admin."}, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            except Doctor.DoesNotExist:
                if not (request.user.is_superuser or request.user.role == 'admin'):
                    return Response(
                        {"detail": "Only doctors and admins can cancel appointments."}, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            
            # Check if the appointment is already cancelled
            if appointment.status == 'cancelled':
                return Response(
                    {"detail": "This appointment is already cancelled."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update the appointment status
            appointment.status = 'cancelled'
            appointment.save()
            serializer = self.get_serializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"detail": f"Error cancelling appointment: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

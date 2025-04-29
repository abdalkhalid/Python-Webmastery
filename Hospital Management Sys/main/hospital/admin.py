from django.contrib import admin
from .models import User, Patient, Doctor, Nurse, Appointment, MedicalRecord, Department


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role') 
    search_fields = ('username', 'email')  
    list_filter = ('role',)  

admin.site.register(User, UserAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'medical_history')
    search_fields = ('name',)

admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')
    search_fields = ('user__username', 'user__email')

admin.site.register(Doctor, DoctorAdmin)

class NurseAdmin(admin.ModelAdmin):
    list_display = ('user', 'shift')
    search_fields = ('user__username', 'user__email')

admin.site.register(Nurse, NurseAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'status')
    list_filter = ('status', 'doctor', 'date')  
    search_fields = ('patient__name', 'doctor__user__username', 'status')

admin.site.register(Appointment, AppointmentAdmin)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'file', 'uploaded_at', 'description')
    search_fields = ('patient__name', 'description')

admin.site.register(MedicalRecord, MedicalRecordAdmin)

admin.site.register(Department)

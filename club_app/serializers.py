from rest_framework import serializers
from .models import (
    Attendance, Club, Clubfinance, ClubCategory, 
    ClubMember, Event, Eventproposal, Fundingrequest, 
    Report, Role, Student, Systemlog, Transactiontype, User
)

# --- NHÓM 1: CÂU LẠC BỘ ---
class ClubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCategory
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

# --- NHÓM 2: THÀNH VIÊN & SINH VIÊN ---
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

# --- NHÓM 3: SỰ KIỆN & ĐỀ XUẤT ---
class EventproposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventproposal
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# --- NHÓM 4: TÀI CHÍNH ---
class TransactiontypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactiontype
        fields = '__all__'

class ClubfinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubfinance
        fields = '__all__'

class FundingrequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundingrequest
        fields = '__all__'

# --- NHÓM 5: HỆ THỐNG & NGƯỜI DÙNG ---
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'status', 'role'] # Giấu password cho an toàn

class SystemlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systemlog
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
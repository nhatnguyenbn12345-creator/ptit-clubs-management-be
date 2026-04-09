from rest_framework import viewsets
from .models import *
from .serializers import *

# Cụm API Câu lạc bộ
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClubCategory.objects.all()
    serializer_class = ClubCategorySerializer

# Cụm API Thành viên & Sinh viên
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClubMemberViewSet(viewsets.ModelViewSet):
    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Cụm API Sự kiện & Đề xuất (Sửa tên Model theo models.py)
class EventproposalViewSet(viewsets.ModelViewSet):
    queryset = Eventproposal.objects.all()
    serializer_class = EventproposalSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Cụm API Tài chính (Sửa tên Model theo models.py)
class FundingrequestViewSet(viewsets.ModelViewSet):
    queryset = Fundingrequest.objects.all()
    serializer_class = FundingrequestSerializer

class ClubfinanceViewSet(viewsets.ModelViewSet):
    queryset = Clubfinance.objects.all()
    serializer_class = ClubfinanceSerializer

class TransactiontypeViewSet(viewsets.ModelViewSet):
    queryset = Transactiontype.objects.all()
    serializer_class = TransactiontypeSerializer

# Cụm API Hệ thống & Báo cáo
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SystemlogViewSet(viewsets.ModelViewSet):
    queryset = Systemlog.objects.all()
    serializer_class = SystemlogSerializer
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

# Cụm API Thành viên & Điểm danh
class ClubMemberViewSet(viewsets.ModelViewSet):
    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Cụm API Sự kiện & Tài chính
class EventProposalViewSet(viewsets.ModelViewSet):
    queryset = EventProposal.objects.all()
    serializer_class = EventProposalSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FundingRequestViewSet(viewsets.ModelViewSet):
    queryset = FundingRequest.objects.all()
    serializer_class = FundingRequestSerializer

class ClubFinanceViewSet(viewsets.ModelViewSet):
    queryset = ClubFinance.objects.all()
    serializer_class = ClubFinanceSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
from rest_framework import serializers
from .models import (
    Club, ClubCategory, ClubMember, Event, 
    EventProposal, FundingRequest, ClubFinance, 
    Attendance, Report
)

# Serializer cho Câu lạc bộ & Danh mục
class ClubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCategory
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

# Serializer cho Thành viên & Điểm danh
class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

# Serializer cho Sự kiện & Tài chính
class EventProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventProposal
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class FundingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingRequest
        fields = '__all__'

class ClubFinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubFinance
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
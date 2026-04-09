from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# Đăng ký các cụm API
router.register(r'clubs', ClubViewSet)
router.register(r'categories', ClubCategoryViewSet)
router.register(r'members', ClubMemberViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'event-proposals', EventProposalViewSet)
router.register(r'events', EventViewSet)
router.register(r'funding-requests', FundingRequestViewSet)
router.register(r'finances', ClubFinanceViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
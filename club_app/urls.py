from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'categories', ClubCategoryViewSet)
router.register(r'students', StudentViewSet)
router.register(r'members', ClubMemberViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'event-proposals', EventproposalViewSet)
router.register(r'events', EventViewSet)
router.register(r'funding-requests', FundingrequestViewSet)
router.register(r'finances', ClubfinanceViewSet)
router.register(r'transaction-types', TransactiontypeViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'system-logs', SystemlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin

# Import chính xác từng chữ hoa/thường theo đúng file models.py của bạn
from .models import (
    Attendance, 
    Club, 
    Clubfinance, 
    ClubCategory, 
    ClubMember, 
    Event, 
    Eventproposal, 
    Fundingrequest, 
    Report, 
    Role, 
    Student, 
    Systemlog, 
    Transactiontype, 
    User
)
from django.contrib import admin
from .models import Club, ClubCategory

# 1. Tạo một lớp Inline cho bảng Club
class ClubInline(admin.TabularInline):
    model = Club
    extra = 0 # Không hiện sẵn các dòng trống
    fields = ('name', 'status') # Các cột muốn xem nhanh
    readonly_fields = ('name',) # Chỉ cho xem, muốn sửa thì bấm vào Club sau

# 2. Đăng ký bảng ClubCategory với Inline vừa tạo
@admin.register(ClubCategory)
class ClubCategoryAdmin(admin.ModelAdmin):
    inlines = [ClubInline]

# Đăng ký 14 bảng lên giao diện Web
admin.site.register(Attendance)
admin.site.register(Club)
admin.site.register(Clubfinance)
admin.site.register(ClubMember)
admin.site.register(Event)
admin.site.register(Eventproposal)
admin.site.register(Fundingrequest)
admin.site.register(Report)
admin.site.register(Role)
admin.site.register(Student)
admin.site.register(Systemlog)
admin.site.register(Transactiontype)
admin.site.register(User)
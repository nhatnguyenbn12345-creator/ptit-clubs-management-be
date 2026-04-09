# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    attendance_id = models.IntegerField(primary_key=True)
    check_in_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attendance'
    def __str__(self):
        return f"Điểm danh ID: {self.attendance_id}"

class Club(models.Model):
    # 1. Khóa chính tự tăng (Bạn đã làm đúng)
    club_id = models.AutoField(primary_key=True) 
    
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    # 3. ĐÂY LÀ DÒNG QUAN TRỌNG NHẤT ĐỂ HẾT LỖI
    # Nó phải khớp với cột 'category_id' trong SSMS của bạn
    category = models.ForeignKey(
        'ClubCategory', 
        models.DO_NOTHING, 
        db_column='category_id', # Tên cột chính xác trong SQL Server
        blank=True, 
        null=True
    )

    class Meta:
        managed = False
        db_table = 'Club'

    def __str__(self):
        return str(self.name)
class Clubfinance(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    transaction_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('Transactiontype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClubFinance'
    def __str__(self):
        return f"Giao dịch {self.transaction_id} - {self.amount} VNĐ"

class ClubCategory(models.Model):
    # Đổi IntegerField thành AutoField
    category_id = models.AutoField(primary_key=True) 
    category_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    
    class Meta:
        managed = False
        db_table = 'Club_Category'

    def __str__(self):
        return self.category_name
class ClubMember(models.Model):
    member_id = models.IntegerField(primary_key=True)
    join_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Club_Member'
    def __str__(self):
        return f"Thành viên ID: {self.member_id}"

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    location = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event'
    def __str__(self):
        return str(self.name)

class Eventproposal(models.Model):
    proposal_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    proposed_time = models.DateTimeField(blank=True, null=True)
    proposed_budget = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    approval_status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EventProposal'
    def __str__(self):
        return str(self.event_name)

class Fundingrequest(models.Model):
    request_id = models.IntegerField(primary_key=True)
    purpose = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    requested_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    approval_status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FundingRequest'
    def __str__(self):
        return f"Yêu cầu {self.request_id} - {self.requested_amount} VNĐ"

class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    report_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    content = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Report'
    def __str__(self):
        return f"Báo cáo {self.report_id} - {self.report_type}"

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Role'
    def __str__(self):
        return str(self.role_name)

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    full_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    faculty = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    academic_year = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Student'
    def __str__(self):
        return str(self.full_name)

class Systemlog(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    entry_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SystemLog'
    def __str__(self):
        return str(self.action)

class Transactiontype(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'TransactionType'
    def __str__(self):
        return str(self.type_name)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'
    def __str__(self):
        
        return self.username

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
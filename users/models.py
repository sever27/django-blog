# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    article_title = models.TextField()
    article_content = models.TextField()
    article_views = models.BigIntegerField()
    article_comment_count = models.BigIntegerField()
    article_date = models.DateTimeField(blank=True, null=True)
    article_like_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'articles'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    article_id = models.BigIntegerField()
    comment_like_count = models.BigIntegerField()
    comment_date = models.DateTimeField(blank=True, null=True)
    comment_content = models.TextField()
    parent_comment_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Labels(models.Model):
    label_id = models.BigAutoField(primary_key=True)
    label_name = models.CharField(max_length=20)
    label_alias = models.CharField(max_length=15)
    label_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'labels'


class SetArtitleLabel(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    label_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'set_artitle_label'


class SetArtitleSort(models.Model):
    article_id = models.BigIntegerField(primary_key=True)
    sort_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'set_artitle_sort'
        unique_together = (('article_id', 'sort_id'),)


class Sorts(models.Model):
    sort_id = models.BigIntegerField(primary_key=True)
    sort_name = models.CharField(max_length=50)
    sort_alias = models.CharField(max_length=15)
    sort_description = models.TextField()
    parent_sort_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sorts'


class UserFriends(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_friends_id = models.BigIntegerField()
    user_note = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_friends'


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_ip = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=15)
    user_email = models.CharField(max_length=30)
    user_profile_photo = models.CharField(max_length=255)
    user_registration_time = models.DateTimeField(blank=True, null=True)
    user_birthday = models.DateField(blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_telephone_number = models.IntegerField()
    user_nickname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
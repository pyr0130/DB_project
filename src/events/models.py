# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Artist(models.Model):
    code = models.TextField(primary_key=True)
    name = models.TextField()
    debut = models.CharField(max_length=4, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_artist'

class Book(models.Model):
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='email', primary_key=True)
    concert = models.ForeignKey('Concert', models.DO_NOTHING, db_column='concert')
    booked_at = models.CharField(max_length=254, blank=True, null=True)
    coin = models.IntegerField(blank=True, null=True)
    section = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_book'
        unique_together = (('email', 'concert'),)

class Concert(models.Model):
    code = models.CharField(primary_key=True, max_length=8)
    name = models.TextField()
    genre = models.CharField(max_length=7, blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    poster = models.CharField(max_length=100, blank=True, null=True)
    hall = models.ForeignKey('Hall', models.DO_NOTHING, blank=True, null=True)
    during = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_concert'

class Fartist(models.Model):
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='email', primary_key=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist')

    class Meta:
        managed = False
        db_table = 'events_fartist'
        unique_together = (('email', 'artist'),)


class Fconcert(models.Model):
    email = models.ForeignKey('User', models.DO_NOTHING, db_column='email', primary_key=True)
    concert = models.ForeignKey(Concert, models.DO_NOTHING, db_column='concert')

    class Meta:
        managed = False
        db_table = 'events_fconcert'
        unique_together = (('email', 'concert'),)


class Hall(models.Model):
    code = models.CharField(primary_key=True, max_length=8)
    contact = models.CharField(max_length=13, blank=True, null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    si = models.TextField(blank=True, null=True)
    gu = models.TextField(blank=True, null=True)
    dong = models.TextField(blank=True, null=True)
    ro = models.TextField(blank=True, null=True)
    gibun = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'events_hall'


class Member(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist', primary_key=True)
    member = models.TextField()

    class Meta:
        managed = False
        db_table = 'events_member'
        unique_together = (('artist', 'member'),)


class Perform(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artist', primary_key=True)
    concert = models.ForeignKey(Concert, models.DO_NOTHING, db_column='concert')

    class Meta:
        managed = False
        db_table = 'events_perform'
        unique_together = (('artist', 'concert'),)


class Schedule(models.Model):
    concert = models.ForeignKey(Concert, models.DO_NOTHING, db_column='concert', primary_key=True)
    date = models.DateField()
    time = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_schedule'
        unique_together = (('concert', 'date'),)


class Seat(models.Model):
    concert = models.ForeignKey(Concert, models.DO_NOTHING, db_column='concert', primary_key=True)
    section = models.TextField()
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events_seat'
        unique_together = (('concert', 'section', 'number'),)



class Sponsor(models.Model):
    code = models.CharField(primary_key=True, max_length=7)
    name = models.TextField()
    homepage = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_sponsor'


class Ticket(models.Model):
    concert = models.ForeignKey(Concert, models.DO_NOTHING, db_column='concert', primary_key=True)
    rating = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events_ticket'
        unique_together = (('concert', 'rating'),)


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=254)
    password = models.CharField(max_length=12)
    name = models.TextField()
    sex = models.CharField(max_length=2)
    contact = models.CharField(max_length=13)
    birth = models.DateField()
    coin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events_user'

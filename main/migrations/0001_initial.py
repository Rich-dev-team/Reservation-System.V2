# Generated by Django 2.2.6 on 2020-01-15 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.UUIDField(default=uuid.UUID('743c2bbb-f36d-48b7-a319-64f75c3f7a30'), primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('staff_name', models.CharField(max_length=45)),
                ('staff_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('staff_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'staff___db',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_id', models.UUIDField(default=uuid.UUID('582b3b85-ec07-466c-8507-a48f4ee8a99e'), primary_key=True, serialize=False)),
                ('social_id', models.CharField(blank=True, max_length=45, null=True)),
                ('social_app', models.CharField(blank=True, max_length=45, null=True)),
                ('social_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'acc___db',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.UUIDField(default=uuid.UUID('2e32a274-1745-441b-8b4a-16adb3c1ab12'), primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=45, unique=True)),
                ('store_address', models.CharField(max_length=45)),
                ('store_phone', models.CharField(max_length=20)),
                ('store_fax', models.CharField(blank=True, max_length=20, null=True)),
                ('tk_service', models.BooleanField(default=False)),
                ('seat', models.PositiveIntegerField()),
                ('store_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'store___db',
            },
        ),
        migrations.CreateModel(
            name='UserActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('ip_address', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Account')),
            ],
            options={
                'db_table': 'user__action_log___db',
            },
        ),
        migrations.CreateModel(
            name='StoreEvent',
            fields=[
                ('event_id', models.UUIDField(default=uuid.UUID('de627633-e6f7-4ebc-bd65-d00f706655c6'), primary_key=True, serialize=False)),
                ('event_type', models.CharField(max_length=45)),
                ('event_date', models.DateField()),
                ('time_session', models.CharField(max_length=45)),
                ('event_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store')),
            ],
            options={
                'db_table': 'store_event___db',
            },
        ),
        migrations.CreateModel(
            name='StaffActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=300)),
                ('ip_address', models.CharField(max_length=200)),
                ('operation', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'staff_action_log___db',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('prod_id', models.UUIDField(default=uuid.UUID('ef9cbc2d-3ea6-4d91-a097-f73ecfb6ca3b'), primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=45)),
                ('prod_price', models.PositiveIntegerField()),
                ('prod_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store')),
            ],
            options={
                'db_table': 'prod___db',
            },
        ),
        migrations.CreateModel(
            name='BkList',
            fields=[
                ('bk_uuid', models.UUIDField(default=uuid.UUID('6dfc33af-09c1-49f0-b866-65bc36603f7b'), primary_key=True, serialize=False)),
                ('bk_date', models.DateField()),
                ('time_session', models.CharField(max_length=10)),
                ('bk_st', models.TimeField()),
                ('wh_bk', models.DateTimeField(blank=True, null=True)),
                ('adult', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('bk_ps', models.CharField(blank=True, max_length=200, null=True)),
                ('bk_habit', models.CharField(blank=True, max_length=200, null=True)),
                ('event_type', models.CharField(blank=True, max_length=20, null=True)),
                ('is_cancel', models.BooleanField(default=False)),
                ('waiting_num', models.PositiveIntegerField()),
                ('entire_time', models.BooleanField(default=False)),
                ('bk_price', models.PositiveIntegerField()),
                ('is_confirm', models.BooleanField(default=False)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Store')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Account')),
            ],
            options={
                'db_table': 'bk_list___db',
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store'),
        ),
        migrations.AddField(
            model_name='staff',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

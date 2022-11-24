# Generated by Django 4.1.3 on 2022-11-24 14:48

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.TextField()),
                ('first_name', models.TextField()),
                ('other_names', models.TextField(blank=True, null=True)),
                ('course', models.TextField()),
                ('class_field', models.TextField(db_column='class')),
                ('index_number', models.TextField(unique=True)),
                ('electives', models.TextField()),
                ('gender', models.IntegerField()),
                ('parent_contact', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.TextField()),
                ('signature', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('fingerprint', models.TextField(blank=True, null=True)),
                ('bece_year', models.IntegerField()),
                ('student_key', models.CharField(blank=True, max_length=6, null=True)),
                ('personal_contact', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'student_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredSchools',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.TextField()),
                ('location', models.TextField()),
                ('country', models.TextField()),
                ('school_code', models.TextField(blank=True, null=True)),
                ('school_logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='School Logo')),
                ('school_email', models.TextField()),
                ('password', models.TextField()),
                ('verified', models.IntegerField()),
            ],
            options={
                'db_table': 'registered_schools',
            },
        ),
        migrations.CreateModel(
            name='RegisteredStudents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wassce_index_number', models.TextField(blank=True, null=True)),
                ('wassce_year', models.IntegerField(blank=True, null=True)),
                ('cleared', models.IntegerField()),
                ('student', models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, to='api.studentdetails')),
            ],
            options={
                'db_table': 'registered_students',
            },
        ),
    ]

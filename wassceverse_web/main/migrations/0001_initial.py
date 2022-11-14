# Generated by Django 4.1.3 on 2022-11-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredSchools',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.TextField()),
                ('location', models.TextField()),
                ('country', models.TextField()),
                ('school_code', models.TextField(blank=True, null=True)),
                ('school_logo', models.TextField()),
                ('school_email', models.TextField()),
                ('password', models.TextField()),
                ('verified', models.IntegerField()),
            ],
            options={
                'db_table': 'registered_schools',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredStudents',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('wassce_index_number', models.TextField(blank=True, null=True)),
                ('wassce_year', models.IntegerField(blank=True, null=True)),
                ('cleared', models.IntegerField()),
            ],
            options={
                'db_table': 'registered_students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.TextField()),
                ('first_name', models.TextField()),
                ('other_names', models.TextField(blank=True, null=True)),
                ('course', models.TextField()),
                ('class_field', models.TextField(db_column='class')),
                ('index_number', models.TextField()),
                ('electives', models.TextField()),
                ('gender', models.IntegerField()),
                ('parent_contact', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.TextField()),
                ('signature', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('fingerprint', models.TextField(blank=True, null=True)),
                ('bece_year', models.IntegerField()),
                ('student_key', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'student_details',
                'managed': False,
            },
        ),
    ]

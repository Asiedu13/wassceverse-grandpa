# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RegisteredSchools(models.Model):
    school_name = models.TextField()
    location = models.TextField()
    country = models.TextField()
    school_code = models.TextField(blank=True, null=True)
    school_logo = models.TextField()
    school_email = models.TextField()
    password = models.TextField()
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registered_schools'


class RegisteredStudents(models.Model):
    student = models.ForeignKey('StudentDetails', models.DO_NOTHING, db_column='student')
    wassce_index_number = models.TextField(blank=True, null=True)
    wassce_year = models.IntegerField(blank=True, null=True)
    cleared = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registered_students'


class StudentDetails(models.Model):
    school = models.ForeignKey(RegisteredSchools, models.DO_NOTHING, db_column='school')
    surname = models.TextField()
    first_name = models.TextField()
    other_names = models.TextField(blank=True, null=True)
    course = models.TextField()
    class_field = models.TextField(db_column='class')  # Field renamed because it was a Python reserved word.
    index_number = models.TextField()
    electives = models.TextField()
    gender = models.IntegerField()
    parent_contact = models.TextField(blank=True, null=True)
    date_of_birth = models.TextField()
    signature = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    fingerprint = models.TextField(blank=True, null=True)
    bece_year = models.IntegerField()
    student_key = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_details'

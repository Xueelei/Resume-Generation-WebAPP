from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Position(models.Model):
    text = models.CharField(max_length=500, default=None)

class Location(models.Model):
    text = models.CharField(max_length=500, default=None)

class Resume(models.Model):
    user            = models.ForeignKey(User, on_delete=models.PROTECT, related_name="resume_user")
    file            = models.FileField(blank=False)
    picture         = models.FileField(blank=False)
    master          = models.BooleanField(default=False)  

class Bio(models.Model):
    user            = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bio_user")
    education_level = models.CharField(max_length=500, default=None, blank=True)
    job_type        = models.CharField(max_length=500, default=None, blank=True)
    positions       = models.ManyToManyField(Position, related_name='positions', symmetrical=False)
    locations       = models.ManyToManyField(Location, related_name='locations', symmetrical=False)
    resume_list     = models.ManyToManyField(Resume, related_name="resume", blank=True)

class Detail(models.Model):
    text = models.CharField(max_length=500, default=None)

class Education(models.Model):
    school_name     = models.CharField(max_length=500, default=None)
    education_level = models.CharField(max_length=500, default=None)
    major           = models.CharField(max_length=500, default=None)
    start_time      = models.CharField(max_length=500, default=None)
    end_time        = models.CharField(max_length=500, default=None)

class Experience(models.Model):
    job_title       = models.CharField(max_length=500, default=None)
    job_type        = models.CharField(max_length=500, default=None)
    company_name    = models.CharField(max_length=500, default=None)
    company_address = models.CharField(max_length=500, default=None)
    start_time      = models.CharField(max_length=500, default=None)
    end_time        = models.CharField(max_length=500, default=None)
    details         = models.ManyToManyField(Detail, related_name='exp_details', symmetrical=False)

class Project(models.Model):
    project_title     = models.CharField(max_length=500, default=None)
    organization_name = models.CharField(max_length=500, default=None)
    start_time        = models.CharField(max_length=500, default=None)
    end_time          = models.CharField(max_length=500, default=None)
    details           = models.ManyToManyField(Detail, related_name='prj_details', symmetrical=False)

class Profile(models.Model):
    user         = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user", default=None)
    phone_number = models.CharField(max_length=500, blank=True)
    email        = models.CharField(max_length=500, default=None)
    educations   = models.ManyToManyField(Education, related_name='educations', symmetrical=False)
    experiences  = models.ManyToManyField(Experience, related_name='experiences', symmetrical=False)
    projects     = models.ManyToManyField(Project, related_name='projects', symmetrical=False)
    skills       = models.ManyToManyField(Detail, related_name='skills', symmetrical=False)

class EmployerBio(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="EmBio_user")
    er_position = models.CharField(max_length=500, blank=True)
    er_location = models.CharField(max_length=500, blank=True)
    education = models.CharField(max_length=500, blank=True)
    link_resume = models.ManyToManyField(Resume, blank=True, related_name="Bio_link_resume")
    company = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    message = models.CharField(max_length=1000000, blank=True)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="employee_user")
    bio_list = models.ManyToManyField(Bio, related_name="bio", blank=True)

class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="employer_user")
    bio = models.ForeignKey(EmployerBio, on_delete=models.PROTECT, related_name="employer_bio",blank=True)
    contact_list = models.ManyToManyField(Employee, related_name='contact', blank=True)
from django.db import models
from django.core.validators import RegexValidator

from student_register_app.college_API import *

gender_choice = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]
mob_regex = RegexValidator(regex=r'^\d{10}$', message="Enter a valid 10-digit mobile number") #mobile number limiter
# Basic Registration detail for every one
class Register(models.Model):

    name = models.CharField('Full Name', max_length=100)
    user_name = models.CharField('User Name', max_length=20, unique=True)
    occupation = models.TextField('Occupation', max_length=100)
    phone_number = models.IntegerField('Phone Number', validators=[mob_regex] , unique=True)
    email_id = models.EmailField('Email',unique=True)
    gender = models.CharField(max_length=10, choices=gender_choice, default='Select', blank=True, null=True)
    dob = models.DateField('Date of Birth')
    

    def __str__(self):
        return self.name
    


# collage API

class State(models.Model):
    state_name  = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['state_name']

    def __str__(self):
        return self.state_name
    
class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='district')
    district_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('state', 'district_name')
        ordering = ['district_name']

    def __str__(self):
        return self.district_name
    
class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='cities')
    city_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('district','city_name')
        ordering = ['city_name']

    def __str__(self):
        return self.city_name
    
class College(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='college')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='college')
    city = models.ForeignKey(City,on_delete=models.CASCADE, related_name='college')

    college_name = models.CharField(max_length=200)

    class Meta:
        unique_together = ('city','college_name')
        ordering = ['college_name']

    def __str__(self):
        return self.college_name
    

# Student Registration form

class StudentRegistration(models.Model):

    selected_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='student_registration')
    selected_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="student_registration")
    selected_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='student_registration')
    selected_college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='student_registration')
    
    college_semester = models.CharField('College Semester', max_length=50)

    subject = models.CharField('Subject you want learn', max_length=50)
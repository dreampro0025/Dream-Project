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
    phone_number = models.IntegerField('Phone Number', max_length=10, validators=[mob_regex] , unique=True)
    email_id = models.EmailField('Email',unique=True)
    gender = models.CharField(max_length=10, choices=gender_choice, default='Select')
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
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='district_list')
    district_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('state', 'district_name')
        ordering = ['district_name']

    def __str__(self):
        return self.district_name
    
class College(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='college_list')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='college_list')

    college_name = models.CharField(max_length=200)

    class Meta:
        unique_together = ('district','college_name')
        ordering = ['college_name']

    def __str__(self):
        return self.college_name
    

# Student Registration form

class StudentRegistration(models.Model):

    selected_state = models.ForeignKey("State",State, on_delete=models.CASCADE, related_name='student_reg')
    selected_district = models.ForeignKey("District",District, on_delete=models.CASCADE, related_name="student_reg")
    selected_college = models.ForeignKey('College Name',College, on_delete=models.CASCADE, related_name='student_reg')
    
    college_year = models.CharField('College Year')

    subject = models.CharField('Subject you want learn')
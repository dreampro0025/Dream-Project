from django.db import models

# Create your models here.

class StrongSubject(models.Model):
    subject = models.CharField("Strong Subject", max_length=30)

    def __str__(self):
        return self.subject
    
class MarkSheet(models.Model):
    mark_sheet = models.FileField('MarkSheet',upload_to='student_markSheet/')

    def __str__(self):
        return self.mark_sheet

class LiveDemo_student(models.Model):
    live_demo_video = models.FileField('Demo Video',upload_to="student_demo_video/")

    def __str__(self):
        return self.live_demo_video

class StudentAsTeach(models.Model):
    strong_subject = models.ManyToManyField(StrongSubject, related_name='student_teach_reg')
    mark_sheet =  models.ManyToManyField(MarkSheet, related_name='student_teach_reg')
    achievement = models.CharField('Achievement', max_length=200,blank=False, null=False)
    profile_picture = models.FileField('Profile Picture', upload_to='profile_picture/',blank=True, null=True)
    demo_video = models.ManyToManyField(LiveDemo_student, related_name='student_teach_reg')
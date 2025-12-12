from django.db import models

# Create your models here.

class StrongSubject(models.Model):
    subject = models.TextField("Strong Subject", max_length=30, null=False, blank=False)

    def __str__(self):
        return self.subject
    
class MarkSheet(models.Model):
    mark_sheet = models.FileField('MarkSheet',upload_to='student_markSheet/',null=False, blank=False)

    def __str__(self):
        return self.mark_sheet

class LiveDemo(models.Model):
    live_demo_video = models.FileField('Demo Video',upload_to="student_demo_video/",blank=False, null=False)

    def __str__(self):
        return self.live_demo_video

class StudentAsTeach(models.Model):
    strong_subject = models.ManyToManyField(StrongSubject, on_delete=models.CASCADE, related_name='student_teach_reg')
    mark_sheet =  models.ManyToManyField(MarkSheet, on_delete=models.CASCADE, related_name='student_teach_reg')
    achievement = models.CharField('Achievement',max_length=200,blank=False, null=False)
    profile_picture = models.FileField('Profile Picture')
    demo_video = models.ManyToManyField(LiveDemo, on_delete=models.CASCADE,related_name='student_teach_reg')
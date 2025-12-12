from django.db import models
from student_register_app.models import*

# Certification File
class Certification(models.Model):
    certificate = models.FileField(upload_to="certifications/", blank=False, null=False)

    def __str__(self):
        return str(self.certificate)


# Strong Subject File
class TeachingSubject(models.Model):
    subject_to_teach = models.FileField(upload_to="teaching_subjects/", blank=False, null=False)

    def __str__(self):
        return str(self.subject_to_teach)


# Live Demo Video
class LiveDemo(models.Model):
    live_demo_video = models.FileField(upload_to="live_demos/", blank=False, null=False)

    def __str__(self):
        return str(self.live_demo_video)

class ProfessionalTeachReg(models.Model):
    
    selected_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='prof_tech')
    selected_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="prof_tech")
    selected_college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='prof_tech')
    experience = models.CharField( max_length=150,blank=False, null=False)
    certification = models.ManyToManyField(Certification,on_delete=models.CASCADE, related_name='prof_tech')
    subject_to_teach = models.ManyToManyField(TeachingSubject,on_delete= models.CASCADE,related_name='prof_tech')
    live_demo = models.ManyToManyField(LiveDemo,on_delete=models.CASCADE, related_name='prof_tech')
    profile_picture = models.FieldFile('Profile Picture', upload_to = 'prof_teach_profile/')
    achievement = models.CharField('Achievement',max_length=200)

    
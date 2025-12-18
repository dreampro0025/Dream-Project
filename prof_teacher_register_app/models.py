from django.db import models
from student_register_app.models import*

# Certification File
class Certification(models.Model):
    certificate = models.FileField(upload_to="certifications/", blank=False, null=False)
    certification_name = models.TextField('Certification Name', max_length=50)

    def __str__(self):
        return self.certificate.name


# Strong Subject File
class TeachingSubject(models.Model):
    subject_to_teach = models.TextField('Subject To Teach',max_length=50)

    def __str__(self):
        return self.subject_to_teach


# Live Demo Video
class LiveDemo_teacher(models.Model):
    live_demo_video = models.FileField(upload_to="live_demos_teacher/")

    def __str__(self):
        return self.live_demo_video.name

class ProfessionalTeachReg(models.Model):
    
    selected_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='professional_teacher')
    selected_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="professional_teacher")
    selected_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='professional_teacher')
    selected_college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='professional_teacher')
    experience = models.CharField('Experience', max_length=150)
    certification = models.ManyToManyField(Certification,  related_name='professional_teacher')
    subject_to_teach = models.ManyToManyField(TeachingSubject, related_name='professional_teacher')
    live_demo = models.ManyToManyField(LiveDemo_teacher, related_name='professional_teacher')
    profile_picture = models.FileField('Profile Picture', upload_to = 'prof_teach_profile/',blank = True,null=True)
    achievement = models.CharField('Achievement',max_length=200)

    def __str__(self):
        return f"professional Teacher #{self.id}"

    
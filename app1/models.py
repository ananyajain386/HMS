from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#     email = models.EmailField(_('email address'), unique = True)
#     native_name = models.CharField(max_length = 5)
#     phone_no = models.CharField(max_length = 10)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
class departments(models.Model):
    department=models.CharField(max_length=150,null=True)
    class Meta:
        db_table = "Departments" 
class doctorsh(models.Model):
     doctor=models.ForeignKey(User,on_delete=models.CASCADE)
     depart=models.ForeignKey(departments,on_delete=models.CASCADE,null=True)
     department=models.CharField(max_length=20,null=True)
     fees=models.IntegerField(null=True)
     morningtime= models.TimeField(null=True)
     eveningtime= models.TimeField(null=True)
     shifts=models.IntegerField(null=True)
     experience=models.IntegerField(null=True)
     Img = models.ImageField(upload_to='Pictures/',blank=True)
     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
     class Meta:
        db_table = "Doctor"
class patientsh(models.Model):
     patient=models.ForeignKey(User,on_delete=models.CASCADE)
     # doctor=models.ForeignKey(doctorsh,on_delete=models.CASCADE,null=True)
     age=models.IntegerField(blank=True)
    #  mention your age
     yourgender=models.CharField(max_length=10,blank=True)
    #  What is your gender
     illness=models.CharField(max_length=30,blank=True)
    #  Do you have any previous major illness
     medicineshist=models.CharField(max_length=100,blank=True)
    #  are you currently taking any medicine
     familyhistory=models.CharField(max_length=30,blank=True)
    #  mention any major illness of any of your immediate relatives
     allergies=models.CharField(max_length=30,blank=True)
    #  Do you have any medication allergies
     tobacco=models.CharField(max_length=30,blank=True)
    #  Do you use or do you have history of using tobacco?
     drugs=models.CharField(max_length=30,blank=True)
    #  Do you use or do you have history of using illegal drugs?
     diabetic=models.CharField(max_length=30,blank=True)
    #  are you diabetic
     alcohol=models.CharField(max_length=30,blank=True)
    #  How often do you consume alcohol?
     # doctorgh=models.ForeignKey(doctor,on_delete=models.CASCADE)
     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
     phone_number = models.CharField(validators=[phone_regex], max_length=17,blank=True) # Validators should be a list
     class Meta:
        db_table = "Patient"
class appointmentsh(models.Model):
    patient= models.ForeignKey(patientsh,on_delete=models.CASCADE,null=True)
    patient2=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    doctor=models.ForeignKey(doctorsh,on_delete=models.CASCADE)
    doctorname=models.CharField(max_length=30,null=True)
    date=models.DateField()
    start_time= models.TimeField(null=True)
    end_time= models.TimeField(null=True)
    recaprvd=models.BooleanField(null=True,default=False)
    docaprvd=models.BooleanField(null=True,default=False)
    removed=models.BooleanField(default=False)
    rec_reason=models.CharField(max_length=150,blank=True)
    doc_reason=models.CharField(max_length=150,blank=True)
    class Meta:
        db_table = "Appointments" 
class payment(models.Model): 
    patient=models.ForeignKey(patientsh,on_delete=models.CASCADE)
    appt=models.ForeignKey(appointmentsh,on_delete=models.CASCADE)
    payment=models.IntegerField(null=True)
    refund=models.BooleanField(default=False)
#   remove or refund 
    class Meta:
        db_table = "Payments" 
class prescriptions(models.Model): 
    patient=models.ForeignKey(patientsh,on_delete=models.CASCADE,null=True)
    appt=models.ForeignKey(appointmentsh,on_delete=models.CASCADE)
    prescription=models.CharField(max_length=150,null=True)
    symptoms=models.CharField(max_length=150,null=True)
    advice=models.CharField(max_length=150,null=True)
    tests=models.CharField(max_length=150,null=True)
    dosage=models.CharField(max_length=150,null=True)
    duration=models.CharField(max_length=150,null=True)
    takingTime=models.CharField(max_length=150,null=True)
    class Meta:
        db_table = "Prescriptions" 
class roles(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=20,null=True)
    class Meta:
        db_table = "Roles" 
class dynamicpanel(models.Model): 
    rolea=models.ForeignKey(roles,on_delete=models.CASCADE,null=True)
    role1=models.CharField(max_length=20,null=True)
    text1=models.CharField(max_length=150,null=True)
    text_link=models.CharField(max_length=150,null=True)
    removed=models.BooleanField(default=False,null=True)
    order1=models.IntegerField(null=True)
    icon=models.FileField(blank=True)
    class Meta:
        db_table = "Dynamic_Panel"      

import json
import random
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as dj_login
from app1.models import patientsh,doctorsh,appointmentsh,payment,prescriptions,departments,roles,dynamicpanel
import datetime
from django.views.generic import View
# import django_renderpdf import pdf_view
from django_renderpdf import helpers
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import get_template
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import Context, Template
from django.contrib.auth.models import AbstractUser
from weasyprint import default_url_fetcher
# import django_url_fetcher


def logout1(request):
   logout(request)      
   return JsonResponse({'message':'Logged out successfully'})
def patientregister(request):
    if request.method=='POST': 
      db=json.loads(request.body)
      username=db['username']
      password=db['password']
      confirmpassword=db['confirmpassword']
      email=db['email']
      print(email)
      first_name=db['firstname']
      last_name=db['lastname']
      # gender=db['gender']
      age=db['age'] 
      phone=db['phone'] 
      # if gender==""or illness==""or medicineshist==""or familyhistory==""or allergies==""or tobacco==""or drugs==""or diabetic==""or alcohol=="":
      #    xm
      if password!=confirmpassword:
           return JsonResponse({'message':'Password does not match'},status=400) 
      elif User.objects.filter(username=username).exists():
         return JsonResponse({'message':'Username already registered'},status=400) 
      elif User.objects.filter(email=email).exists():
         return JsonResponse({'message':'Email already registered'},status=400) 
      else:  
           user = User.objects.create_user(username,email,confirmpassword) 
           user.first_name =first_name
           user.last_name =last_name 
           user.save()
           r=User.objects.get(username=username).pk
           p=patientsh(patient_id=r,age=age,phone_number=phone)
           p.save()
           rl=roles(role='patient',user_id=r)
           rl.save()
           return JsonResponse({'message':'Successfully registered'})
def doctorregister(request):
    if request.method=='POST':
      #  db=json.loads(request.body)
       username=request.POST.get('username')
       password=request.POST.get('password')
       confirmpassword=request.POST.get('confirmpassword')
       email=request.POST.get('email')
       first_name=request.POST.get('firstname')
       last_name=request.POST.get('lastname')
       department_id=request.POST.get('id')
       print(department_id)
       dep=departments.objects.get(id=department_id)
       dep1=dep.department
       fees=request.POST.get('fees')
      #  a=request.POST.get('a')  
      #  b=request.POST.get('b') 
      #  d1 = datetime.time(a,b)
      #  c=request.POST.get('c')
      #  d=request.POST.get('d') 
      # d2 = datetime.time(c,d)
       a=request.POST.get('a')  
       b=request.POST.get('b')
       shifts=request.POST.get('shifts')
       experience=request.POST.get('experience')
       phone=request.POST.get('phone')
       file = request.FILES.get('sectionImage')
       if password!=confirmpassword:
            return JsonResponse({'message':'Password does not match'},status=400) 
       elif User.objects.filter(username=username).exists():
          return JsonResponse({'message':'Username already registered'},status=400) 
       elif User.objects.filter(email=email).exists():
          return JsonResponse({'message':'Email already registered'},status=400) 
       else:  
            user = User.objects.create_user(username=username,email=email,password=password) 
            user.first_name =first_name
            user.last_name =last_name
            user.is_superuser = True
            user.save() 
            r=User.objects.get(username=username).pk
            d=doctorsh(doctor_id=r,department=dep1,fees=fees,morningtime=a,eveningtime=b,experience=experience,Img=file,shifts=shifts,phone_number=phone,depart_id=department_id)
            rl=roles(role='doctor',user_id=r)
            rl.save()
            response=JsonResponse({'message':'Successfully registered'},status=200)
            return response
    if request.method=='GET':
       depart=departments.objects.all()
       data= [{'id': x.id,'department': x.department} for x in depart]
       return JsonResponse(data,safe=False)
def login1(request):  
    if request.method=='POST': 
       db=json.loads(request.body)
       username=db['username']
       password=db['password']
       user = authenticate(request,username=username,password=password)
       if user is not None:
         superuser=user.is_superuser    
         dj_login(request,user)  
         if superuser==True: 
          return JsonResponse({'message':'Doctor'},status=200)
         elif user.is_staff==True:
          return JsonResponse({'message':'receptionist'},status=200)
         else:
          return JsonResponse({'message':'Patient'},status=200)
       else:
         return JsonResponse({'message':'Invalid login'},status=400) 
def patientdashboard1(request):
    if request.user.is_authenticated:
      if request.method=='GET':
         depart=departments.objects.all()
         data2 = [{'id': x.id,'department': x.department} for x in depart]
         return JsonResponse(data2,safe=False)
def patientdashboard2(request):
    if request.user.is_authenticated:
      if request.method=='GET':
         user=request.user.id
         # db=json.loads(request.body)
         # department=request.POST.get('department')
         # print(department)
         data1=doctorsh.objects.filter()
         data2 = [{'department': x.department,'first_name': x.doctor.first_name,'last_name': x.doctor.last_name,'fees': x.fees,'image': x.Img.url,'morningtime': x.morningtime,'eveningtime': x.eveningtime,'experience':x.experience} for x in data1]
         return JsonResponse(data2,safe=False)
         # data1=doctor.objects.filter(department=department)
         # for object in data1:
         #   id=object.id 
         #   data2=appointments.objects.get(doctor_id=id) 
         #   object.save()
         # data2=appointments.objects.filter(doctor_id=8) 
# def patientdashboard2(request):
#     if request.user.is_authenticated:
#       if request.method=='GET':
#          user=request.user.id
#          # db=json.loads(request.body)
#          # department=request.POST.get('department')
#          # print(department)
#          data1=doctorsh.objects.filter().values('department','doctor.first_name','doctor_last_name','fees','Img.url','morningtime','eveningtime','experience')
#          data2 =list(data1)
#          return JsonResponse(data2,safe=False)
#          # data1=doctor.objects.filter(department=department)
#          # for object in data1:
#          #   id=object.id 
#          #   data2=appointments.objects.get(doctor_id=id) 
#          #   object.save()
#          # data2=appointments.objects.filter(doctor_id=8) 
def patientdashboard3(request):
    if request.user.is_authenticated:
      if request.method=='GET':
         user=request.user.id
         doc=appointmentsh.objects.filter(patient2_id=user,removed=False,recaprvd=True,docaprvd=True)
         data3 = [{'id':x.id,'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'gender':x.patient.yourgender,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'doctorfirst_name':x.doctor.doctor.first_name,'doctorlast_name':x.doctor.doctor.last_name,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd} for x in doc]
         return JsonResponse(data3,safe=False,status=200)
def patientdashboard4(request):
    if request.user.is_authenticated:
      if request.method=='GET':
         user=request.user.id
         doc=appointmentsh.objects.filter(patient2_id=user,removed=False,recaprvd=False,docaprvd=False)
         data3 = [{'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'gender':x.patient.yourgender,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'doctorfirst_name':x.doctor.doctor.first_name,'doctorlast_name':x.doctor.doctor.last_name,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd} for x in doc]
         return JsonResponse(data3,safe=False,status=200)
def departmentwisedoc(request):
    if request.method=='GET':
       id=request.GET.get('id')
       print(id)
       depart=doctorsh.objects.filter(depart_id=id)
       data2 = [{'department': x.department,'first_name': x.doctor.first_name,'last_name': x.doctor.last_name,'fees': x.fees,'image': x.Img.url,'morningtime': x.morningtime,'eveningtime': x.eveningtime,'experience':x.experience} for x in depart]
       return JsonResponse(data2,safe=False,status=200)
def medicalhistory(request):
   #   if request.user.is_authenticated:    
      if request.method=='POST':  
       user=request.user
       db=json.loads(request.body)
       gender=db['gender']
       illness=db['illness']
       medicineshist=db['medicineshist']
       familyhistory=db['familyhistory']
       allergies=db['allergies']
       tobacco=db['tobacco']
       drugs=db['drugs']
       diabetic=db['diabetic']
       alcohol=db['alcohol']
       if gender==""or illness==""or medicineshist==""or familyhistory==""or allergies==""or tobacco==""or drugs==""or diabetic==""or alcohol=="":
          return JsonResponse(status=400)
       else: 
         r=patientsh.objects.filter(patient_id=user)
         for x in r:
          if gender is not None:
           x.yourgender=gender
           x.save()
          if illness is not None:
           x.illness=illness
           x.save()
          if medicineshist is not None:
           x.medicineshist=medicineshist
           x.save()
          if familyhistory is not None:
           x.familyhistory=familyhistory
           x.save()
          if allergies is not None:
           x.allergies=allergies
           x.save()
          if tobacco is not None:          
           x.tobacco=tobacco
           x.save()
          if drugs is not None: 
           x.drugs=drugs
           x.save()
          if diabetic is not None:  
           x.diabetic=diabetic
           x.save()
          if alcohol is not None: 
           x.alcohol=alcohol
           x.save()
          else:
             return JsonResponse({'message':'Upload all details'},status=400)
         return JsonResponse({'message':'Medical history uploaded'},status=200)
      if request.method=='GET':
         user=request.user.id 
         a=patientsh.objects.filter(patient_id=user)
         data = [{'first_name': x.patient.first_name,'last_name': x.patient.last_name,'age': x.age,'gender': x.yourgender,'illness': x.illness,'medicineshist': x.medicineshist,'familyhistory': x.familyhistory,'allergies': x.allergies,'tobacco': x.tobacco,'drugs': x.drugs,'diabetic': x.diabetic,'alcohol': x.alcohol,'phone_number': x.phone_number} for x in a]
         return JsonResponse(data,safe=False,status=200)
   #   else:
   #    return JsonResponse({'message':'Patient'})
def appointment(request):
    if request.user.is_authenticated:       
      if request.method=='POST':  
         user=request.user.id
         # user1=User.objects.get(id=user)
         # print(user)
         db=json.loads(request.body)
         id=db['id']
         date=db['date']
         # shiftno=db['shiftno']
         start_time=db['start_time']
         end_time=db['end_time']         
         # doc1=User.objects.get(username=doctor).pk
         # print(doc1)
         doc7=doctorsh.objects.get(doctor_id=id)
         doc2=doc7.id
         fees=doc7.fees
         # print(doc2)
         doc3=patientsh.objects.get(patient_id=user).pk
         # print(doc2)
         # doc=doc1.
         # p1=patientsh.objects.get(patient_id=user) 
         # p1.doctor_id=doc
         if appointmentsh.objects.filter(start_time=start_time,date=date).exists():
          return JsonResponse({'message':'Slot already booked'},status=400) 
         else:
          appt=appointmentsh.objects.create(patient2_id=user,patient_id=doc3,doctor_id=doc2,date=date,start_time=start_time,end_time=end_time) 
          appt.save()
          id=appt.id
          print(id)
          pay=payment.objects.create(payment=fees,patient_id=doc3,appt_id=id)
          pay.save()
          return JsonResponse({'message':'Slot booked successfully'},status=200)
         #  message = f'Dear {user1.username}, your appointment has been booked successfully.'
         #  email_from = settings.EMAIL_HOST_USER
         #  send_mail( subject, message, email_from, recipient_list )
         #  text_content = "This is an important message."
         #  html_content ="templates/email.html"
         #  msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
         #  msg.attach_alternative(html_content, "text/html")
         #  msg.send()
         #  plaintext = get_template('email.txt')
         #  subject, from_email, to = "Appointment booked successfully", "ananyajain386@gmail.com",'sukritisingh9469@gmail.com'
         #  htmly     = get_template('email.html')
         #  d = ({ 'username': user1.username })
         # #  text_content = plaintext.render(d)
         #  context = {'first_name': user1.first_name ,
         #                    'last_name': user1.last_name ,
         #                    'username': user1.username ,
         #                    'email': user1.email ,
         #                    'start_time': appt.start_time ,
         #                    'end_time': appt.end_time ,
         #                    'doctor_firstname': appt.doctor.doctor.first_name ,
         #                    'doctor_lastname': appt.doctor.doctor.last_name ,
         #                    'date': appt.date }
         #  html_content = htmly.render(d)
         #  text_content = Template.render(context)
         #  msg = EmailMultiAlternatives(subject,text_content,from_email, [to])
         #  msg.attach_alternative(html_content, "text/html")
         #  msg.content_subtype = "html"
         #  msg.send()
         #  message = render_to_string('email.html',ctx)
         #  msg = EmailMessage('Subject',message,'ananyajain386@gmail.com',['sukritisingh9469@gmail.com'],)
         #  msg.content_subtype ="html"
         #  msg.send()
         #  ctx =           {'first_name': user1.first_name ,
         #                   'last_name': user1.last_name ,
         #                    'username': user1.username ,
         #                    'email': user1.email ,
         #                    'start_time': appt.start_time ,
         #                    'end_time': appt.end_time ,
         #                    'doctor_firstname': appt.doctor.doctor.first_name ,
         #                    'doctor_lastname': appt.doctor.doctor.last_name ,
         #                    'doctor_department': appt.doctor.department ,
         #                    'date': appt.date }
         #  email_content = render_to_string('email.html', ctx)
         #  subject = 'Appointment Approved'
         #  from_email = 'ananyajain386@gmail.com'
         #  recipient_list = [user1.email]
         #  send_mail(subject, 'Appointment Approved', from_email, recipient_list, html_message=email_content)
    if request.method=='GET':
       depart=departments.objects.all()
       data= [{'id': x.id,'department': x.department} for x in depart]
       return JsonResponse(data,safe=False,status=200)   
def appointment1(request):
    if request.method=='GET':
       id=request.GET.get('departmentid')
       print(id)
       depart=doctorsh.objects.filter(depart_id=id)
       data= [{'first_name':x.doctor.first_name,'last_name':x.doctor.last_name,'id': x.doctor.id} for x in depart]
       return JsonResponse(data,safe=False,status=200)  
def doctordashboard0(request):
    if request.user.is_authenticated:  
      if request.method=='GET':
         user=request.user.id
         data1=doctorsh.objects.filter(doctor_id=user)
         data2 = [{'department': x.department,'first_name': x.doctor.first_name,'last_name': x.doctor.last_name,'fees': x.fees,'morningtime': x.morningtime,'eveningtime': x.eveningtime,'experience':x.experience} for x in data1]
         return JsonResponse(data2,safe=False,status=200)
def doctordashboard(request):
    if request.user.is_authenticated:  
      if request.method=='GET':
         user=request.user.id
         id=doctorsh.objects.get(doctor_id=user).pk
         doc=appointmentsh.objects.filter(doctor_id=id,removed=False,recaprvd=True)
         data = [{'doctor_first_name':x.doctor.doctor.first_name,'patient_last_name':x.doctor.doctor.last_name,'id': x.id,'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'gender':x.patient.yourgender,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'username':x.patient2.username,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd} for x in doc]
         return JsonResponse(data,safe=False,status=200)
def doctordashboard1(request):
    if request.user.is_authenticated:  
      if request.method=='GET':
         user=request.user.id
         id=doctorsh.objects.get(doctor_id=user).pk
         doc=appointmentsh.objects.filter(doctor_id=id,removed=False,recaprvd=True,docaprvd=True)
         data = [{'doctor_first_name':x.doctor.doctor.first_name,'patient_last_name':x.doctor.doctor.last_name,'id': x.id,'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'gender':x.patient.yourgender,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'username':x.patient2.username,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd,'idd':x.patient2.id} for x in doc]
         return JsonResponse(data,safe=False,status=200)
def receptionistdashboard1(request):
     if request.method=='GET':
        depart=departments.objects.all()
        data0 = [{'id': x.id,'department': x.department} for x in depart]
        return JsonResponse(data0,safe=False,status=200)
def receptionistdashboard2(request):
     if request.method=='GET':
        dta1=doctorsh.objects.filter()
        data1 = [{'department': x.department,'fees': x.fees,'image': x.Img.url,'morningtime': x.morningtime,'eveningtime': x.eveningtime,'experience':x.experience} for x in dta1]
        return JsonResponse(data1,safe=False,status=200)
def receptionistdashboard3(request):
     if request.method=='GET':
        doc=appointmentsh.objects.filter(removed=False)
        data2 = [{'id': x.id,'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'gender':x.patient.yourgender,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'doctorfirst_name':x.doctor.doctor.first_name,'doctorlast_name':x.doctor.doctor.last_name,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd} for x in doc]
      #  data=[{'DEPARTMENTS':data0,'DOCTORS':data1,'PATIENTS':data2}]
        return JsonResponse(data2,safe=False,status=200)
def receptionistdashboard4(request):
      if request.method=='GET':
         doc=appointmentsh.objects.filter(removed=False,recaprvd=True,docaprvd=True)
         data = [{'doctor_first_name':x.doctor.doctor.first_name,'patient_last_name':x.doctor.doctor.last_name,'id': x.id,'date': x.date,'start_time': x.start_time,'end_time': x.end_time,'age': x.patient.age,'illness': x.patient.illness,'gender':x.patient.yourgender,'medicineshist':x.patient.medicineshist,'familyhistory':x.patient.familyhistory,'allergies':x.patient.allergies,'tobacco':x.patient.tobacco,'drugs':x.patient.drugs,'diabetic':x.patient.diabetic,'alcohol':x.patient.alcohol,'phone_number':x.patient.phone_number,'first_name':x.patient2.first_name,'last_name':x.patient2.last_name,'username':x.patient2.username,'email':x.patient2.email,'recaprvd':x.recaprvd,'docaprvd':x.docaprvd,'idd':x.patient2.id} for x in doc]
         return JsonResponse(data,safe=False,status=200)
def recaprvd(request): 
     if request.method=='POST':
        db=json.loads(request.body)
        id=db['id']
        r=appointmentsh.objects.filter(id=id,removed=False)
        for x in r:
          x.recaprvd=True
          x.save()
        return JsonResponse({'message':'Appointment approved successfully'},status=200) 
def docaprvd(request):
     if request.method=='POST':
        db=json.loads(request.body)
        id=db['id']
        r=appointmentsh.objects.filter(id=id,removed=False)
        for x in r:
          x.docaprvd=True
          x.save()
        rw=appointmentsh.objects.get(id=id,removed=False) 
        ctx =           {'first_name': rw.patient2.first_name ,
                           'last_name': rw.patient2.last_name ,
                            'username': rw.patient2.username ,
                            'email': rw.patient2.email ,
                            'start_time': rw.start_time ,
                            'end_time': rw.end_time ,
                            'doctor_firstname': rw.doctor.doctor.first_name ,
                            'doctor_lastname': rw.doctor.doctor.last_name ,
                            'doctor_department': rw.doctor.department ,
                            'date': rw.date }
        email_content = render_to_string('email.html', ctx)
        subject = 'Appointment Approved'
        from_email = 'ananyajain386@gmail.com'
        recipient_list = [rw.patient2.email]
        send_mail(subject, 'Appointment Approved', from_email, recipient_list, html_message=email_content)
        return JsonResponse({'message':'Appointment approved successfully'},status=200) 
def delete(request):     
    if request.method=='POST':
        db=json.loads(request.body)
        id=db['id']
      #   reason=db['reason']
        print(id)
        r=appointmentsh.objects.get(id=id,removed=False)
        r.removed=True
      #   r.rec_reason=reason
        r.save()
        refund=payment.objects.get(id=id,appt_id=r.id,refund=False)
        refund.refund=False
        refund.save()
        ctx =           {'first_name': r.patient2.first_name ,
                           'last_name': r.patient2.last_name ,
                            'username': r.patient2.username ,
                            'email': r.patient2.email ,
                            'start_time': r.start_time ,
                            'end_time': r.end_time ,
                            'doctor_firstname': r.doctor.doctor.first_name ,
                            'doctor_lastname': r.doctor.doctor.last_name ,
                            'doctor_department': r.doctor.department ,
                            'date': r.date,
                            'reason':r.rec_reason }
        email_content = render_to_string('rec_email.html', ctx)
        subject = 'Appointment Cancelled'
        from_email = 'ananyajain386@gmail.com'
        recipient_list = [r.patient2.email]
        send_mail(subject, 'Appointment Cancelled', from_email, recipient_list, html_message=email_content)
        return JsonResponse({'message':'Appointment deleted successfully'})
def doc_delete(request):     
    if request.method=='POST':
        db=json.loads(request.body)
        id=db['id']
      #   reason=db['reason']
        print(id)
        r=appointmentsh.objects.get(id=id,removed=False)
      #   r.doc_reason=reason
        r.removed=True
        r.save()
        refund=payment.objects.get(id=id,appt_id=r.id,refund=False)
        refund.refund=False
        refund.save()
        ctx =           {'first_name': r.patient2.first_name ,
                           'last_name': r.patient2.last_name ,
                            'username': r.patient2.username ,
                            'email': r.patient2.email ,
                            'start_time': r.start_time ,
                            'end_time': r.end_time ,
                            'doctor_firstname': r.doctor.doctor.first_name ,
                            'doctor_lastname': r.doctor.doctor.last_name ,
                            'doctor_department': r.doctor.department ,
                            'date': r.date 
                           }
        email_content = render_to_string('doc_email.html', ctx)
        subject = 'Appointment Approved'
        from_email = 'ananyajain386@gmail.com'
        recipient_list = [r.patient2.email]
        send_mail(subject, 'Appointment Approved', from_email, recipient_list, html_message=email_content)
        return JsonResponse({'message':'Appointment deleted successfully'},status=200)
def update(request):
   if request.method=='POST':
      doctor_id=request.POST.get('doctor_id')
      patient_id=request.POST.get('patient_id')
      date=request.POST.get('date')
      start_time=request.POST.get('start_time')
      end_time=request.POST.get('end_time')
      editp=appointmentsh.objects.get(patient_id=patient_id,doctor_id=doctor_id,removed=False)
      if date is not None:
       editp.date=date
      if start_time is not None:
       editp.start_time=start_time
      if end_time is not None:
       editp.end_time=end_time
       editp.save()
      return JsonResponse({'message':'Appointment updated successfully'},status=200) 
# def paymentreciept(request):
#    if request.method=='GET':
#       renderp
def showpaymenthist(request):
    if request.user.is_authenticated:
       if request.method=='GET':
        user=request.user.id
        id=patientsh.objects.get(patient_id=user).pk
        pay=payment.objects.filter(patient_id=id)
        data = [{'payment': x.payment,'illness': x.appt.date,'medicineshist': x.appt.start_time,'familyhistory': x.appt.end_time,'refund': x.refund,} for x in pay]
        return JsonResponse(data,safe=False,status=200)
# def addprescription0(request):
#    if request.method=='POST':
#        db=json.loads(request.body)
#        id=db['id']
#        ppt=prescriptions.objects.create(appt_id=id)
#        ppt.save()
#        return JsonResponse({'message':'success'}) 
def addprescription(request):
   if request.user.is_authenticated:
      if request.method=='POST':
         # # db=json.loads(request.body)
         # db=json.loads(request.body)
         # # id=db['id']
         # advice=db['advice']
         # symptoms=db['symptoms']
         # tests=db['tests']
         # # print(id)
         # prescription = db['prescription']
         # for x in prescription:
         #    name=x.get(name)
         #    options=x.get(options)
         # # dosage = request.POST.getlist('prescription[dosage]')
         # # options=request.POST.getlist('prescription[options]')
         # # name=prescription[1]
         # # options=prescription[2]
         # print(name)
         # print(options)
         # print(advice)
         # # dosage=db['dosage']
         # # duration=db['duration']
         # # takingTime=db['takingTime']
         # #frontend will send id
         # # ppt=prescriptions.objects.create(appt_id=id,prescription=ukeys,symptoms=symptoms,advice=advice,tests=tests,dosage=dosage,duration=duration,takingTime=takingTime)
         # # ppt.save()
         # return JsonResponse({'message':'Appointment updated successfully'}) 
         data = json.loads(request.body)
         id=data['id']
         idd=data['idd']
         advice = data.get('advice', '')
         priscription = data.get('priscription', [])
         symptoms = data.get('symptoms', '')
         tests = data.get('tests', '')
         for prescription_item in priscription:
                name = prescription_item.get('name', '')
                options = prescription_item.get('options', [])
         options_details = []
         prescription_details = []
         prescription_details.append({
                    'name': name,
                    'options': options_details
                })
         for option in options:
                    dosage = option.get('dosage', '')
                    duration = option.get('duration', '')
                    taking_time = option.get('takingTime', '')
         options_details.append({
                        'dosage': dosage,
                        'duration': duration,
                        'takingTime': taking_time
                    })
         print(prescription_details)
         print(options_details)
         ppt=prescriptions.objects.create(appt_id=id,patient_id=idd,prescription=name,symptoms=symptoms,advice=advice,tests=tests,dosage=dosage,duration=duration,takingTime=taking_time)
         return JsonResponse({'message':'Appointment updated successfully'},status=200) 
            # Process the data as needed
            # For example, you can save it to a database or perform calculations

            # Return a JSON response
      if request.method=='GET': 
         user=request.user.id
         n=User.objects.get(id=user)
         patient_first_name=n.first_name
         patient_last_name=n.last_name
         d=patientsh.objects.get(patient_id=user)
         age=d.age
         gender=d.yourgender
         i=appointmentsh.objects.get(patient2_id=user)
         doctor_first_name=i.doctor.doctor.first_name
         doctor_last_name=i.doctor.doctor.last_name
         depart=i.doctor.department
         data=({'patient_first_name':patient_first_name,'patient_second_name':patient_last_name,'age':age,'gender':gender,'doctor_first_name':doctor_first_name,'doctor_last_name':doctor_last_name,'depart':depart}) 
         return JsonResponse(data,safe=False,status=200)
def showprescription(request):
    if request.user.is_authenticated:
       if request.method=='GET':  
         #  user=request.user.id
          idd=request.GET.get('idd')
          id=patientsh.objects.get(patient_id=idd).pk
          pres=prescriptions.objects.filter(patient_id=id)
          data = [{'prescription': x.prescription,'symptoms': x.symptoms,'advice': x.advice,'tests': x.tests,'dosage': x.dosage,'duration': x.duration} for x in pres]
          return JsonResponse(data,safe=False,status=200)
def prescription1(request):
    if request.user.is_authenticated:
       if request.method=='GET':  
         #  user=request.user.id
          id=request.GET.get('id')
          print(id)
         #  id=patientsh.objects.get(patient_id=idd).pk
          pres=prescriptions.objects.filter(appt_id=id)
          data0= [{'prescription': x.prescription,'symptoms': x.symptoms,'advice': x.advice,'tests': x.tests,'dosage': x.dosage,'duration': x.duration} for x in pres]
          i=appointmentsh.objects.get(id=id)
          doctor_first_name=i.doctor.doctor.first_name
          doctor_last_name=i.doctor.doctor.last_name
          depart=i.doctor.department
          patient_first_name=i.patient2.first_name
          patient_last_name=i.patient2.last_name
          age=i.patient.age
          gender=i.patient.yourgender
          data1=({'patient_first_name':patient_first_name,'patient_second_name':patient_last_name,'age':age,'gender':gender,'doctor_first_name':doctor_first_name,'doctor_last_name':doctor_last_name,'depart':depart})
          data=[{'data1':data0,'data2':data1}]
          return JsonResponse(data,safe=False,status=200)  
# def departmentwisedoctor(request):
#      if request.method=='POST':
#          user=request.user.id
#          db=json.loads(request.body)
#          depart=db['depart']
def dynamicpanel1(request):
   if request.user.is_authenticated:
      if request.method=='GET':  
          user=request.user.id
          role0=roles.objects.get(user_id=user)
          print(user)
          rol=role0.role 
          if rol=='patient':
             pre=dynamicpanel.objects.filter(role1=rol,removed=False)
             data = [{'text1': x.text1,'text_link': x.text_link,'order1': x.order1,'icon':str(x.icon)} for x in pre]
             return JsonResponse(data,safe=False,status=200)
          elif rol=='doctor':
             pre=dynamicpanel.objects.filter(role1=rol,removed=False)
             data = [{'text1': x.text1,'text_link': x.text_link,'order1': x.order1,'icon':str(x.icon)} for x in pre]
             return JsonResponse(data,safe=False,status=200)
          else:
             pre=dynamicpanel.objects.filter(role1=rol,removed=False)
             data = [{'text1': x.text1,'text_link': x.text_link,'order1': x.order1,'icon':str(x.icon)} for x in pre]
             return JsonResponse(data,safe=False,status=200)
def upload_file(request):             
    if request.method == 'POST':
        newdoc = dynamicpanel(icon=request.FILES.get('myfile'))
        newdoc.save()
        return JsonResponse({'message':'Appointment updated successfully'},status=200) 
def fee(request):
   if request.user.is_authenticated:
      if request.method=='GET':
        user=request.user.id
        id1=request.GET.get('id')
        rw=appointmentsh.objects.get(removed=False,id=id1,patient2_id=user) 
        id=rw.id
        print(id)
        pay=payment.objects.get(appt_id=50,refund=False) 
        wt =           {'first_name': rw.patient2.first_name ,
                           'last_name': rw.patient2.last_name ,
                            'username': rw.patient2.username ,
                            'email': rw.patient2.email ,
                            'start_time': rw.start_time ,
                            'end_time': rw.end_time ,
                            'doctor_firstname': rw.doctor.doctor.first_name ,
                            'doctor_lastname': rw.doctor.doctor.last_name ,
                            'doctor_department': rw.doctor.department ,
                            'date': rw.date,
                            'amount':pay.payment}
        template_name = 'base.html'
        response = HttpResponse(content_type="application/pdf")
        helpers.render_pdf(
            template=template_name,
            file_=response,
            context=wt
        )
        return response

# def chart(request):
#     if request.method == 'POST':
#        depart=department.objects.all()
# def luckydraw(request):
#     if request.method == 'GET':
#        arr=["Ananya","Sukriti","Srijan","Siddharth","Nikhil","Keshav","Saurbh","Himanshu","Amritansh","Mayank","Swapnil"]
#        i=0
#        while i<20:
#         z=random.choice(arr)
#         i=i+1
#        print(z)
#        data=[{'luck':i}for i in z]
#        return JsonResponse(data,safe=False)
 
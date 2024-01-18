from django.urls import path

from . import views

urlpatterns = [
     path('patientregister', views.patientregister, name='patientregister'),
     path('doctorregister', views.doctorregister, name='doctorregister'),
     path('login1', views.login1, name='login1'),
     path('logout1', views.logout1, name='logout1'),
     path('patientdashboard1', views.patientdashboard1, name='patientdashboard1'),
     path('patientdashboard2', views.patientdashboard2, name='patientdashboard2'),
     path('patientdashboard3', views.patientdashboard3, name='patientdashboard3'),
     path('patientdashboard4', views.patientdashboard4, name='patientdashboard4'),
     #  path('patientdashboard5', views.patientdashboard5, name='patientdashboard5'),
     path('departmentwisedoc', views.departmentwisedoc, name='departmentwisedoc'),
     path('medicalhistory', views.medicalhistory, name='medicalhistory'),
     path('appointment', views.appointment, name='appointment'),
     path('appointment1', views.appointment1, name='appointment1'),
     path('doctordashboard0', views.doctordashboard0, name='doctordashboard0'),
     path('doctordashboard', views.doctordashboard, name='doctordashboard'),
     path('doctordashboard1', views.doctordashboard1, name='doctordashboard1'),
     path('receptionistdashboard1', views.receptionistdashboard1, name='receptionistdashboard1'),
     path('receptionistdashboard2', views.receptionistdashboard2, name='receptionistdashboard2'),
     path('receptionistdashboard3', views.receptionistdashboard3, name='receptionistdashboard3'),
     path('receptionistdashboard4', views.receptionistdashboard4, name='receptionistdashboard4'),
     path('recaprvd', views.recaprvd, name='recaprvd'),
     path('docaprvd', views.docaprvd, name='docaprvd'),
     path('delete', views.delete, name='delete'),
     path('doc_delete', views.doc_delete, name='doc_delete'),
     path('update', views.update, name='update'),
     path('showpaymenthist', views.showpaymenthist, name='showpaymenthist'),
     #path('addprescription0', views.addprescription0, name='addprescription0'),
     path('addprescription', views.addprescription, name='addprescription'),
     path('showprescription', views.showprescription, name='showprescription'),
     path('prescription1', views.prescription1, name='prescription1'),     
     path('dynamicpanel1', views.dynamicpanel1, name='dynamicpanel1'),
     path('upload_file', views.upload_file, name='upload_file'),
     #path('luckydraw', views.luckydraw, name='luckydraw'),
     path('fee', views.fee, name='fee'),
]
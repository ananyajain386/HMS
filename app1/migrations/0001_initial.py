# Generated by Django 2.2 on 2023-09-16 15:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='patientsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('illness', models.CharField(max_length=30, null=True)),
                ('medicineshist', models.CharField(max_length=100, null=True)),
                ('familyhistory', models.CharField(max_length=30, null=True)),
                ('systolic_bp', models.CharField(max_length=30, null=True)),
                ('diastolic_bp', models.CharField(max_length=30, null=True)),
                ('heartrate', models.CharField(max_length=30, null=True)),
                ('phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='doctorsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=10, null=True)),
                ('fees', models.IntegerField(null=True)),
                ('morningtime', models.TimeField(null=True)),
                ('eveningtime', models.TimeField(null=True)),
                ('shifts', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('Img', models.ImageField(blank=True, upload_to='Pictures/')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='appointmentsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=30, null=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.doctorsh')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patientsh')),
            ],
            options={
                'db_table': 'Appointments',
            },
        ),
    ]
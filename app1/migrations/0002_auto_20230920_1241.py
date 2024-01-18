# Generated by Django 2.2 on 2023-09-20 12:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentsh',
            name='docaprvd',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointmentsh',
            name='patient2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointmentsh',
            name='recaprvd',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointmentsh',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointmentsh',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.patientsh'),
        ),
        migrations.AlterField(
            model_name='doctorsh',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='diastolic_bp',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='familyhistory',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='heartrate',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='illness',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='medicineshist',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='phone_number',
            field=models.CharField(blank=True, default=1, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsh',
            name='systolic_bp',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patientsh')),
            ],
            options={
                'db_table': 'Payments',
            },
        ),
    ]

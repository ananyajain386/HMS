# Generated by Django 2.2 on 2023-09-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_auto_20230928_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentsh',
            name='reason',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
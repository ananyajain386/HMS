# Generated by Django 2.2 on 2023-09-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_appointmentsh_reason'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentsh',
            old_name='reason',
            new_name='doc_reason',
        ),
        migrations.AddField(
            model_name='appointmentsh',
            name='rec_reason',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

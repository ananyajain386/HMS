# Generated by Django 2.2 on 2023-09-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_auto_20230929_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='role',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

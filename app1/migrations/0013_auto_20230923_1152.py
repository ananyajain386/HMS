# Generated by Django 2.2 on 2023-09-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20230923_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicpanel',
            name='role',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
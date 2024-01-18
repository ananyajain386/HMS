# Generated by Django 2.2 on 2023-09-23 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20230920_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=150, null=True)),
            ],
            options={
                'db_table': 'Departments',
            },
        ),
        migrations.AddField(
            model_name='doctorsh',
            name='depart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.departments'),
        ),
    ]
# Generated by Django 2.2 on 2023-09-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_payment_refund'),
    ]

    operations = [
        migrations.CreateModel(
            name='dynamicpanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, null=True)),
                ('text_link', models.CharField(max_length=150, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.roles')),
            ],
            options={
                'db_table': 'Dynamic Panel',
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-07 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotalapp', '0005_staff_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cust',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='approved',
        ),
    ]

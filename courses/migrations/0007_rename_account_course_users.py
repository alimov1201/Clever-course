# Generated by Django 5.1.1 on 2024-10-05 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='account',
            new_name='users',
        ),
    ]

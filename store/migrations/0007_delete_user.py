# Generated by Django 4.2.11 on 2024-07-16 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_password1_user_password_remove_user_password2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
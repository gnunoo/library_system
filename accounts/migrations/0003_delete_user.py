# Generated by Django 4.0.4 on 2022-06-02 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
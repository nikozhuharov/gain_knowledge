# Generated by Django 4.0.3 on 2022-04-08 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_course_description_alter_course_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]

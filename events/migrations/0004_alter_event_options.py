# Generated by Django 4.2.8 on 2024-01-09 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_on']},
        ),
    ]

# Generated by Django 3.1.5 on 2021-04-20 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0006_auto_20190408_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id']},
        ),
    ]

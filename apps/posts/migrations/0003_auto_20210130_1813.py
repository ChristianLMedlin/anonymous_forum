# Generated by Django 3.1.5 on 2021-01-30 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210130_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-creation_date']},
        ),
    ]

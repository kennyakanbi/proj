# Generated by Django 5.1.5 on 2025-04-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_internship'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='proj_report',
            field=models.TextField(default='NOT SUBMITTED', max_length=60),
            preserve_default=False,
        ),
    ]

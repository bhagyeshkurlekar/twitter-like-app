# Generated by Django 2.2.3 on 2019-07-21 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='question',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
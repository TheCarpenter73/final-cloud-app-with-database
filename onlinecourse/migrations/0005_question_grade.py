# Generated by Django 4.1.6 on 2023-02-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onlinecourse", "0004_alter_question_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="grade",
            field=models.FloatField(default=0.0),
        ),
    ]
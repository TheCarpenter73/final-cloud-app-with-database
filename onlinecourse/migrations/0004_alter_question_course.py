# Generated by Django 4.1.6 on 2023-02-12 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("onlinecourse", "0003_alter_question_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course"
            ),
        ),
    ]
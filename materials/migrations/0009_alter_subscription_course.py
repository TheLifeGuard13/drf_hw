# Generated by Django 5.0.6 on 2024-05-16 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0008_alter_subscription_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET,
                related_name="course_for_subscription",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]

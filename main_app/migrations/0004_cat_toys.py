# Generated by Django 4.2.16 on 2024-12-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0003_toy_alter_feeding_options_alter_feeding_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="cat",
            name="toys",
            field=models.ManyToManyField(to="main_app.toy"),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0003_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                default="profile_pics/default.jpg", null=True, upload_to="profile_pics/"
            ),
        ),
    ]
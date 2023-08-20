# Generated by Django 4.0.6 on 2023-08-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='id_client',
        ),
        migrations.AddField(
            model_name='pet',
            name='available_for_adoption',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
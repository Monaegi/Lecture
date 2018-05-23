# Generated by Django 2.0 on 2018-01-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, upload_to='user'),
        ),
        migrations.AddField(
            model_name='user',
            name='period',
            field=models.CharField(blank=True, choices=[('3', '3기'), ('4', '4기'), ('5', '5기'), ('6', '6기'), ('7', '7기')], max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('instructor', '강사'), ('assistant', '조교'), ('manager', '매니저'), ('student', '수강생')], default='student', max_length=20),
            preserve_default=False,
        ),
    ]
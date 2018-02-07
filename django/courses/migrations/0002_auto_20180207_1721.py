# Generated by Django 2.0.1 on 2018-02-07 08:21

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': '강의 섹션',
                'verbose_name_plural': '강의 섹션 목록',
            },
        ),
        migrations.CreateModel(
            name='SectionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', martor.models.MartorField(blank=True)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Section')),
            ],
            options={
                'verbose_name': '섹션 노트',
                'verbose_name_plural': '섹션 노트 목록',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '강의 기수', 'verbose_name_plural': '강의 기수 목록'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': '강의', 'verbose_name_plural': '강의 목록'},
        ),
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Subject'),
        ),
    ]
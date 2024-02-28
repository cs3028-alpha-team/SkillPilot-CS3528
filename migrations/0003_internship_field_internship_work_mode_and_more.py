# Generated by Django 5.0.2 on 2024-02-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_rename_internships_internship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='field',
            field=models.CharField(default='Nursing', max_length=100),
        ),
        migrations.AddField(
            model_name='internship',
            name='work_mode',
            field=models.CharField(choices=[('online', 'Online'), ('in-person', 'In-Person'), ('hybrid', 'Hybrid')], default='in-person', max_length=10),
        ),
        migrations.AddField(
            model_name='internship',
            name='work_pattern',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time')], default='FT', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='field',
            field=models.CharField(default='Nursing', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='mode_study',
            field=models.CharField(choices=[('online', 'Online'), ('in-person', 'In-Person'), ('hybrid', 'Hybrid')], default='in-person', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='study_pattern',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time')], default='FT', max_length=2),
        ),
    ]
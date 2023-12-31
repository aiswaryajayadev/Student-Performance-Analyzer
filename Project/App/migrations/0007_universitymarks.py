# Generated by Django 4.2.1 on 2023-06-28 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_delete_universitymarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityMarks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sem_no', models.IntegerField(default=0)),
                ('university_marks', models.FloatField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.subjects')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.students')),
            ],
        ),
    ]

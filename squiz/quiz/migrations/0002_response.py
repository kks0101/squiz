# Generated by Django 2.2.2 on 2019-06-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_ans', models.CharField(max_length=2000)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]
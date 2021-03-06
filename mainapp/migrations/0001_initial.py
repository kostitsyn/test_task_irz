# Generated by Django 4.0 on 2021-12-27 10:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64, verbose_name='Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Surname')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Date of creation')),
                ('title', models.CharField(max_length=256, verbose_name='Task title')),
                ('is_answered', models.BooleanField(db_index=True, default=False, verbose_name='Is it question answered')),
                ('link', models.URLField(verbose_name='link to question')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-creation_date'],
            },
        ),
    ]

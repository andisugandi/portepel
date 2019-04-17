# Generated by Django 2.2 on 2019-04-17 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Finishing GCP and Kubernetes Quests', max_length=255),
            preserve_default=False,
        ),
    ]
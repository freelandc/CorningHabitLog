# Generated by Django 3.0.7 on 2020-06-08 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.PositiveIntegerField(null=True)),
                ('sleep', models.PositiveIntegerField(null=True)),
                ('meals', models.PositiveIntegerField(null=True)),
                ('sweets', models.PositiveIntegerField(null=True)),
                ('junkfood', models.PositiveIntegerField(null=True)),
                ('crosstraining', models.PositiveIntegerField(null=True)),
                ('core', models.PositiveIntegerField(null=True)),
                ('lifting', models.PositiveIntegerField(null=True)),
                ('stretching', models.PositiveIntegerField(null=True)),
                ('mood', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

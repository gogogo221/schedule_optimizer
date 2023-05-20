# Generated by Django 4.2.1 on 2023-05-19 20:55

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
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("tag", models.CharField(max_length=50)),
                ("units", models.IntegerField()),
                ("semester", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("rating", models.DecimalField(decimal_places=3, max_digits=5)),
                ("num_ratings", models.IntegerField()),
                ("difficulty", models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name="Time",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.CharField(max_length=10)),
                ("start", models.CharField(max_length=10)),
                ("end", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("type", models.CharField(max_length=20)),
                ("capacity", models.IntegerField()),
                ("registered", models.IntegerField()),
                ("dclearence", models.BooleanField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="optimizer.course",
                    ),
                ),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="optimizer.professor",
                    ),
                ),
                (
                    "time",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="optimizer.time"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("units", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="todolist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="schedule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="optimizer.schedule"
            ),
        ),
    ]
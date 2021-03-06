# Generated by Django 4.0.3 on 2022-05-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='do_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='In Progress', max_length=15),
        ),
    ]

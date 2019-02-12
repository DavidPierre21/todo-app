# Generated by Django 2.1.5 on 2019-02-12 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.Todo'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-02-22 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_auto_20190221_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todos.Todo'),
        ),
    ]
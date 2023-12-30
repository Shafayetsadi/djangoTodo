# Generated by Django 4.1.3 on 2023-12-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='task',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-31 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_shoppinglistitem_bought'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoListItem',
            fields=[
                ('name', models.TextField(max_length=40)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]

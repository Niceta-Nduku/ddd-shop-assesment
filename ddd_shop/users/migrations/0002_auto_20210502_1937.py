# Generated by Django 3.1.8 on 2021-05-02 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_attendant',
            field=models.BooleanField(default=False, help_text='Designates whether this user is a store attendant', verbose_name='attendant status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False, help_text='Designates whether this user is the owner of a store', verbose_name='owner status'),
        ),
        migrations.CreateModel(
            name='StoreOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ManyToManyField(blank=True, to='shop.Store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreAttendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

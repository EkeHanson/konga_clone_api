# Generated by Django 5.1.1 on 2024-09-06 21:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('level', models.CharField(choices=[('VIP1', 'VIP1'), ('VIP2', 'VIP2'), ('VIP3', 'VIP3')], max_length=5)),
                ('reset_token', models.CharField(blank=True, max_length=100, null=True)),
                ('reset_token_expires', models.DateTimeField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('balance', models.DecimalField(decimal_places=1, default=0.0, max_digits=10)),
                ('unsettle', models.DecimalField(decimal_places=1, default=0.0, max_digits=10)),
                ('commission1', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('commission2', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('withdrawalPassword', models.CharField(max_length=255)),
                ('grabbed_orders_count', models.PositiveIntegerField(default=0)),
                ('firstName', models.CharField(blank=True, max_length=255, null=True)),
                ('lastName', models.CharField(blank=True, max_length=255, null=True)),
                ('middleName', models.CharField(default='None', max_length=255)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('client', 'Client')], max_length=10)),
                ('created_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('invitationCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.invitationcode')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]

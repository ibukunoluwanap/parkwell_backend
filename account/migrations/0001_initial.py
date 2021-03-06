# Generated by Django 3.1.8 on 2021-08-08 08:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification', models.BooleanField(default=False, verbose_name='verification')),
                ('is_company_admin', models.BooleanField(default=False, verbose_name='Company admin')),
                ('photo', models.ImageField(blank=True, default='../static/images/avatar.png', null=True, upload_to='administrator_photos/', verbose_name="Administrator's photo(optional)")),
                ('mobile_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid mobile number!', regex='^\\+?1?\\d{9,15}$')], verbose_name="Administrator's mobile number")),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
        ),
        migrations.CreateModel(
            name='ParkAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='../static/images/avatar.png', null=True, upload_to='administrator_photos/', verbose_name="Park Admin's photo(optional)")),
                ('mobile_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid mobile number!', regex='^\\+?1?\\d{9,15}$')], verbose_name="Park Admin's mobile number")),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('company_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.administrator')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ParkAdmin',
                'verbose_name_plural': 'ParkAdmins',
            },
        ),
    ]

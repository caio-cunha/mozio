# Generated by Django 4.0.4 on 2022-06-02 13:22

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('language', models.CharField(blank=True, choices=[('BRA', 'Brazil'), ('SPA', 'Spanish'), ('ENG', 'English'), ('CHI', 'Chinese'), ('AR', 'Arabic'), ('HIN', 'Hindi'), ('JPN', 'Japanese'), ('GER', 'German'), ('FRA', 'French')], max_length=3, null=True)),
                ('currency', models.CharField(blank=True, choices=[('BRL', 'Real'), ('EUR', 'Euro'), ('JPY', 'Japanese Yen'), ('CNY', 'Chinese Yuan'), ('INR', 'Indian Rupee'), ('USD', 'US Dollar'), ('GBP', 'Pound')], max_length=3, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

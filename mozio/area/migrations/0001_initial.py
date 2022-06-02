# Generated by Django 4.0.4 on 2022-06-02 13:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('geojson', models.JSONField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.provider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

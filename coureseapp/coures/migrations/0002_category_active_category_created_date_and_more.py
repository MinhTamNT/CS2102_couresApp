# Generated by Django 4.2.6 on 2023-10-22 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=255)),
                ('descrption', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coures.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]

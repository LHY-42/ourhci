# Generated by Django 4.0 on 2022-02-12 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0005_user_consortium_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.user')),
            ],
        ),
    ]

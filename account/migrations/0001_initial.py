<<<<<<< Updated upstream
# Generated by Django 3.0.5 on 2020-04-10 19:50
=======
# Generated by Django 3.0.5 on 2020-04-10 15:44
>>>>>>> Stashed changes

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
<<<<<<< Updated upstream
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
>>>>>>> Stashed changes
                ('phone_number', models.CharField(max_length=11)),
                ('email_address', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('city', models.CharField(default='تهران', max_length=30)),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر',
            },
        ),
    ]
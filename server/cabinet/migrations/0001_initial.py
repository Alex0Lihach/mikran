

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=5)),
                ('subdivision', models.CharField(max_length=30)),
                ('birth_date', models.DateField(null=True)),
                ('position', models.CharField(max_length=30)),
                ('experience', models.FloatField(default='0.0')),
                ('shift', models.CharField(max_length=30)),
                ('part_time_job', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30)),
                ('lateness', models.TimeField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

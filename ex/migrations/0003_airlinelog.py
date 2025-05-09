from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ex', '0002_flightreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_founded', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ex', '0003_airlinelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='total_flight_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

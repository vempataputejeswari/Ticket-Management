from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_Tutorial',
            fields=[
                 ('title_name', models.CharField(max_length=70, default='')),
                 ('language', models.TextField(max_length = 160)),
                 ('airing_date',  models.DateField()),
                 ('theater_name', models.CharField(max_length = 200)),
                 ('city',  models.CharField(default='', max_length=70)),
                 ('movie_rating', models.BooleanField(default=False)),
                ('casts', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=15)),
                ('movie_name',models.CharField(max_length = 200)),
                ('ticket_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

            ],
        ),
    ]
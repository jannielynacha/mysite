# Generated by Django 3.2.8 on 2021-10-10 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Critic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('sort_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('bio', models.CharField(max_length=300)),
                ('seo_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_title', models.CharField(max_length=5000)),
                ('mpaa_rating', models.CharField(max_length=100)),
                ('critics_pick', models.IntegerField()),
                ('headline', models.CharField(max_length=400)),
                ('summary_short', models.CharField(max_length=500)),
                ('publication_date', models.CharField(max_length=100)),
                ('opening_date', models.CharField(max_length=100)),
                ('date_updated', models.CharField(max_length=100)),
                ('review_text', models.CharField(max_length=200)),
                ('byline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.critic')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='reviews.review')),
                ('type', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('suggested_link_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='reviews.review')),
                ('type', models.CharField(max_length=100)),
                ('src', models.CharField(max_length=500)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
    ]

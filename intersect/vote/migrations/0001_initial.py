# Generated by Django 2.1.7 on 2019-04-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAction', models.IntegerField()),
                ('reason', models.CharField(max_length=30)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Intersection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idIntersecion', models.IntegerField()),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('intersectionName', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idIntervention', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('beginning', models.DateField()),
                ('ending', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('actionIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Action')),
                ('intersectionIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Intersection')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idVote', models.IntegerField()),
                ('response', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('intersectionIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Intersection')),
            ],
        ),
    ]
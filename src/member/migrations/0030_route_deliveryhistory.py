# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 21:36
from __future__ import unicode_literals

import annoying.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0029_member_address_fk_to_1to1'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date of the delivery')),
                ('vehicle', models.CharField(choices=[('cycling', 'Cycling'), ('walking', 'Walking'), ('driving', 'Driving')], max_length=20, verbose_name='vehicle')),
                ('client_id_sequence', annoying.fields.JSONField(default=[], verbose_name='IDs of clients on this route (as a JSON list)')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='comments')),
            ],
            options={
                'verbose_name': 'Delivery History',
                'ordering': ['route', '-date'],
                'verbose_name_plural': 'Delivery Histories',
            },
        ),
        migrations.AlterField(
            model_name='route',
            name='client_id_sequence',
            field=annoying.fields.JSONField(default=[], verbose_name='IDs of clients on this route (as a JSON list)'),
        ),
        migrations.AddField(
            model_name='deliveryhistory',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_histories', to='member.Route', verbose_name='route'),
        ),
        migrations.AlterUniqueTogether(
            name='deliveryhistory',
            unique_together=set([('route', 'date')]),
        ),
    ]

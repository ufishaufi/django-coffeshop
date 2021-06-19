# Generated by Django 3.2.4 on 2021-06-19 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=10000)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meja', models.CharField(max_length=100)),
                ('pelanggan', models.CharField(max_length=100)),
                ('total', models.PositiveIntegerField(default=0)),
                ('dibayar', models.PositiveIntegerField(default=0)),
                ('kembalian', models.PositiveIntegerField(default=0)),
                ('selesai', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('harga', models.PositiveIntegerField(default=0)),
                ('subtotal', models.PositiveIntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='pos.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='pos.order')),
            ],
        ),
    ]

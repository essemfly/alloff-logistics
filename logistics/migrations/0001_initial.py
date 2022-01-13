# Generated by Django 4.0 on 2022-01-10 19:43

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sweettracker_id', models.CharField(max_length=6)),
                ('tracking_url_base', models.TextField(blank=True, default='https://search.naver.com/search.naver?query=')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=30)),
                ('status', models.CharField(choices=[('IN_STOCK', 'In Stock'), ('PROCESSING_NEEDED', 'Processing Needed'), ('SHIPPED', 'Shipped'), ('SHIPPING_PENDING', 'Shipping Pending')], max_length=30)),
                ('product_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=20)),
                ('product_brand_id', models.CharField(max_length=20)),
                ('product_brand_name', models.CharField(max_length=20)),
                ('product_size', models.CharField(max_length=10)),
                ('product_color', models.CharField(max_length=10)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('memo', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'inventories',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=13, unique=True)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('LOCKED', 'Locked'), ('SEALED', 'Sealed'), ('SHIPPED', 'Shipped')], default='CREATED', max_length=20)),
                ('template_url', models.URLField(blank=True, null=True)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('sealed_at', models.DateTimeField(blank=True, null=True)),
                ('shipped_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('MADAM', 'Madam'), ('MALL', 'Mall'), ('OFFLINE', 'Offline'), ('INVENTORY', 'Inventory')], max_length=20)),
                ('bank_name', models.CharField(max_length=20)),
                ('bank_account_holder', models.CharField(max_length=40)),
                ('bank_account_number', models.CharField(max_length=40)),
                ('biz_registration_id', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingNoticeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='logistics.inventory')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='logistics.shippingnotice')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=30)),
                ('status', models.CharField(choices=[('SOURCING_REQUIRED', 'Sourcing Required'), ('ON_RECEIVING', 'On Receiving'), ('RECEIVED', 'Received'), ('OUT_OF_STOCK', 'Out Of Stock'), ('CANCELED', 'Canceled')], default='SOURCING_REQUIRED', max_length=50)),
                ('product_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=20)),
                ('product_brand_id', models.CharField(max_length=20)),
                ('product_brand_name', models.CharField(max_length=20)),
                ('product_size', models.CharField(max_length=10)),
                ('product_color', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='logistics.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='PackageRemarkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('CANCELED', 'Canceled'), ('PARTIALLY_CANCELED', 'Partially Canceled'), ('PARTIALLY_SHIPMENT', 'Partially Shipment'), ('COMBINE_SHIPMENT', 'Combine Shipment')], max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('reference', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('DELIVERY_PREPARING', 'Delivery Preparing'), ('DELIVERY_STARTED', 'Delivery Started'), ('DELIVERY_FINISHED', 'Delivery Finished'), ('OVERSEA_SHIPMENT_PREPARING', 'Oversea Shipment Preparing'), ('OVERSEA_SHIPMENT_STARTED', 'Oversea Shipment Started'), ('CANCEL_REQUESTED', 'Cancel Requested'), ('CANCEL_PENDING', 'Cancel Pending'), ('CANCEL_FINISHED', 'Cancel Finished')], max_length=50)),
                ('related_order_item_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=list, size=None)),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_contact', models.CharField(max_length=13)),
                ('base_address', models.CharField(max_length=255)),
                ('detail_address', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=6)),
                ('delivery_note', models.CharField(max_length=50)),
                ('tracking_number', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('inventories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistics.inventory')),
                ('remark_records', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.packageremarkrecord')),
                ('tracking_courier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistics.courier')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedItemLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logistics.log')),
                ('received_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistics.receiveditem')),
            ],
            bases=('logistics.log',),
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logistics.log')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistics.inventory')),
            ],
            bases=('logistics.log',),
        ),
    ]
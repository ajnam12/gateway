# Generated by Django 3.2.2 on 2021-09-13 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_community_readable_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetagovID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.PositiveIntegerField(unique=True)),
                ('external_id', models.PositiveIntegerField(unique=True)),
                ('primary', models.BooleanField(default=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.community')),
                ('linked_ids', models.ManyToManyField(related_name='_core_metagovid_linked_ids_+', to='core.MetagovID')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_platform_id', models.CharField(blank=True, max_length=100, null=True)),
                ('platform_type', models.CharField(max_length=50)),
                ('platform_identifier', models.CharField(max_length=200)),
                ('custom_data', models.JSONField(default=dict)),
                ('link_type', models.CharField(choices=[('oauth', 'OAUTH'), ('manual admin', 'MANUAL_ADMIN'), ('email matching', 'EMAIL_MATCHING'), ('unknown', 'UNKNOWN')], default='unknown', max_length=30)),
                ('link_quality', models.CharField(choices=[('confirmed (strong)', 'STRONG_CONFIRM'), ('confirmed (weak)', 'WEAK_CONFIRM'), ('unconfirmed', 'UNCONFIRMED'), ('unknown', 'UNKNOWN')], default='unknown', max_length=30)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.community')),
                ('metagov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_accounts', to='core.metagovid')),
            ],
        ),
        migrations.AddConstraint(
            model_name='linkedaccount',
            constraint=models.UniqueConstraint(fields=('community', 'community_platform_id', 'platform_type', 'platform_identifier'), name='unique_identifer_on_community_platform'),
        ),
    ]

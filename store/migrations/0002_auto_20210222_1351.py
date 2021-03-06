# Generated by Django 3.1.6 on 2021-02-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='codepostal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='pays',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='rue',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='ville',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='typeproduit',
            name='unite_mesure',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

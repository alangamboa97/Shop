# Generated by Django 3.1.6 on 2021-02-04 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Mat',
            fields=[
                ('idCategoriaCatM', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCatM', models.CharField(max_length=50)),
                ('descripcionCatM', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Prod',
            fields=[
                ('idCategoriaCatP', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCatP', models.CharField(max_length=50)),
                ('descripcionCatP', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('idMaterial', models.AutoField(primary_key=True, serialize=False)),
                ('descripcionMat', models.CharField(max_length=100)),
                ('nombreMat', models.CharField(max_length=50)),
                ('costoMat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cantidadMat', models.IntegerField(default=0)),
                ('unidadMat', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('idCategoriaMat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria_mat')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcionProd', models.CharField(max_length=100)),
                ('nombreProd', models.CharField(max_length=50)),
                ('imgProd', models.ImageField(blank=True, null=True, upload_to='media/productos')),
                ('precioProd', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('idCategoriaProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria_prod')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionTemp', models.CharField(max_length=100)),
                ('nombreTemp', models.CharField(max_length=50)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('tipo', models.CharField(choices=[('0', 'necesario'), ('1', 'extra')], max_length=1)),
                ('idMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.material')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='temporada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.temporada'),
        ),
    ]

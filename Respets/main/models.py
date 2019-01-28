from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuarioid = models.AutoField(db_column='UsuarioID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=40)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=60)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='NombreUsuario', max_length=60)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=200)  # Field name made lowercase.
    genero = models.IntegerField(db_column='Genero')  # Field name made lowercase.
    adminstatus = models.BooleanField(db_column='AdminStatus')  # Field name made lowercase. .

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre



class Solicitudinteres(models.Model):
    idsolicitudinteres = models.AutoField(db_column='IDsolicitudInteres', primary_key=True)  # Field name made lowercase.
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioID')  # Field name made lowercase.
    animalid = models.ForeignKey('Animal', models.DO_NOTHING, db_column='AnimalID')  # Field name made lowercase.
    detalleid = models.ForeignKey('Detalleinteres', models.DO_NOTHING, db_column='DetalleID')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=24)  # Field name made lowercase.

    class Meta:
        db_table = 'solicitudinteres'

    def __str__(self):
        return self.idsolicitudinteres




class Detalleinteres(models.Model):
    detalleid = models.AutoField(db_column='DetalleID', primary_key=True)  # Field name made lowercase.
    descripcionadicional = models.CharField(db_column='DescripcionAdicional', max_length=300)  # Field name made lowercase.
    fechasolicitud = models.DateField(db_column='FechaSolicitud')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'detalleinteres'

    def __str__(self):
        return self.detalleid


class Animal(models.Model):
    animalid = models.AutoField(db_column='AnimalID', primary_key=True)  # Field name made lowercase.
    encargado = models.ForeignKey('Encargado', models.DO_NOTHING, db_column='Encargado')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    raza = models.CharField(db_column='Raza', max_length=40)  # Field name made lowercase.
    genero = models.BooleanField(db_column='Genero')  # Field name made lowercase.
    descripicon = models.CharField(db_column='Descripicon', max_length=300)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.
    foto = models.CharField(db_column="Foto" , max_length = 300) # Field name made lowercase.

    class Meta:
        db_table = 'animal'

    def __str__(self):
        return self.nombre




class Encargado(models.Model):
    encargadoid = models.AutoField(db_column='EncargadoID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=30)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=300)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=30)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'encargado'

    def __str__(self):
        return self.nombre

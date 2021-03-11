from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser, Permission, Group, PermissionsMixin



class state_user(models.Model):
    id_state_usr = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=20, blank=True, null=True, db_column='name_st')
    descripcion = models.CharField(max_length=50, blank=True, null=True, db_column='description')
    

    def __str__(self):
        return self.nombre_estado

    class Meta:
        db_table = 'state_user'
        verbose_name = "estado del usuario"
        verbose_name_plural = "estados de los usuarios"


class type_user(models.Model):
    id_ty_us = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50, db_column='type_name')

    def __str__(self):
        return self.tipo_usuario

    class Meta:
        db_table = 'type_user'
        verbose_name = "tipo de usuario"
        verbose_name_plural = "tipos de usuarios"



class service(models.Model):
    id_ser = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=50, db_column='name_ser')
    oferta_servicio = models.CharField(max_length=50, db_column='service_offer')

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        db_table = 'service'
        verbose_name = "servicio"
        verbose_name_plural = "servicios"


class contact_request(models.Model):
    id_request = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True, db_column='fname')
    no_celular = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, db_column='cell_phone')
    email = models.CharField(max_length=50, blank=True, null=True, db_column='email')
    mensaje = models.CharField(max_length=300, blank=True, null=True, db_column='message')
    fecha_solicitud = models.DateTimeField(blank=True,  auto_now=True, null = True, db_column='regis_date')
    atendido = models.BooleanField(default=False, db_column='check_soli')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'contact_request'
        verbose_name = "solicitud de contacto"
        verbose_name_plural = "solicitudes de contacto"

class usersManager(BaseUserManager):
    def create_superuser(self, email,no_documento, nombre, apellido, no_celular, tel_fijo,direccion, barrio, referencia_vivienda, nickname, password):
        usuario = self.create_user(email = email, no_documento = no_documento , nombre = nombre, apellido = apellido, no_celular = no_celular, tel_fijo = tel_fijo,direccion = direccion, barrio = barrio, referencia_vivienda = referencia_vivienda, nickname = nickname, password = password)
        usuario.usuario_administrador = True
        usuario.is_superuser = True
        usuario.save()
        return usuario

    def create_user(self, email,no_documento, nombre, apellido, no_celular, tel_fijo,direccion, barrio, referencia_vivienda, nickname, password ):
        if not email:
            raise ValueError('el usuario debe tener un correo electronico')
        else :
            usuario = self.model(email = self.normalize_email(email),no_documento = no_documento , nombre = nombre, apellido = apellido, no_celular = no_celular, tel_fijo = tel_fijo,direccion = direccion, barrio = barrio, referencia_vivienda = referencia_vivienda, nickname = nickname)
            usuario.set_password(password)
            
            usuario.save()
            
            return usuario

class users(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    tipo_usuario = models.ForeignKey(type_user, models.DO_NOTHING, db_column='type_user', null = True)
    no_documento = models.DecimalField(max_digits=13, decimal_places=0, null=True, db_column='document_user')
    nombre = models.CharField(max_length=50, db_column='f_name')
    apellido = models.CharField(max_length=50, db_column='l_name')
    email = models.CharField(unique=True, max_length=100)
    no_celular = models.DecimalField(max_digits=10, decimal_places=0, null=True, db_column='cell_number')
    tel_fijo = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True, db_column='phone')
    direccion = models.CharField(max_length=50, null=True, db_column='address')
    barrio = models.CharField(max_length=50, blank=True, null=True, db_column='neighborhood')
    referencia_vivienda = models.CharField(max_length=50, blank=True, null=True, db_column='home_reference')
    fecha_cumpleaños = models.DateField(blank=True, null=True, db_column='dob')
    nickname = models.CharField(max_length=30, blank=True, null=True)
    token_key = models.CharField(max_length=300, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, auto_now=True, null = True, db_column='register_date')
    estado = models.ForeignKey(state_user, models.DO_NOTHING, db_column='state_usr', null = True)

    usuario_administrador = models.BooleanField(default=False)
    objects = usersManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'no_documento', 'nombre', 'apellido', 'no_celular', 'tel_fijo','direccion', 'barrio', 'referencia_vivienda', 'nickname' ]

    def __str__(self):
        return self.email
    
    """def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
    """
    @property
    def is_staff(self):
        return self.usuario_administrador
    
    class Meta:
        db_table = 'users'
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"



class carpas(models.Model):

    nombre = models.CharField(max_length=30, null = False)
    no_personas = models.DecimalField(max_digits=2, decimal_places=0, null=False)
    no_carpas = models.DecimalField(max_digits=2, decimal_places=0, default=1, null=False)
    descripcion = models.CharField(max_length=300, null = True)
    url_img = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=60000)
 
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'carpas'
        verbose_name = "carpa"
        verbose_name_plural = "carpas"


class cant_carpas(models.Model):
    carpa = models.ForeignKey('carpas', models.DO_NOTHING, db_column='carp' )
    reserva = models.ForeignKey('reservas', models.DO_NOTHING, db_column='reser' )
    cantidad = models.PositiveSmallIntegerField(default = 1, db_column='cant', null = False )

class reservas(models.Model):

    fecha_llegada = models.DateField(null=False)
    hora_llegada = models.TimeField()
    fecha_salida = models.DateField(null=False)
    hora_salida = models.TimeField()

    no_personas = models.DecimalField( max_digits=2, decimal_places=0, default=2)
    nombre = models.CharField(max_length=30, null = False)
    celular = models.DecimalField(max_digits=10, decimal_places=0, default=2)
    email = models.EmailField()
    no_documento = models.DecimalField(max_digits=13, decimal_places=0)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'reservations'
        verbose_name = "reservacion"
        verbose_name_plural = "reservaciones"

        constraints = [
            models.UniqueConstraint(fields=['carpas', 'fecha_llegada'], name='reserva_carpa_uno'),
            models.UniqueConstraint(fields=['carpas', 'fecha_salida'], name='reserva_carpa_dos'),

        ]


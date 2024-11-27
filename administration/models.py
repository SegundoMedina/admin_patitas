from django.db import models

# Create your models here.
class Provider(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Nombres")
    last_name = models.CharField(max_length=128, verbose_name="Apellidos")
    main_photo = models.ImageField(upload_to="provider/", blank=True, null=True, verbose_name="Selecciona tu foto")
    description = models.TextField(verbose_name="Describe al paseador")

class Meta:
    verbose_name_plural = "Paseadores"
    verbose_name = "Paseador"
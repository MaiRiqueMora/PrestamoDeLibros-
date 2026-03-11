from django.db import models

class Lector(models.Model):
    CodLector = models.AutoField(primary_key=True)
    ApellidoP = models.CharField(max_length=100)
    ApellidoM = models.CharField(max_length=100)
    Nombres = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ApellidoP} {self.ApellidoM}, {self.Nombres}"

class Autor(models.Model):
    CodAutor = models.AutoField(primary_key=True)
    NombreAutor = models.CharField(max_length=200)

    def __str__(self):
        return self.NombreAutor

class Editorial(models.Model):
    CodEditorial = models.AutoField(primary_key=True)
    NombreEditorial = models.CharField(max_length=200)

    def __str__(self):
        return self.NombreEditorial

class Libro(models.Model):
    CodLibro = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=255)
    autores = models.ManyToManyField(Autor, through='LibroAutor')
    editoriales = models.ManyToManyField(Editorial, through='LibroEditorial')

    def __str__(self):
        return self.Titulo

class LibroAutor(models.Model):
    CodLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    CodAutor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['CodLibro', 'CodAutor']]

class LibroEditorial(models.Model):
    CodLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    CodEditorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['CodLibro', 'CodEditorial']]

class Pristano(models.Model):
    CodLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    CodLector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    FechaDev = models.DateField()

    class Meta:
        unique_together = [['CodLibro', 'CodLector']]
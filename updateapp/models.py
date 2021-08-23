from django.db import models

class Produtos(models.Model):
    id=models.BigAutoField(primary_key=True)
    nome=models.CharField(max_length=255, blank=False)
    descrição=models.TextField(blank=False)
    foto=models.FileField(upload_to="media/%y/%m/%d/")


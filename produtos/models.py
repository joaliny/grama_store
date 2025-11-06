from django.db import models

class Grama(models.Model):
    TIPOS_GRAMA = [
        ('ESMERALDA', 'Grama Esmeralda'),
        ('SAO_CARLOS', 'Grama São Carlos'), 
        ('BERMUDA', 'Grama Bermuda'),
        ('SANTO_AGOSTINHO', 'Grama Santo Agostinho'),
    ]
    
    nome = models.CharField('Nome da Grama', max_length=100)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPOS_GRAMA)
    preco_por_m2 = models.DecimalField('Preço por m²', max_digits=10, decimal_places=2)
    descricao = models.TextField('Descrição')
    imagem = models.ImageField('Imagem', upload_to='gramas/')
    disponivel = models.BooleanField('Disponível', default=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco_por_m2}/m²"
    
    class Meta:
        verbose_name = 'Grama'
        verbose_name_plural = 'Gramas'
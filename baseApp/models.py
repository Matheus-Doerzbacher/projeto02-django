from django.db import models

from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField("Data de Criação", auto_now_add=True)
    modificado = models.DateField("Data de Modificação", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preco", decimal_places=2, max_digits=8)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField(
        "Imagem", upload_to="produtos", variations={"thumb": (124, 124)}
    )
    slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(sigal, instance, sender, **kwargs):
    instance.slug = slugify(produto_pre_save, sender=Produto)

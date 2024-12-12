from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id) + '. ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '. ' + self.choice_text
    
class Cat(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Price(models.Model):
    time=models.CharField(max_length=50)
    close=models.FloatField()
    

class Box(models.Model):
    x=models.FloatField()
    y=models.FloatField() 
    z=models.FloatField()  
    pos_x=models.IntegerField()
    pos_y=models.IntegerField()
    pos_z=models.IntegerField()
    color=models.CharField(max_length=8)






class QRCode(models.Model):
    nome = models.CharField(max_length=100)
    link_menu = models.URLField()

    def __str__(self):
        return self.nome
    
    
class Ordine(models.Model):
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name="ordini")
    data_creazione = models.DateTimeField(auto_now_add=True)
    dettagli = models.TextField()

    def __str__(self):
        return f"Ordine {self.id} - QR {self.qr_code.nome}"
    


class Tipologia(models.Model):

    tipo = models.CharField(max_length=20)
    immagine = models.ImageField(upload_to="tipologia/")

    def __str__(self):
        return self.tipo


class Portata(models.Model):
    
    tipologia = models.ForeignKey("Tipologia", on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    immagine = models.ImageField(upload_to="portate/")
    ingredienti = models.CharField(max_length=20)
    allergeni = models.CharField(max_length=20)
    disponibilita = models.BooleanField(default=True)
    prezzo = models.FloatField()

    def __str__(self):
        return self.nome

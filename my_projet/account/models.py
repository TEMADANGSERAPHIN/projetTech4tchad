from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    sujet = models.CharField(max_length=150)
    message = models.TextField(max_length=1500)
    def __str__(self):
        return self.nom
    

    
class Reservation(models.Model):
    service = (
    ('VOYAGE', ('VOYAGE')),
    ('BAGAGE', ('BAGAGE')),
    )
    Agence = (
    ('STTL', ('STTL')),
    ('ABOU ISLAM', ('ABOU ISLAM')),
    ('ABOU HAMMA', ('ABOU HAMAMA')),
    ('SUD VOYAGE', ('SUD VOYAGE')),
    ('ABROUM VOYAGE', ('ABROUM VOYAGE')),
      
    )
    ville_depart = models.CharField(max_length=200)
    ville_arrive = models.CharField(max_length=200)
    agences = models.CharField(max_length=200, choices=Agence, null=False, blank=False, default=None)
    type = models.CharField(max_length=32, choices=service)
    nombre_services = models.CharField(max_length=200, null=False, blank=False, default=None)
    date = models.DateTimeField('date du jour')
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    somme_paye = models.CharField(max_length=100, null=False, blank=False, default=None)
    details = models.TextField(max_length=100)
    def __str__(self):
        return self.nom

class PayeTel(models.Model):
    service = (
    ('VOYAGE', ('VOYAGE')),
    ('BAGAGE', ('BAGAGE')),
    
    )
    Agence = (
    ('STTL', ('STTL')),
    ('ABOU ISLAM', ('ABOU ISLAM')),
    ('ABOU HAMMA', ('ABOU HAMAMA')),
    ('SUD VOYAGE', ('SUD VOYAGE')),
    ('ABROUM VOYAGE', ('ABROUM VOYAGE')),
      
    )
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    somme = models.CharField(max_length=100, null=False, blank=False, default=None)
    agences=models.CharField(max_length=200, choices=Agence, null=False, blank=False, default=None )
    service = models.CharField(max_length=111, choices=service)
    destination = models.CharField(max_length=100)
    telephone = models.CharField(max_length=200)
    def __str__(self):
        return self.telephone

class PayeAgence(models.Model):
    service = (
    ('VOYAGE', ('VOYAGE')),
    ('BAGAGE', ('BAGAGE')),
   
    )
    Agence = (
    ('STTL', ('STTL')),
    ('ABOU ISLAM', ('ABOU ISLAM')),
    ('ABOU HAMMA', ('ABOU HAMAMA')),
    ('SUD VOYAGE', ('SUD VOYAGE')),
    ('ABROUM VOYAGE', ('ABROUM VOYAGE')),
      
    )
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    somme = models.CharField(max_length=200, null=False, blank=False, default=None)
    agences=models.CharField(max_length=200, choices=Agence, null=False, blank=False, default=None )
    service = models.CharField(max_length=111, choices=service)
    destination = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nom 
    
class PayeBan(models.Model):
    service = (
    ('VOYAGE', ('VOYAGE')),
    ('BAGAGE', ('BAGAGE')),

    )
    Agence = (
    ('STTL', ('STTL')),
    ('ABOU ISLAM', ('ABOU ISLAM')),
    ('ABOU HAMMA', ('ABOU HAMAMA')),
    ('SUD VOYAGE', ('SUD VOYAGE')),
    ('ABROUM VOYAGE', ('ABROUM VOYAGE')),
      
    )
    nom = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    agences=models.CharField(max_length=200, choices=Agence , null=False, blank=False, default=None)
    somme = models.CharField(max_length=200, null=False, blank=False, default=None)
    service = models.CharField(max_length=111, choices=service)
    destination = models.CharField(max_length=100)
    banque = models.CharField(max_length=200)
    
    def __str__(self):
        return self.banque

class Camion(models.Model):
    marque=models.TextField(max_length=100)
    plaque=models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.plaque

class Chauffer(models.Model):
    nom=models.CharField(max_length=150)
    matricule=models.CharField(max_length=200)
    camion= models.ForeignKey(Camion, on_delete=models.CASCADE )

    def __str__(self):
        return self.nom

class Agence(models.Model):
    nom=models.CharField(max_length=200)
    reservation=models.ForeignKey(Reservation, on_delete=models.CASCADE)
    chauffer = models.ForeignKey(Chauffer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom

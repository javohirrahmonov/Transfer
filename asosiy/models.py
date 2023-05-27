from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    logo= models.FileField()
    prezident = models.CharField(max_length=50,blank=True)
    murabbiy = models.CharField(max_length=100,blank= True)
    yil = models.DateField()
    eng_qimmat_sotuv = models.CharField(max_length= 200)
    eng_qimmat_tr= models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=150)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    t_yil = models.DateField()
    tr_narx = models.PositiveSmallIntegerField()
    pozitsiya = models.CharField(max_length=150)
    davlat = models.CharField(max_length=150 , blank=True)
    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    eski = models.ForeignKey(Club,on_delete=models.CASCADE, related_name="sotganlari")
    yangi = models.ForeignKey(Club,on_delete=models.CASCADE)
    tr_nax = models.PositiveSmallIntegerField()
    tahmn_narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=6)

class HozirgiMavsum(models.Model):
    mavsum = models.CharField(max_length=6)
    def __str__(self):
        return self.mavsum
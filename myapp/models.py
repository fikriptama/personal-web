from django.db import models


# Create your models here.
class todoList(models.Model): #models.model tell we want to make database model
    nama = models.CharField(max_length=200) # type database kalo int pakai IntField we store in our database
    
    def __str__(self):
        return self.nama
    

class item(models.Model):
    todo = models.ForeignKey(todoList, on_delete=models.CASCADE) #foreignkey untuk mendifiniskan class todoList yang kita buat diawal if on_dlelet hapus data ini juga jika data awal todoList dihapus
    text = models.CharField(max_length=300)
    complate = models.BooleanField()
    
    def __str__(self):
        return self.text
    
    
class fitur:
    fiturapp = str
    nama: str
    project: str
    about: str
    bahasa: list
    id: int
    
class experience(models.Model):
    tahun = models.IntegerField()
    posisi = models.CharField(max_length=50)
    di = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    cerita = models.CharField(max_length=200)
    show = models.BooleanField(default=False)
    
class education(models.Model):
    tahun = models.IntegerField()
    universitas = models.CharField(max_length=50)
    cerita = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50)
    lulusan = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    is_true = models.BooleanField()
    
class databs(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pw = models.CharField(max_length=50)
    
    
class contact(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)
    sendat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nama} - {self.email}'
    
    
class project(models.Model):
    nama = models.CharField(max_length=50)
    desk = models.CharField(max_length=50)
    models.ImageField(null=True, blank=True, upload_to="images/")    

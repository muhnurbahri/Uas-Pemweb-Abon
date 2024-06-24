from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telpon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='artikel', blank=True, null=True)
   
    def _str_(self):
        return self.user.username
    class Meta:
        verbose_name_plural = "1. Biodata"
#One-to-One
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/')
##penjelasan##
#Biodata Model:
#Merepresentasikan data biodata pengguna dalam sistem.
#Terhubung dengan model pengguna bawaan Django (User) melalui relasi one-to-one menggunakan bidang user.
#Memiliki dua atribut tambahan, yaitu alamat untuk menyimpan alamat pengguna dan telpon untuk menyimpan nomor telepon. Kedua atribut ini dapat memiliki nilai kosong.
#Metode __str__ mengembalikan nama pengguna (username) dari objek User yang terkait.
#Employee dan EmployeeProfile Model:
#Employee merepresentasikan data karyawan dengan atribut name dan department.
#EmployeeProfile terhubung secara satu-satunya dengan Employee melalui relasi one-to-one menggunakan bidang employee.
#Memiliki atribut bio untuk menyimpan biodata karyawan dan photo untuk menyimpan foto profil karyawan.
    
#One-to-Many
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
##penjelasan##
#Model Author merepresentasikan penulis buku dengan atribut seperti name (nama) dan nationality (kewarganegaraan). 
#Model Book merepresentasikan buku dengan atribut seperti title (judul), author (penulis), dan publication_date (tanggal publikasi).
#Hubungan antara Author dan Book adalah One-to-Many, yang berarti satu penulis dapat memiliki banyak buku (One-to-Many). 
#Ini ditunjukkan oleh field author pada model Book yang merupakan ForeignKey yang menghubungkan setiap buku ke satu penulis. 
#Ketika instance penulis dihapus, semua buku yang terkait dengan penulis tersebut juga dihapus (dengan on_delete=models.CASCADE).

    
#Many-to-Many
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
##penjelasan##
#Model Tag merepresentasikan tag atau label yang dapat diberikan pada artikel. Setiap tag memiliki atribut name (nama).
#Model Article merepresentasikan artikel dengan atribut seperti title (judul) dan content (konten). 
#Artikel dapat memiliki banyak tag, dan sebaliknya, satu tag dapat diberikan pada banyak artikel. 
#Hubungan antara Article dan Tag adalah Many-to-Many, yang ditunjukkan oleh field tags pada model Article. 
#Ini memungkinkan artikel untuk terhubung dengan banyak tag melalui tabel relasi Many-to-Many yang diciptakan secara otomatis oleh Django.

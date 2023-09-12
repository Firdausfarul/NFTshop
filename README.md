

## 1. Step by step pengerjaan

*Checklist* untuk tugas ini adalah sebagai berikut.

- [x] Membuat sebuah proyek Django baru.
 
    Selesai dengan menjalankan perintah `django-admin startproject NFTshop` di terminal

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

    Selesai dengan masuk ke folder `NFTshop` baru dan menjalankan perintah `python manage.py startapp main` di terminal

- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

    Menambahkan `path('main/', include('main.urls')),` ke list `urlpatterns` pada `NFTshop/urls.py` hal ini dilakukan untuk menambahkan subdirektori `main` pada web.


- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.

    Selesai dengan menambahkan kode berikut pada `main/models.py`
    ```python
    from django.db import models
    class Item(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
        img = models.TextField()
        emoji = models.CharField(max_length=255)
        country = models.CharField(max_length=255)
        continent = models.CharField(max_length=255)
        price = models.IntegerField()
    ```
    Snippet diatas digunakan untuk membuat model `Item` yang memiliki atribut `name`, `amount`, dan `description` dengan tipe data yang sesuai, serta atribut pelengkap lain.

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

- [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

    Membuat file baru `main/urls.py` dengan isi sebagai berikut:
    ```python
    from django.urls import path
    from main.views import show_main
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Snippet ini dilakukan untuk menambahkan routing ke aplikasi `main` yang akan menjalankan fungsi `show_main` pada `main/views.py` ketika subdirektori main diakses

- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Repo sudah dideploy dengan command `python manage.py migrate && gunicorn NFTshop.wsgi`
    dan dapat diakses pada `nftshop.adaptable.app/main/`

- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

## 2. Kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`


## 3. Tujuan penggunaan Virtual Environment
Tujuan utama digunakannya ***Virtual Environment*** adalah untuk mengisolasi lingkungan Python masing2 proyek. Hal ini dilakukan untuk menghindari konflik antar proyek yang menggunakan versi Python atau versi library yang berbeda.

Misalkan proyek A membutuhkan dependency library X versi 1.0, sedangkan proyek B membutuhkan dependency library X versi 2.0. 
Kita harus membuat virtual environment untuk setidaknya salah satu proyek tersebut agar tidak ada konflik dependency apabila kita ingin menjalankan kedua proyek tersebut secara berbarengan mengingat python [Tidak bisa memiliki 2 versi library yang sama dalam satu environment](https://stackoverflow.com/questions/48332046/does-pip-python-support-multiple-versions-of-the-same-package). 

Selain itu dengan penggunaan virtual environment, proyek kita akan lebih mudah direplikasi di mesin lain karena kita hanya perlu mengirimkan file `requirements.txt` yang berisi daftar dependency yang dibutuhkan oleh proyek tersebut. Hal ini akan sangat berguna ketika kita berkolaborasi dalam sebuah proyek, seperti ketika tugas kelompok nanti.

Kita tetap bisa membuat aplikasi Django tanpa virtual environment, namun hal ini tidak disarankan karena hal ini akan mempersulit kolaborasi serta dapat mengakibatkan konflik dependency seperti yang dicontohkan dengan hal yang dijelaskan diatas.

# 4. MVC, MVT, MVVM dan perbedaannya
- MVC, MVT, MVVM adalah pola desain arsitektur perangkat lunak. Perbedaannya:

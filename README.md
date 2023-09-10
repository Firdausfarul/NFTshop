## Checklist Tugas

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

- [ ] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [ ] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Perhatikan bahwa kamu harus mengerjakan tugas ini menggunakan repositori yang **berbeda** dengan tutorial, sehingga pastikan kamu **membuat repositori baru** untuk tugas ini.
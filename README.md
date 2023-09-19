# Tugas 2

## 1. Step by step pengerjaan

*Checklist* untuk tugas ini adalah sebagai berikut.

- [x] Membuat sebuah proyek Django baru.
 
    Menjalankan perintah `django-admin startproject NFTshop` di terminal

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

    Masuk ke folder `NFTshop` baru dan menjalankan perintah `python manage.py startapp main` di terminal

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

    Menambahkan fungsi `show_main` pada `main/views.py` dengan kode berikut:
    ```python
    from django.shortcuts import render
    from random import randint
    from requests import get

    def show_main(request):
        context = reqnft()
        return render(request, "main.html", context)
    ```
    Fungsi ini akan mengambil data/context dari fungsi `reqnft` yang akan mengembalikan context yang relevan, lalu memasukkan data tersebut ke dalam template `main.html` lalu merendernya. 

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

## 2. Kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`
![Bagan](https://github.com/Firdausfarul/Intft_stellar/blob/c054585a66a5f9fdba9306d904f4b64b58cbe6a9/image_2023-09-13_112035326.png)

1. Request akan masuk ke urls.py menentukan mana program/fungsi yang akan dijalankan berdasarkan request pengguna/url yang diakses.

2. Fungsi yang dipanggil akan mengambil data dari models.py dan memasukkannya ke dalam context.

3. Model akan mengedit/mengambil data dari database dan mengembalikannya ke fungsi.

4. Fungsi akan memasukkan data yang diterima dari model ke dalam template html.

5. Template html akan dirender oleh views.py mengembalikan html yang sudah dirender/dimasukin data.

    untuk aplikasi ini models.py belum bertransaksi dengan database. sehingga models.py hanya berfungsi sebagai menentukan database schema.

## 3. Tujuan penggunaan Virtual Environment
Tujuan utama digunakannya ***Virtual Environment*** adalah untuk mengisolasi lingkungan Python masing2 proyek. Hal ini dilakukan untuk menghindari konflik antar proyek yang menggunakan versi Python atau versi library yang berbeda.

Misalkan proyek A membutuhkan dependency library X versi 1.0, sedangkan proyek B membutuhkan dependency library X versi 2.0. 
Kita harus membuat virtual environment untuk setidaknya salah satu proyek tersebut agar tidak ada konflik dependency apabila kita ingin menjalankan kedua proyek tersebut secara berbarengan mengingat python [Tidak bisa memiliki 2 versi library yang sama dalam satu environment](https://stackoverflow.com/questions/48332046/does-pip-python-support-multiple-versions-of-the-same-package). 

Selain itu dengan penggunaan virtual environment, proyek kita akan lebih mudah direplikasi di mesin lain karena kita hanya perlu mengirimkan file `requirements.txt` yang berisi daftar dependency yang dibutuhkan oleh proyek tersebut. Hal ini akan sangat berguna ketika kita berkolaborasi dalam sebuah proyek, seperti ketika tugas kelompok nanti.

Kita tetap bisa membuat aplikasi Django tanpa virtual environment, namun hal ini tidak disarankan karena hal ini akan mempersulit kolaborasi serta dapat mengakibatkan konflik dependency seperti yang dicontohkan dengan hal yang dijelaskan diatas.

# 4. MVC, MVT, MVVM dan perbedaannya
MVC, MVT, dan MVVM adalah tiga pola desain arsitektur yang digunakan dalam pengembangan *software*.

1. MVC (Model-View-Controller):
 
     Pola desain yang memisahkan aplikasi menjadi tiga komponen interaktif utama : 
      - Model adalah bagian aplikasi yang menangani logika bisnis dan data. 
      - View adalah bagian yang menangani penampilan data kepada pengguna. 
      - Controller adalah bagian yang menghubungkan model dan view. 
      
      Pengguna berinteraksi dengan Controller, Contoller berinteraksi dengan Model untuk mengambil data, dan data tersebut kemudian ditampilkan kepada pengguna melalui View. 

2. MVT (Model-View-Template): 

    Modifikasi dari pola MVC. Dalam MVT, 
    - Model bertugas sebagai interface ke database dan mengelola data.
    - Logika bisnis pada MVT ditempatkan pada View
    - View bertugas untuk mengambil data dari Model dan merendernya dengan Template.
    - Template hanya bertugas sebagai kerangka/template untuk menampilkan data yang sudah dikumpulkan oleh View.

    MVT digunakan oleh Django.

3. MVVM (Model-View-ViewModel):

     Pola desain yang digunakan dalam pada Angular dan KnockoutJS. Dalam MVVM, ViewModel bertindak sebagai penghubung antara Model dan View. ViewModel befungsi untuk memperbarui View ketika ada request perubahan dari Model ataupun sebaliknya.

Perbedaan utama antara ketiganya terletak pada bagaimana mereka memisahkan tugas dalam aplikasi.
 MVC memisahkan aplikasi menjadi logika bisnis (Model), tampilan pengguna (View), dan pengendali yang menghubungkan dua yang pertama (Controller). MVT mirip MVC, tapi tugas merespon ke request dan logika bisnis dihandle oleh View, Template hanya sebagai kerangka untuk menampilkan data. Sedangkan MVVM menggunakan ViewModel sebagai penghubung antara Model dan View, ViewModel memungkinkan perubahan otomatis antara Model dan View, cocok untuk aplikasi web yang dinamis.

 ---
 # Tugas 3
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
# 1. Apa perbedaan antara form POST dan form GET dalam Django?

- GET mempunyai limit payload size yang relatif kecil dibanding POST

- GET umumnya digunakan untuk mengambil data dari server, dan tidak berefek/mengubah database. POST umumny digunakan untuk mengirim data ke server, dan berefek/mengubah database.

- GET dapat di-bookmark karena payload berada di URL itu sendiri, sehingga dapat diakses kembali dengan mudah, sehingga tidak cocok untuk mengirim data sensitif. POST tidak dapat di-bookmark, data berada di payload http request sehingga lebih cocok untuk mengirim data sensitif seperti password.

# 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- HTML bertujuan utama untuk menampilkan data sehingga, sedangkan XML dan JSON bertujuan utama untuk mengirim/menyimpan data.

- HTML lebih berorientasi kepada User Interface sedangkan XML dan JSON lebih berorientasi kepada data.

- JSON mempunyai native support di Javascript, sedangkan XML tidak. Sehingga membuatnya relatif lebih ringan dan cepat untuk diproses pada browser.

- JSON memiliki struktur key-value yang sederhana, sehingga lebih mudah dibaca manusia dibanding XML yang berstruktur tree yang lebih kompleks.



# 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON mempunyai native support di Javascript, sehingga parsingnya lebih ringan dan cepat untuk diproses pada browser dibanding XML.

- Struktur key-value yang sederhana membuatnya lebih mudah dibaca dan di-edit manusia.

- Ukuran JSON yang relatif kecil membuatnya lebih efisien untuk ditransfer melalui jaringan.

- JSON lebih simple dan fleksibel dibanding XML.

# 4.Step By Step

- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

1. Menginisialisasi form pada `main/forms.py` dengan format seperti tutorial

2. Menambahkan templat `base.html` pada `/templates` folder dengan format seperti tutorial serta menambahkan path template tersebut di `settings.py` pada folder `NFTshop`.

3. Menambahkan fungsi `create_product` yang menghandle form pada `main/views.py` dengan format seperti tutorial.

4. Menambahkan template `create_product.html` di `main/templates` sesuai tutorial.

5. Menambahkan path untuk `create_product` pada `main/urls.py` sesuai tutorial.

6. Menambahkan akses ke `create_product` pada `main.html` dengan button seperti tutorial.

- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

- Dilakukan dengan mengambil data dari database sesuai dengan ID yang diberikan atau semua data jika ID tidak diberikan lalu menserialisasinya ke format yang sesuai dan mengembalikannya ke User. Untuk HTML data akan dirender sesuai dengan template html pada `main/templates`.

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

- Menghubungkan path dengan fungsi yang relevan pada `main/urls.py` dengan format seperti tutorial.

# 5. Postman SS
**1. HTML**

![Postman](https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/image_2023-09-20_052047083.png)

**2. XML**

![Postman](https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/image_2023-09-20_052002792.png)

**3. XML by ID**

![Postman](https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/image_2023-09-20_052020305.png)

**4. JSON**

![Postman](https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/image_2023-09-20_051944319.png)

**5. JSON by ID**

![Postman](https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/image_2023-09-20_051907377.png)

---

# Tugas 4

1. **Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?**
    
    Django UserCreationForm adalah class/form yang sudah disediakan Django untuk mempermudah proses pembuatan akun baru/registrasi.  Kelebihannya adalah lebih praktis, developer tidak perlu membuat sistem registrasi dari awal, cukup mengimport UserCreationForm dari Django dan menggunakannya. Kekurangannya adalah UserCreationForm kurang fleksibel, kita tidak bisa mengubah tampilan form dengan bebas, hanya bisa dengan bawaan django.

2.  **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

    Autentikasi dalam konteks Django adalah proses verifikasi identitas pengguna, seperti proses login. Sementara otorisasi adalah proses menentukan apa yang bisa dilakukan pengguna setelah mereka terautentikasi, seperti akses ke halaman tertentu atau melakukan tindakan tertentu. Contohnya pengguna hanya bisa menghapus item yang dibuatnya sendiri, tidak bisa menghapus item yang dibuat orang lain. Keduanya penting untuk memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses dan berinteraksi dengan aplikasi web.

3. **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

    Cookies dalam konteks aplikasi web adalah data yang disimpan di browser pengguna oleh situs web. Django menggunakan cookies untuk mengelola data sesi pengguna, seperti informasi login, siapa user yang saat ini login. Cookies juga memungkinkan Django untuk 'mengingat' pilihan/informasi mengenai pengguna dan menyediakan pengalaman yang lebih dipersonalisasi.

4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

    Penggunaan cookies secara umum dianggap aman, tetapi ada beberapa risiko yang harus diwaspadai. Misalnya, cookies dapat disalahgunakan oleh pihak ketiga untuk melacak aktivitas online pengguna tanpa sepengetahuan mereka. Selain itu, jika ada kemungkinan cookies pengguna dicuri melalui Cross Site Scripting(XSS). Apabila yang dicuri adalah cookies yang berisi informasi login/session maka perettas bisa berpura-pura menjadi user yang cookiesnya dicuri. Oleh karena itu, penting untuk selalu menggunakan enkripsi dan *best practices* keamanan lainnya saat bekerja dengan cookies.

5.  **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    - membuat fungsi `register`, `login_user`, `logout_user` di `main/views.py` dengan memanfaatkan framework Django (Seperti di Tutorial)
    - Menyambungkan fungsi-fungsi tersebut ke path yang relevan di `main/urls.py` 

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    - ![Gambar](https://github.com/Firdausfarul/Intft_stellar/blob/main/image_2023-09-26_124033288.png?raw=true)
    - ![Gambar](https://github.com/Firdausfarul/Intft_stellar/blob/main/image_2023-09-26_125159110.png?raw=true)

- [x] Menghubungkan model Item dengan User.

    - Menambahkan atribut User pada model Item dengan tipe ForeignKey untuk menghubungkan Item dengan User.
    - Make migration dan migrate untuk mengaplikasikan perubahan pada database.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    - Menambahkan cookies yang berisi last login
    - Menambahkan cookies tersebut ke context
    - Menambahkan template untuk mendisplay last login tersebut
    - Menambahkan User ke context untuk mendisplay username
    - Menambahkan template untuk mendisplay username 

---
# Tugas 5

## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. **Type Selector:** 

    Memilih semua elemen berdasarkan tipe elemennya (misalnya, p, div).

    Tepat digunakan ketika ingin menerapkan gaya yang sama ke semua elemen jenis yang sama.

2. **Class Selector:**
    
    Memilih elemen berdasarkan kelasnya (misalnya, .my-class).

    Tepat digunakan ketika ingin menerapkan gaya ke sekelompok elemen yang berbeda, tetapi membutuhkan gaya yang sama.

3. **ID Selector:**
    
    Memilih elemen berdasarkan ID-nya (misalnya, #my-id).

   Tepat digunakan ketika perlu menerapkan gaya ke elemen yang spesifik dan unik.

4. **Attribute Selector:**

    Memilih elemen berdasarkan atributnya (misalnya, [type="text"]).

    Tepat digunakan ketika ingin memilih elemen berdasarkan atributnya, bukan tipe, ID, atau kelas.

5. **Pseudo-class Selector:**
    Memilih elemen berdasarkan keadaannya (misalnya, :hover, :active).

    Tepat digunakan ketika ingin menerapkan gaya berdasarkan interaksi pengguna atau keadaan elemen.

6. **Pseudo-element Selector:** 
    
    Memilih bagian tertentu dari elemen (misalnya, ::before, ::after).

    Tepat digunakan ketika perlu memodifikasi atau menambah konten ke elemen tanpa mengubah HTML.


## 2. Jelaskan HTML5 Tag yang kamu ketahui.

### Struktur Dasar
1. `<html>`: Tag pembuka untuk dokumen HTML.
2. `<head>`: Berisi metadata dan informasi lain seperti judul dan tautan ke CSS atau file JS.
3. `<title>`: Menentukan judul halaman web yang akan muncul pada tab browser.
4. `<body>`: Berisi konten yang akan ditampilkan di browser.

### Berhubungan dengan teks
1. `<h1>, <h2>, ..., <h6>`: Digunakan untuk heading atau judul dengan berbagai tingkat.
2. `<p>`: Digunakan untuk paragraf teks.
3. `<strong>`: Digunakan untuk nge-bold teks.

### Tautan dan Gambar
1. `<a>`: Digunakan untuk membuat tautan.
2. `<img>`: Digunakan untuk menyisipkan gambar.

### List
1. `<ul>`: Digunakan untuk membuat daftar tidak berurutan. (yang titik titik)
2. `<ol>`: Digunakan untuk membuat daftar berurutan. (yang pake angka)

### Form
1. `<form>`: Digunakan untuk membuat form.
2. `<input>`: Digunakan untuk elemen input seperti teks, radio button, dan lain-lain.
3. `<button>`: Digunakan untuk membuat tombol.

### Layout
1. `<div>`: Digunakan untuk pembagian bagian/membuat bagian baru pada halaman web.
2. `<header>`, `<footer>`, `<main>`, `<section>`, `<article>`, `<aside>`: Digunakan untuk layout semantik, mempermudah pembacaan struktur halaman oleh mesin seperti web crawler dan manusia.

## 3. Jelaskan perbedaan antara margin dan padding.
![marginpadding](https://cdn-images-1.medium.com/v2/resize:fit:1200/1*xOn6MsNhUcju7Did367ssQ.jpeg)

- Margin adalah Jarak antara elemen dengan elemen lainnya di sekitarnya.

- Padding adalah Jarak antara konten elemen dengan batas elemennya.

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

- Bootstrap lebih berorientasi pada komponen, sudah menyediakan banyak elemen UI **siap pakai**.

- Tailwind lebih berfokus pada utilitas, memungkinkan untuk membangun desain dari awal dengan lebih cepat. 

Gunakan bootstrap ketika :
- Butuh banyak komponen UI yang sudah siap pakai.

- Ketika kita lebih suka mendeklarasikan gaya dalam HTML menggunakan kelas yang lebih semantik.

- Butuh waktu pengembangan yang lebih cepat, karena bootstrap sudah menyediakan banyak komponen UI yang siap pakai dan lebih sederhana. 

Gunakan Tailwind ketika :

- Ingin kontrol lebih atas desain.

- Ingin mengkustomisasi desain karena tailwind lebih fleksibel.

- Ketika kita Lebih suka mendeklarasikan gaya langsung di elemen/in-line, tanpa perlu menulis CSS ekstra.

## 5. Step by Step

- [x]  Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.

    Menandai indeks item keberapa yang ada di row akhir / diberi warna berbeda dan mengirimnya melalui context (berada di `views.py` karena di template django sulit untuk menghitungnya), lalu pada template kita beri percabangan / if untuk menambahkan class `last-row` pada item di row akhir. (if menggunakan context yang dikirim untuk menentukan item keberapa yang diberi warna berbeda)

- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card

    Membuat div baru untuk semua detail `Item` dan styling div tersebut menggunakan css yang ada di class `item-container`. Semua item nanti akan ditampilkan dalam div baru yaitu `grid-container` untuk menampilkan item dalam bentuk grid dengan lebar 3.

- [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

    Menggunakan CSS untuk styling sebagus mungkin. Menyatukan beberapa item ke div baru dan memberi border ke div tersebut agar batas dari elemen terlihat jelas. Selain itu saya juga mengganti dan mengadjust warna dan ukuran beberapa elemen agar lebih bagus dipandang. Saya juga mencoba mengaplikasikan styling pseudo-class hover pada button agar tampilan button berubah sedikit ketika user menghover mousenya ke button. 

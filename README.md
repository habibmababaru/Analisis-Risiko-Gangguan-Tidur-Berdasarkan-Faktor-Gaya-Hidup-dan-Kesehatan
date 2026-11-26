# Program Analisis Risiko Gangguan Tidur Berdasarkan Faktor Gaya Hidup dan Kesehatan

Program berbasis Python yang berfungsi sebagai alat pemeriksaan awal (Screening) untuk menganalisis dan memeriksa kondisi kesehatan tidur seseorang berdasarkan berbagai faktor kesehatan dan gaya hidup menggunakan Sistem Pembobotan Poin (Scoring System).

---

## Daftar Isi

1. [Latar Belakang](#latar-belakang)
2. [Tujuan Program](#tujuan-program)
3. [Fitur Program](#fitur-program)
4. [Penggunaan Dataset](#penggunaan-dataset)
5. [Metodologi Klasifikasi](#metodologi-klasifikasi)
6. [Struktur Repositori](#struktur-repositori)
7. [Persyaratan Sistem](#persyaratan-sistem)
8. [Instalasi dan Cara Menjalankan Program](#instalasi-dan-cara-menjalankan-program)
9. [Panduan Penggunaan](#panduan-penggunaan)
10. [Validasi Data](#validasi-data)
11. [Keterbatasan Program](#keterbatasan-program)

---

## Latar Belakang

Tidur merupakan salah satu kebutuhan dasar manusia yang memiliki peran penting dalam menjaga kesehatan fisik maupun mental. Kualitas dan durasi tidur yang tidak sesuai dapat memengaruhi kondisi kesehatan serta aktivitas sehari-hari. Gangguan tidur seperti *Insomnia* dan *Sleep Apnea* merupakan beberapa kondisi yang dapat mengganggu kualitas tidur seseorang. Berbagai faktor, seperti usia, durasi tidur, tingkat stres, aktivitas fisik, indeks massa tubuh (BMI), dan tekanan darah, dapat berkaitan dengan kondisi kesehatan tidur.

Berdasarkan permasalahan tersebut, dikembangkan sebuah program berbasis Python yang bertujuan untuk mengolah data kesehatan dan gaya hidup guna mengidentifikasi kemungkinan gangguan tidur melalui sistem pembobotan poin (*Scoring System*). Program ini diharapkan dapat memberikan gambaran awal bagi pengguna seberapa besar risiko dirinya terdampak kondisi gangguan tidur berdasarkan faktor kesehatan dan gaya hidupnya.

## Tujuan Program

Tujuan pengembangan program ini adalah:

1. Mengolah data kesehatan dan gaya hidup berdasarkan variabel yang tersedia.
2. Memeriksa validitas data sebelum dilakukan proses klasifikasi.
3. Menerapkan sistem pembobotan poin berdasarkan kriteria tertentu.
4. Mengidentifikasi kemungkinan kondisi gangguan tidur berdasarkan hasil perhitungan skor.
5. Menyediakan penyimpanan dan pengelolaan riwayat hasil klasifikasi.

## Fitur Program

Program ini memiliki beberapa fitur utama, yaitu:

| No. | Fitur | Keterangan |
|---|---|---|
| 1 | Registrasi dan Login | Pengguna membuat akun dan masuk menggunakannya. |
| 2 | Input Data | Memasukkan data kesehatan dan gaya hidup. |
| 3 | Sampel Data | Menampilkan data sampel yang telah ada sebelumnya |
| 4 | Filter Data | Mencari data tertentu di dalam seluruh data sampel. |
| 5 | Riwayat Pemeriksaan | Menyimpan dan menampilkan hasil pemeriksaan pengguna. |
| 6 | Pembaruan Data | Menambahkan data yang diinput pengguna ke dalam data sampel. |

## Penggunaan Dataset

Dataset yang digunakan dalam program ini adalah **Sleep Health and Lifestyle Dataset.CSV**.

Dataset tersebut memuat informasi mengenai kesehatan dan gaya hidup individu yang dapat digunakan untuk menganalisis faktor-faktor yang berkaitan dengan kondisi tidur.

### Variabel Dataset

| No. | Variabel | Keterangan |
|---|---|---|
| 1 | Person ID | Identitas individu |
| 2 | Gender | Jenis kelamin |
| 3 | Age | Usia individu |
| 4 | Sleep Duration | Durasi tidur |
| 5 | Sleep Quality | Kualitas tidur |
| 6 | Activity Level | Tingkat aktivitas fisik |
| 7 | Stress Level | Tingkat stres |
| 8 | BMI Category | Kategori indeks massa tubuh |
| 9 | Blood Pressure | Tekanan darah |
| 10 | Heart Rate | Denyut jantung |
| 11 | Daily Steps | Jumlah langkah harian |

## Metodologi Klasifikasi

### 1. Metode yang Digunakan

Program ini menggunakan metode pembobotan poin (*Scoring System*) untuk mengidentifikasi kemungkinan gangguan tidur berdasarkan beberapa variabel kesehatan dan gaya hidup.

Setiap variabel memiliki kriteria penilaian dan bobot tertentu. Poin diberikan berdasarkan kondisi data yang dimasukkan, kemudian dijumlahkan untuk memperoleh skor akhir.

### 2. Variabel Penilaian

Variabel yang digunakan dalam proses klasifikasi meliputi:

- Gender
- Age
- Sleep Duration
- Sleep Quality
- Stress Level
- Activity Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps

### 3. Perhitungan Skor

Secara umum, perhitungan skor dilakukan dengan menjumlahkan seluruh poin dari variabel yang digunakan.

Rumus umum:

**Skor Total = Poin Variabel 1 + Poin Variabel 2 + ... + Poin Variabel n**

Keterangan:

- Skor Total: jumlah keseluruhan poin.
- Poin Variabel: nilai yang diperoleh berdasarkan kriteria masing-masing variabel.
- n: jumlah variabel yang digunakan.

### 4. Penentuan Status Akhir

Setelah seluruh poin dijumlahkan, skor akhir digunakan untuk menentukan status klasifikasi gangguan tidur.

Kategori hasil klasifikasi meliputi:

| No. | Status | Keterangan |
|---|---|---|
| 1 | Normal | Tidak teridentifikasi adanya risiko gangguan tidur berdasarkan kriteria program. |
| 2 | Insomnia | Teridentifikasi risiko yang mengarah pada kategori Insomnia. |
| 3 | Sleep Apnea | Teridentifikasi risiko yang mengarah pada kategori Sleep Apnea. |
| 4 | Both | Teridentifikasi risiko yang sama besar mengarah pada kedua kategori. |

*Catatan: Kriteria, bobot, dan batas skor setiap kategori harus disesuaikan dengan implementasi algoritma yang digunakan dalam program.*

## Struktur Repositori

Berikut merupakan struktur direktori proyek:

```text
Mini-Project/
│
├── main program.py
├── Sleep_health_and_lifestyle_dataset.csv
├── akun.json
│
├── riwayat/
│   ├── riwayat_1.csv
│   ├── riwayat_2.csv
│   └── ...
│
└── test case/
    ├── csv reading.py
    ├── Sleep_health_and_lifestyle_dataset(rev).csv
    └── ...
```

Keterangan:

| File/Folder | Fungsi |
|---|---|
| main program.py | Program utama untuk menjalankan sistem. |
| Sleep_health_and_lifestyle_dataset.csv | Dataset kesehatan dan gaya hidup. |
| akun.json | Penyimpanan informasi akun pengguna. |
| riwayat/ | Direktori penyimpanan riwayat hasil program. |
| riwayat_x.csv | Penyimpanan riwayat pemeriksaan pengguna. |
| test case/ | Direktori pengujian program. |
| csv reading.py | Program untuk percobaan klasifikasi data. |
| Sleep_health_and_lifestyle_dataset(rev).csv | Dataset kesehatan dan gaya hidup yang telah dimodifikasi. |

*Catatan: File akun.json dan riwayat_x.csv akan otomatis dibuat oleh program saat pertama kali dijalankan.*

## Persyaratan Sistem
Untuk menjalankan program, diperlukan beberapa perangkat lunak berikut:

- Python 3.6
- Code Editor (Visual Studio Code atau sejenisnya)
- Terminal atau Command Prompt

Library Python yang digunakan perlu disesuaikan dengan modul yang diimpor pada program utama.

## Instalasi dan Cara Menjalankan Program

### 1. Clone Repositori

Unduh proyek menggunakan perintah berikut:

```bash
git clone https://github.com/habibmababaru/Mini-Project.git
```

### 2. Masuk ke Direktori Proyek

```bash
cd Mini-Project
```

### 3. Jalankan Program

```bash
python "main program.py"
```

## 9. PANDUAN PENGGUNAAN

Berikut merupakan tahapan umum penggunaan program:

1. Jalankan program melalui terminal.
2. Program akan menampilkan menu **Beranda**.
3. Pilih menu **Register** apabila belum memiliki akun.
4. Masukkan username dan password untuk membuat akun.
5. Masuk melalui menu **Login** menggunakan akun yang telah terdaftar.
6. Setelah berhasil masuk, program menampilkan **Menu Utama**.
   - Menu 1 - **Pengenalan Sleep Disorder**. Menampilkan penjelasan ringkas tentang Gangguan Tidur.
   - Menu 2 - **Data Sampel Sleep Disorder**. Menampilkan beberapa data sampel yang telah ada.
   - Menu 3 - **Pencarian Data Sampel**. Fitur pencarian data tertentu dari data sampel.
   - Menu 4 - **Skrining Mandiri**. Fitur pemeriksaan dengan datanya di input oleh pengguna.
   - Menu 5 - **Pembobotan Kategori**. Menampilkan cara penghitungan dalam program ini.
   - Menu 6 - **Riwayat Pemeriksaan Saya**. Fitur yang menampilkan riwayat pemeriksaan pengguna. 
   - Menu 7 - **Log Out**.

## Validasi Data

Validasi data dilakukan untuk memastikan bahwa data yang digunakan memenuhi ketentuan yang telah ditetapkan.

Beberapa aspek yang diperiksa meliputi:

- Kesesuaian tipe data.
- Kelengkapan data.
- Rentang nilai variabel numerik.
- Kesesuaian kategori data.
- Format penulisan tekanan darah.
- Konsistensi antarvariabel.

Data yang tidak memenuhi kriteria validasi tidak akan dilanjutkan ke proses klasifikasi.

## Keterbatasan Program

Program ini memiliki beberapa keterbatasan:

1. Hasil klasifikasi bergantung pada variabel dan kriteria pembobotan yang telah ditentukan.
2. Dataset yang digunakan memiliki keterbatasan dalam merepresentasikan seluruh kondisi kesehatan individu.
3. Sistem pembobotan poin tidak secara langsung menggambarkan hubungan sebab-akibat antarvariabel.
4. Hasil klasifikasi hanya memberikan indikasi berdasarkan kriteria program dan bukan diagnosis medis.

---

## PENGEMBANG

| No | Nama Lengkap | NIM |
|---|---|---|
| 1. | Nathania Diandra Asgul | 2610931015 |
| 2. | Kesya Febryani Manihuruk | 2610931035 |
| 3. | Habib Abdillah | 2610932038 |
| 4. | Embun Dinanti | 2610932050 |

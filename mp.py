#Mini Project Sleep Health and Lifestyle Dataset
import csv
import os
import re
from datetime import datetime
from getpass import getpass

file_csv = r"C:\Users\embun dinanti\Downloads\Sleep_health_and_lifestyle_dataset.csv"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_RIWAYAT = os.path.join(BASE_DIR, "riwayat")
BATAS_RISIKO = 5

kolom_wajib = [ 
    "gender", "age",
    "sleep_duration", 
    "sleep_quality", 
    "activity_level", 
    "stress_level", 
    "bmi_category", 
    "blood_pressure", 
    "heart_rate", 
    "daily_steps", 
    ]

KOLOM_RIWAYAT = [
    "tanggal", "gender", "age", "sleep_duration", "sleep_quality",
    "activity_level", "stress_level", "bmi_category", "blood_pressure",
    "heart_rate", "daily_steps", "total_skor_apnea", "total_skor_insomnia", "status",
    ]

data = []
skor_apnea = 0
skor_insomnia = 0
user_awal = {"admin": "admin123", "user": "user123"}
text1 = (
    "Gangguan Tidur (Sleep Disorder) adalah "
    )
text2 = (
    "Berikut penjelasan mengenai makna dari setiap kategori Sleep Disorder"
    "1. Normal == "
    "   Kategori ini"
    "2. Sleep Apnea == "
    "   Kategori ini"
    "3. Insomnia == "
    "   Kategori ini"
    "4. Both == "
    "   Kategori ini"
    )

#REGISTER & LOGIN
def username_valid(username):
    return re.fullmatch(r"[A-Za-z0-9_]{3,20}", username) is not None

def registrasi():
    print("\n===( Register )===")
    print("(kosongkan username lalu tekan Enter untuk membatalkan)")
    while True:
        username = input("Buat Username Baru (3-20 karakter: huruf, angka, _): ").strip().lower()
        if username == "":
            print("Register dibatalkan.")
            return
        if not username_valid(username):
            print("Username hanya boleh huruf, angka, dan _ (3-20 karakter).")
            continue
        if username in user_awal:
            print("Username sudah dipakai, pilih yang lain.")
            continue
        break

    while True:
        password = getpass("Buat Password (minimal 6 karakter): ")
        if len(password) < 6:
            print("Password minimal 6 karakter.")
            continue
        if password != getpass("Ulangi Password: "):
            print("Password tidak sama. Coba lagi.")
            continue
        break

    user_awal[username] = password
    print(f"Register berhasil! Silahkan Login dengan username '{username}'.")

def login():
    """Return username bila berhasil, None bila dibatalkan atau gagal 3 kali."""
    print("\n===( Login )===")
    print("(kosongkan username lalu tekan Enter untuk kembali ke Beranda)")
    for percobaan in range(1, 4):
        username = input("Masukkan username: ").strip().lower()
        if username == "":
            print("Login dibatalkan.")
            return None
        password = getpass("Masukkan password: ")
        if username in user_awal and user_awal[username] == password:
            print(f"Login berhasil! Selamat Datang, {username}")
            return username
        print(f"Username atau password salah! ({percobaan}/3)")
        print("Belum punya akun? Kosongkan username untuk kembali ke Beranda, lalu pilih 2. Register terlebih dahulu.")
    print("Terlalu banyak percobaan gagal. Kembali ke Beranda.")
    return None

# MENU
def menu_awal():
    print("\n===( Beranda )===")
    print("1. Log In")
    print("2. Register")
    print("3. Exit Program")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        username = login()
        if username is None:
            return menu_awal()
        return menu_utama(username)
    elif opsi == "2":
        registrasi()
        return menu_awal()
    elif opsi == "3":
        print("\nTerima kasih telah menggunakan sistem skrining risiko gangguan tidur!")
    else:
        print("\nMenu tidak tersedia!")
        return menu_awal()

def kembali_ke_menu(username):
    print("\n1. Back to Menu")
    opsi = input("Pilih menu yang tersedia: ").strip()
    while opsi != "1":
        print("Menu tidak tersedia!")
        opsi = input("\nPilih menu yang tersedia: ").strip()
    print("Kembali ke menu utama.")
    return menu_utama(username)

def menu_utama(username):
    print("\n=====( Menu Utama )=====")
    print(f"Pengguna: {username}")
    print("1. Mengenal Sleep Disorder")
    print("2. Data Sampel Sleep Disorder")
    print("3. Pencarian Data Sampel")
    print("4. Skrining Mandiri")
    print("5. Status Kategori")
    print("6. Riwayat Pemeriksaan Saya")
    print("7. Log Out")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("\n===( Sleep Disorder )===")
        print(text1)
        return kembali_ke_menu(username)
    elif opsi == "2":
        print("\n===( Data Sampel Sleep Disorder )===")
        return menu_data_sampel(username)
    elif opsi == "3":
        print("\n===( Pencarian Data Sampel )===")
        return menu_cari_data(username)
    elif opsi == "4":
        print("\n===( Skrining Mandiri )===")
        return menu_skrining(username)
    elif opsi == "5":
        print("\n===( Status Kategori )===")
        print(text2)
        return kembali_ke_menu(username)
    elif opsi == "6":
        print("\n===( Riwayat Pemeriksaan Saya )===")
        return menu_riwayat(username)
    elif opsi == "7":
        print(f"\n{username} berhasil Log Out. Kembali ke Beranda")
        return menu_awal()
    else:
        print("\nMenu tidak tersedia!")
        return menu_utama(username)

def menu_cari_data(username):
    print("Coming Soon")
    return kembali_ke_menu(username)

# VALIDASI & RULE-BASED SCORING 
def validasi_data(gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,heart_rate,daily_steps):
    if gender not in ["Male", "Female"]:
        return False
    if age < 0:
        return False
    if sleep_duration < 0:
        return False
    if sleep_quality < 0 or sleep_quality > 10:
        return False
    if activity_level < 0 or activity_level > 100:
        return False
    if stress_level < 0 or stress_level > 10:
        return False
    if bmi_category not in ["Normal", "Overweight", "Obese"]:
        return False
    if heart_rate < 20:
        return False
    if daily_steps < 0:
        return False
    else:
        return True

def klasifikasi_gender(gender):
    skor_apnea = 0
    skor_insomnia = 0
    if gender == "Male":
        skor_apnea += 2
        skor_insomnia += 0
    elif gender == "Female":
        skor_apnea += 0
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

def klasifikasi_age(age):
    skor_apnea = 0
    skor_insomnia = 0
    if age >= 50:
        skor_apnea += 3
        skor_insomnia += 1
    elif age >= 40:
        skor_apnea += 2
        skor_insomnia += 1
    elif age >= 30:
        skor_apnea += 1
        skor_insomnia += 0
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_sleep_duration(sleep_duration):
    skor_apnea = 0
    skor_insomnia = 0
    if sleep_duration >= 9:
        skor_apnea += 1
        skor_insomnia += 0
    elif sleep_duration >= 7:
        skor_apnea += 0
        skor_insomnia += 0
    elif sleep_duration >= 6:
        skor_apnea += 1
        skor_insomnia += 2
    else:
        skor_apnea += 1
        skor_insomnia += 3
    return skor_apnea, skor_insomnia

def klasifikasi_sleep_quality(sleep_quality):
    skor_apnea = 0
    skor_insomnia = 0
    if sleep_quality >= 8:
        skor_apnea += 0
        skor_insomnia += 0
    elif sleep_quality >= 6:
        skor_apnea += 1
        skor_insomnia += 1
    elif sleep_quality >= 4:
        skor_apnea += 1
        skor_insomnia += 2
    else:
        skor_apnea += 1
        skor_insomnia += 3
    return skor_apnea, skor_insomnia

def klasifikasi_activity_level(activity_level):
    skor_apnea = 0
    skor_insomnia = 0
    if activity_level >= 30:
        skor_apnea += 0
        skor_insomnia += 0
    else:
        skor_apnea += 1
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

def klasifikasi_stress_level(stress_level):
    skor_apnea = 0
    skor_insomnia = 0
    if stress_level >= 7:
        skor_apnea += 0
        skor_insomnia += 3
    elif stress_level >= 4:
        skor_apnea += 0
        skor_insomnia += 1
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_bmi_category(bmi_category):
    skor_apnea = 0
    skor_insomnia = 0
    if bmi_category == "Normal":
        skor_apnea += 0
        skor_insomnia += 0
    elif bmi_category == "Overweight":
        skor_apnea += 2
        skor_insomnia += 0
    else:
        skor_apnea += 3
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_blood_pressure(blood_pressure):
    skor_apnea = 0
    skor_insomnia = 0
    sistolik, diastolik = map(int, blood_pressure.split('/'))
    if sistolik >= 140:
        skor_apnea += 3
        skor_insomnia += 0
    elif sistolik >= 130:
        skor_apnea += 2
        skor_insomnia += 0
    elif sistolik >= 120:
        skor_apnea += 1
        skor_insomnia += 0
    else:
        skor_apnea += 0
        skor_insomnia += 0
    if diastolik >= 100:
        skor_apnea += 3
        skor_insomnia += 0
    elif diastolik >= 90:
        skor_apnea += 2
        skor_insomnia += 0
    elif diastolik >= 80:
        skor_apnea += 1
        skor_insomnia += 0
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_heart_rate(heart_rate):
    skor_apnea = 0
    skor_insomnia = 0
    if heart_rate >= 100:
        skor_apnea += 1
        skor_insomnia += 1
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_daily_steps(daily_steps):
    skor_apnea = 0
    skor_insomnia = 0
    if daily_steps >= 5000:
        skor_apnea += 0
        skor_insomnia += 0
    else:
        skor_apnea += 1
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

def klasifikasi_status(total_skor_apnea,total_skor_insomnia,total_apnea,total_insomnia,total_both,total_normal):
    if total_skor_apnea >= 5 or total_skor_insomnia >= 5:
        if total_skor_apnea > total_skor_insomnia:
            status = "Sleep Apnea"
            total_apnea += 1
        elif total_skor_insomnia > total_skor_apnea:
            status = "Insomnia"
            total_insomnia += 1
        else:
            status = "Both"
            total_both += 1
    else:
        status = "Normal"
        total_normal += 1
    return status,total_apnea,total_insomnia,total_both,total_normal

def hitung_skor(d):
    semua_skor = [
        klasifikasi_gender(d["gender"]),
        klasifikasi_age(d["age"]),
        klasifikasi_sleep_duration(d["sleep_duration"]),
        klasifikasi_sleep_quality(d["sleep_quality"]),
        klasifikasi_activity_level(d["activity_level"]),
        klasifikasi_stress_level(d["stress_level"]),
        klasifikasi_bmi_category(d["bmi_category"]),
        klasifikasi_blood_pressure(d["blood_pressure"]),
        klasifikasi_heart_rate(d["heart_rate"]),
        klasifikasi_daily_steps(d["daily_steps"]),
    ]
    total_apnea = sum(skor[0] for skor in semua_skor)
    total_insomnia = sum(skor[1] for skor in semua_skor)
    return total_apnea, total_insomnia

# MENU 2: DATA SAMPEL (logika tidak diubah, hanya perbaikan agar bisa jalan)
def menu_data_sampel(username):
    data = []

    if not os.path.exists(file_csv):
        print("File CSV tidak Ditemukan")

    else:
        with open(file_csv, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for nomor_baris, row in enumerate(reader, start=2):
                try:
                    person_id = row["person_id"]
                    gender = row["gender"]
                    age = int(row["age"])
                    sleep_duration = float(row["sleep_duration"])
                    sleep_quality = int(row["sleep_quality"])
                    activity_level = int(row["activity_level"])
                    stress_level = int(row["stress_level"])
                    bmi_category = row["bmi_category"]
                    blood_pressure = row["blood_pressure"]
                    heart_rate = int(row["heart_rate"])
                    daily_steps = int(row["daily_steps"])
                except:
                    continue
                data.append(row)

            if len(data) == 0:
                print("\nDataset tidak valid!")          
            else:
                total_apnea = 0
                total_insomnia = 0
                total_both = 0
                total_normal = 0

                for row in data:
                    gender = row["gender"]
                    age = int(row["age"])
                    sleep_duration = float(row["sleep_duration"])
                    sleep_quality = int(row["sleep_quality"])
                    activity_level = int(row["activity_level"])
                    stress_level = int(row["stress_level"])
                    bmi_category = row["bmi_category"]
                    blood_pressure = row["blood_pressure"]
                    heart_rate = int(row["heart_rate"])
                    daily_steps = int(row["daily_steps"])

                    skor_gender = klasifikasi_gender(gender)
                    skor_age = klasifikasi_age(age)
                    skor_sleep_duration = klasifikasi_sleep_duration(sleep_duration)
                    skor_sleep_quality = klasifikasi_sleep_quality(sleep_quality)
                    skor_activity_level = klasifikasi_activity_level(activity_level)
                    skor_stress_level = klasifikasi_stress_level(stress_level)
                    skor_bmi_category = klasifikasi_bmi_category(bmi_category)
                    skor_blood_pressure = klasifikasi_blood_pressure(blood_pressure)
                    skor_heart_rate = klasifikasi_heart_rate(heart_rate)
                    skor_daily_steps = klasifikasi_daily_steps(daily_steps)
                    
                    semua_skor = [skor_gender,skor_age,skor_sleep_duration,skor_sleep_quality,skor_activity_level,skor_stress_level,skor_bmi_category,skor_blood_pressure,skor_heart_rate,skor_daily_steps]
                    total_skor_apnea = sum(skor[0] for skor in semua_skor)
                    total_skor_insomnia = sum(skor[1] for skor in semua_skor)
                    status, total_apnea, total_insomnia, total_both, total_normal = klasifikasi_status(total_skor_apnea,total_skor_insomnia,total_apnea,total_insomnia,total_both,total_normal)
                    
                    row["total_skor_apnea"] = total_skor_apnea
                    row["total_skor_insomnia"] = total_skor_insomnia
                    row["status"] = status
                
                persentase_apnea = (total_apnea / len(data)) * 100
                persentase_insomnia = (total_insomnia / len(data)) * 100
                persentase_both = (total_both / len(data)) * 100
                persentase_normal = (total_normal / len(data)) * 100

                print("[TABEL SAMPEL RISIKO SLEEP DISORDER]")
                print("=" * 179)
                print(f"|{'No':<4}|{'Person ID':<10}|{'Gender':<6}|{'Age':<3}|{'Sleep Duration':<14}|{'Sleep Quality':<13}|{'Activity Level':<14}|{'Stress Level':<12}|{'BMI Category':<12}|{'Blood Pressure':<15}|{'Heart Rate':<10}|{'Daily Steps':<11}|{'Total Apnea':<12}|{'Total Insomnia':<15}|{'Status':<12}|")
                print("=" * 179)
                for nomor, row in enumerate(data, start=1):
                    print(f"|{nomor:<4}|{row['person_id']:<10}|{row['gender']:<6}|{row['age']:<3}|{row['sleep_duration']:<14}|{row['sleep_quality']:<13}|{row['activity_level']:<14}|{row['stress_level']:<12}|{row['bmi_category']:<12}|{row['blood_pressure']:<15}|{row['heart_rate']:<10}|{row['daily_steps']:<11}|{row['total_skor_apnea']:<12}|{row['total_skor_insomnia']:<15}|{row['status']:<12}|")
                print("=" * 179)
                print("\n[RINGKASAN TABEL SAMPEL]")
                print(f"Jumlah Data                 : {len(data)}")
                print(f"Jumlah Sleep Apnea          : {total_apnea}")
                print(f"Jumlah Insomnia             : {total_insomnia}")
                print(f"Jumlah Both                 : {total_both}")
                print(f"Jumlah Normal               : {total_normal}")
                print(f"Persentase Sleep Apnea      : {persentase_apnea:.2f}%")
                print(f"Persentase Insomnia         : {persentase_insomnia:.2f}%")
                print(f"Persentase Both             : {persentase_both:.2f}%")
                print(f"Persentase Normal           : {persentase_normal:.2f}%")
    return kembali_ke_menu(username)

# MENU 4: SKRINING MANDIRI
def tekanan_darah_valid(teks):
    """Format harus sistolik/diastolik (contoh 120/80) dengan nilai masuk akal."""
    try:
        sistolik, diastolik = map(int, teks.split("/"))
    except ValueError:
        return False
    return 70 <= sistolik <= 250 and 40 <= diastolik <= 150 and sistolik > diastolik

def input_angka(pesan, tipe, minimum, maksimum):
    """Minta angka (int/float) sampai valid dan berada di rentang minimum-maksimum."""
    while True:
        teks = input(pesan).strip().replace(",", ".")
        try:
            nilai = tipe(teks)
        except ValueError:
            jenis = "bilangan bulat" if tipe is int else "angka"
            print(f"  Input harus berupa {jenis}. Coba lagi.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Nilai harus antara {minimum} dan {maksimum}. Coba lagi.")

def input_pilihan(judul, pilihan):
    """Tampilkan pilihan bernomor, kembalikan teks pilihan yang dipilih."""
    print(judul)
    for nomor, teks in enumerate(pilihan, start=1):
        print(f"  {nomor}. {teks}")
    nomor = input_angka("  Pilih nomor: ", int, 1, len(pilihan))
    return pilihan[nomor - 1]

def input_tekanan_darah():
    while True:
        teks = input("Tekanan darah (format sistolik/diastolik, contoh 120/80): ").strip()
        if tekanan_darah_valid(teks):
            sistolik, diastolik = teks.split("/")
            return f"{int(sistolik)}/{int(diastolik)}"
        print("  Format/nilai tidak valid. Contoh: 120/80 (sistolik 70-250, diastolik 40-150, sistolik > diastolik).")

def ambil_data_pengguna():
    print("Masukkan data pemeriksaanmu:")
    d = {}
    d["gender"] = input_pilihan("Jenis kelamin:", ["Male", "Female"])
    d["age"] = input_angka("Usia (tahun): ", int, 1, 120)
    d["sleep_duration"] = input_angka("Durasi tidur per malam (jam, contoh 6.5): ", float, 0, 24)
    d["sleep_quality"] = input_angka("Kualitas tidur (1-10): ", int, 1, 10)
    d["activity_level"] = input_angka("Aktivitas fisik per hari (menit, 0-100): ", int, 0, 100)
    d["stress_level"] = input_angka("Tingkat stres (1-10): ", int, 1, 10)
    d["bmi_category"] = input_pilihan("Kategori BMI:", ["Normal", "Overweight", "Obese"])
    d["blood_pressure"] = input_tekanan_darah()
    d["heart_rate"] = input_angka("Detak jantung istirahat (bpm): ", int, 30, 220)
    d["daily_steps"] = input_angka("Langkah harian: ", int, 0, 100000)
    return d

def buat_rekomendasi(d, status):
    sistolik, diastolik = map(int, d["blood_pressure"].split("/"))
    ada_apnea = status in ("Sleep Apnea", "Both")
    ada_insomnia = status in ("Insomnia", "Both")
    saran = []

    if status == "Normal":
        saran.append("Pertahankan pola tidur 7-9 jam dengan jam tidur dan bangun yang konsisten.")
        saran.append("Tetap aktif bergerak dan jaga berat badan serta tekanan darah dalam batas sehat.")

    if d["sleep_duration"] < 7:
        saran.append("Tambah durasi tidur menuju 7-9 jam per malam; tidur dan bangun di jam yang sama, termasuk akhir pekan.")
    if d["activity_level"] < 30:
        saran.append("Targetkan aktivitas fisik minimal 30 menit per hari (jalan cepat, bersepeda, olahraga ringan).")
    if d["daily_steps"] < 5000:
        saran.append("Naikkan langkah harian secara bertahap, misalnya tambah 1.000 langkah tiap minggu.")

    if ada_apnea:
        if d["bmi_category"] != "Normal":
            saran.append("Kelola berat badan lewat pola makan seimbang dan olahraga rutin; berat badan berlebih adalah faktor risiko sleep apnea.")
        if sistolik >= 130 or diastolik >= 80:
            saran.append("Pantau tekanan darah secara rutin, kurangi garam, dan konsultasikan bila tetap tinggi.")
        saran.append("Coba tidur miring dan hindari alkohol atau makan berat beberapa jam sebelum tidur.")
        saran.append("Bila kamu mendengkur keras, sering terbangun tersengal, atau sangat mengantuk di siang hari, periksakan ke dokter untuk evaluasi lebih lanjut.")

    if ada_insomnia:
        if d["stress_level"] >= 4:
            saran.append("Kelola stres: latihan pernapasan, meditasi, jurnal, atau ngobrol dengan orang terpercaya sebelum tidur.")
        saran.append("Hindari kafein di sore/malam hari dan kurangi layar gawai 1 jam sebelum tidur.")
        saran.append("Buat kamar tidur gelap, sejuk, dan tenang; bila tidak bisa tidur dalam sekitar 20 menit, bangun sebentar dan lakukan aktivitas santai.")
        saran.append("Bila sulit tidur terjadi hampir setiap malam selama berminggu-minggu, konsultasikan ke tenaga kesehatan.")

    if d["heart_rate"] >= 100:
        saran.append("Detak jantung istirahatmu tergolong tinggi; kurangi kafein dan periksakan ke dokter bila berlanjut.")

    return saran

def path_riwayat(username):
    aman = re.sub(r"[^A-Za-z0-9_-]", "_", username)
    return os.path.join(FOLDER_RIWAYAT, f"riwayat_{aman}.csv")

def simpan_riwayat(username, d, total_apnea, total_insomnia, status):
    os.makedirs(FOLDER_RIWAYAT, exist_ok=True)
    path = path_riwayat(username)
    file_baru = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=KOLOM_RIWAYAT)
        if file_baru:
            writer.writeheader()
        writer.writerow({
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **d,
            "total_skor_apnea": total_apnea,
            "total_skor_insomnia": total_insomnia,
            "status": status,
        })
    return path

def menu_skrining(username):
    d = ambil_data_pengguna()
    total_apnea, total_insomnia = hitung_skor(d)
    status = klasifikasi_status(total_apnea, total_insomnia, 0, 0, 0, 0)[0]

    print("\n[HASIL SKRINING]")
    print(f"Skor risiko Sleep Apnea : {total_apnea} (ambang batas {BATAS_RISIKO})")
    print(f"Skor risiko Insomnia    : {total_insomnia} (ambang batas {BATAS_RISIKO})")
    print(f"Status                  : {status}")

    print("\n[REKOMENDASI]")
    for nomor, teks in enumerate(buat_rekomendasi(d, status), start=1):
        print(f"{nomor}. {teks}")

    path = simpan_riwayat(username, d, total_apnea, total_insomnia, status)
    print(f"\nHasil pemeriksaan disimpan ke: {os.path.abspath(path)}")
    print("Catatan: hasil ini hanya skrining awal berbasis skor, bukan diagnosis medis.")
    return kembali_ke_menu(username)

# MENU 6: RIWAYAT PEMERIKSAAN SAYA
URUTAN_STATUS = {"Normal": 0, "Insomnia": 1, "Sleep Apnea": 1, "Both": 2}

def baca_riwayat(username):
    """Return list baris riwayat milik username (list kosong bila belum ada)."""
    path = path_riwayat(username)
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def menu_riwayat(username):
    riwayat = baca_riwayat(username)
    if len(riwayat) == 0:
        print("Belum ada riwayat pemeriksaan. Silakan lakukan Skrining Mandiri terlebih dahulu.")
        return kembali_ke_menu(username)

    kolom = [
        ("No", 4, None), ("Tanggal", 19, "tanggal"), ("Gender", 6, "gender"),
        ("Usia", 4, "age"), ("Durasi", 6, "sleep_duration"), ("Kualitas", 8, "sleep_quality"),
        ("Aktivitas", 9, "activity_level"), ("Stres", 5, "stress_level"),
        ("BMI", 10, "bmi_category"), ("Tekanan", 8, "blood_pressure"),
        ("Detak", 5, "heart_rate"), ("Langkah", 7, "daily_steps"),
        ("Apnea", 5, "total_skor_apnea"), ("Insomnia", 8, "total_skor_insomnia"),
        ("Status", 11, "status"),
    ]
    garis = "=" * (sum(lebar for _, lebar, _ in kolom) + len(kolom) + 1)

    print(f"[TABEL RIWAYAT PEMERIKSAAN: {username}]")
    print(garis)
    print("|" + "|".join(f"{judul:<{lebar}}" for judul, lebar, _ in kolom) + "|")
    print(garis)
    for nomor, baris in enumerate(riwayat, start=1):
        sel = [f"{nomor:<4}"]
        for _, lebar, nama in kolom[1:]:
            sel.append(f"{baris.get(nama, '-'):<{lebar}}")
        print("|" + "|".join(sel) + "|")
    print(garis)

    print(f"Jumlah pemeriksaan   : {len(riwayat)}")
    print(f"Status terbaru       : {riwayat[-1].get('status', '-')}")
    if len(riwayat) >= 2:
        sebelum = riwayat[-2].get("status", "-")
        sekarang = riwayat[-1].get("status", "-")
        if sebelum not in URUTAN_STATUS or sekarang not in URUTAN_STATUS:
            perubahan = "-"
        elif URUTAN_STATUS[sekarang] < URUTAN_STATUS[sebelum]:
            perubahan = f"membaik ({sebelum} -> {sekarang})"
        elif URUTAN_STATUS[sekarang] > URUTAN_STATUS[sebelum]:
            perubahan = f"memburuk ({sebelum} -> {sekarang})"
        else:
            perubahan = f"tetap ({sekarang})"
        print(f"Dibanding sebelumnya : {perubahan}")
    print("Catatan: hasil ini hanya skrining awal berbasis skor, bukan diagnosis medis.")
    return kembali_ke_menu(username)


if __name__ == "__main__":
    print("\n========( Sleep Disorder Risk Screening System )========")
    print("Selamat datang di sistem skrining risiko gangguan tidur!")    
    menu_awal()
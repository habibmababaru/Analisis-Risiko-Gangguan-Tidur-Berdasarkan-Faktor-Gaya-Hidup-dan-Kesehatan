#Mini Project Sleep Health and Lifestyle Dataset
import csv
import os
import re
import json
import hashlib
from datetime import datetime

file_csv = r"C:\Users\Admin\Downloads\Mini Project\Sleep_health_and_lifestyle_dataset(rev).csv"
kolom_wajib = [ 
    "gender", "age", "sleep_duration", "sleep_quality", 
    "activity_level", "stress_level", "bmi_category", 
    "blood_pressure", "heart_rate", "daily_steps", 
    ]
kolom_riwayat = [   
    "tanggal", "gender", "age", "sleep_duration", 
    "sleep_quality", "activity_level", "stress_level", 
    "bmi_category", "blood_pressure", "heart_rate", 
    "daily_steps", "total_skor_apnea", "total_skor_insomnia",
    "status_user"
    ]
urutan_status = {"Normal": 0, "Insomnia": 1, "Sleep Apnea": 1, "Both": 2}
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_riwayat = os.path.join(base_dir, "riwayat")
file_akun = os.path.join(base_dir, "akun.json")

data = []
skor_apnea = 0
skor_insomnia = 0
text1 = (
    "Gangguan Tidur (Sleep Disorder) adalah kelainan pada pola tidur seseorang. Kondisi ini dapat menurunkan kualitas tidur dan berdampak pada kesehatan secara keseluruhan." 
    "Gangguan tidur dapat menyebabkan kantuk di siang hari, sulit tidur di malam hari,  atau  memiliki pola tidur dan  bangun  yang  tidak  teratur. Tanpa  penanganan  yang" 
    "tepat, gangguan tidur dapat meningkatkan risiko terjadinya berbagai masalah kesehatan, seperti hipertensi dan penyakit jantung."
    )
text2 = (
    "Pembobotan Skor setiap variabel terhadap status akhir Sleep Disorder."
    "\nA. Gender    -->  Jenis kelamin pengguna/sampel."
    "\n                  Male   = skor apnea + 2, skor insomnia + 0"
    "\n                  Female = skor apnea + 0, skor insomnia + 1"
    "\nB. Age       -->  Umur pengguna/sampel saat ini."
    "\n                  <30   = skor apnea + 0, skor insomnia + 0"
    "\n                  30-39 = skor apnea + 1, skor insomnia + 0"
    "\n                  40-49 = skor apnea + 2, skor insomnia + 0"
    "\n                  >=50  = skor apnea + 3, skor insomnia + 0"
    "\nC. Sleep     -->  Durasi tidur per malam pengguna/sampel."
    "\n   Duration       <6 jam    = skor apnea + 1, skor insomnia + 3"
    "\n                  6-6,9 jam = skor apnea + 1, skor insomnia + 2"
    "\n                  7-8,9 jam = skor apnea + 1, skor insomnia + 2"
    "\n                  >=9 jam   = skor apnea + 1, skor insomnia + 2"
    "\nD. Sleep     -->  Tingkat kualitas tidur menurut pengguna/sampel."
    "\n   Quality        1-3  = skor apnea + 1, skor insomnia + 3"
    "\n                  4-5  = skor apnea + 1, skor insomnia + 2"
    "\n                  6-7  = skor apnea + 1, skor insomnia + 1"
    "\n                  8-10 = skor apnea + 0, skor insomnia + 0"
    "\nE. Activity  -->  Tingkat aktifitas fisik pengguna/sampel dalam satu hari."
    "\n   Level          <30  = skor apnea + 1, skor insomnia + 1"
    "\n                  >=30 = skor apnea + 0, skor insomnia + 0"
    "\nF. Stress    -->  Tingkat stress yang dialami pengguna/sampel."
    "\n   Level          1-3  = skor apnea + 0, skor insomnia + 0"
    "\n                  4-6  = skor apnea + 0, skor insomnia + 1"
    "\n                  7-10 = skor apnea + 0, skor insomnia + 3"
    "\nG. BMI       -->  Indeks massa tubuh pengguna/sampel."
    "\n   Category       Normal     = skor apnea + 0, skor insomnia + 0"
    "\n                  Overweight = skor apnea + 2, skor insomnia + 0"
    "\n                  Obese      = skor apnea + 3, skor insomnia + 0"
    "\nH. Blood     -->  Tekanan darah (sistolik/diastolik) pengguna/sampel)."
    "\n   Pressure       a) Sistolik"
    "\n                     <120 mmHg    = skor apnea + 0, skor insomnia + 0"
    "\n                     120-129 mmHg = skor apnea + 1, skor insomnia + 0"
    "\n                     130-139 mmHg = skor apnea + 2, skor insomnia + 0"
    "\n                     >=140 mmHg   = skor apnea + 3, skor insomnia + 0"
    "\n                  b) Diastolik"
    "\n                     <80 mmHg   = skor apnea + 0, skor insomnia + 0"
    "\n                     80-89 mmHg = skor apnea + 1, skor insomnia + 0"
    "\n                     90-99 mmHg = skor apnea + 2, skor insomnia + 0"
    "\n                     >=100 mmHg = skor apnea + 3, skor insomnia + 0"
    "\nI. Heart     -->  Detak jantung pengguna/sampel."
    "\n   Rate           <100  = skor apnea + 0, skor insomnia + 0"
    "\n                  >=100 = skor apnea + 1, skor insomnia + 1"
    "\nJ. Daily     -->  Jumlah langkah harian pengguna/sampel."
    "\n   Steps          <5000  = skor apnea + 1, skor insomnia + 1"
    "\n                  >=5000 = skor apnea + 0, skor insomnia + 0"
    
    "\n\nBerikut penjelasan makna setiap kategori Sleep Disorder dalam skrining ini:"
    "\n1. Normal == Skor Sleep Apnea dan Skor Insomnia di bawah 5."
    "\n   Kategori ini menunjukkan bahwa pengguna/sampel tidak memiliki risiko terdampak gangguan tidur."
    "\n2. Sleep Apnea == Skor Sleep Apnea di atas 5 dan lebih besar daripada Skor Insomnia."
    "\n   Kategori ini menunjukkan bahwa pengguna/sampel memiliki risiko terdampak Sleep Apnea lebih besar daripada Insomnia."
    "\n3. Insomnia == Skor Insomnia di atas 5 dan lebih besar daripada Skor Insomnia."
    "\n   Kategori ini menunjukkan bahwa pengguna/sampel memiliki risiko terdampak Insomnia lebih besar daripada Sleep Apnea."
    "\n4. Both == Skor Sleep Apnea dan Skor Insomnia di atas 5 dan keduanya berjumlah sama."
    "\n   Kategori ini menunjukkan bahwa pengguna/sampel memiliki risiko yang sama besar untuk terdampak Sleep Apnea dan Insomnia."
    )

def username_valid(username):
    return re.fullmatch(r"[A-Za-z0-9_]{3,20}", username) is not None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def muat_akun():
    if os.path.exists(file_akun):
        with open(file_akun, "r", encoding="utf-8") as file:
            return json.load(file)
    default = {
        "admin": hash_password("admin123"),
        "user": hash_password("user123")
    }
    with open(file_akun, "w", encoding="utf-8") as file:
        json.dump(default, file, indent=4)
    return default

user_awal = muat_akun()

def simpan_akun():
    with open(file_akun, "w", encoding="utf-8") as file:
        json.dump(user_awal, file, indent=4)

def menu_awal():
    print("\n===( Beranda )===")
    print("1. Register")
    print("2. Log In")
    print("3. Exit Program")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("\n===( Register )===")
        print("(Kosongkan username lalu tekan Enter untuk kembali ke Beranda)")
        while True:
            username = input("Buat Username Baru (3-20 karakter: huruf, angka, _): ").strip().lower()
            if username == "":
                print("Register Dibatalkan!")
                return menu_awal()
            if not username_valid(username):
                print("Username hanya boleh huruf, angka, dan _ (3-20 karakter).")
                continue
            if username in user_awal:
                print("Username sudah dipakai!") 
                continue
            break
        while True:
            password = input("Buat Password (minimal 6 karakter): ").strip()
            if len(password) < 6:
                print("Password minimal 6 karakter!")
                continue
            break
        user_awal[username] = hash_password(password)
        simpan_akun()
        print("Register berhasil! Silahkan Login.")
        return menu_awal()          
    elif opsi == "2":
        print("\n===( Login )===")
        print("(Kosongkan username lalu tekan Enter untuk kembali ke Beranda)")
        percobaan = 0
        while percobaan < 3:
            username = input("Masukkan username: ").strip()
            if username == "":
                return menu_awal()
            password = input("Masukkan password: ").strip()
            if username in user_awal and user_awal[username] == hash_password(password):
                print(f"Login berhasil! Selamat Datang, {username}")
                return menu_utama(username)
            percobaan += 1
            print(f"Username atau password salah! ({percobaan}/3)")
            print("Belum punya akun? Kosongkan username untuk kembali ke Beranda, lalu pilih 1. Register terlebih dahulu.")
        return menu_awal()
    elif opsi == "3":
        print("\nTerima kasih telah menggunakan sistem skrining risiko gangguan tidur!")
    else:
        print("\nMenu tidak tersedia!")
        return menu_awal()

def menu_utama(username):
    print("\n=====( Menu Utama )=====")
    print(f"Username: {username}")
    print("1. Mengenal Sleep Disorder")
    print("2. Data Sampel Sleep Disorder")
    print("3. Pencarian Data Sampel")
    print("4. Skrining Mandiri")
    print("5. Pembobotan Kategori")
    print("6. Riwayat Pemeriksaan Saya")
    print("7. Log Out")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("\n===( Mengenal Sleep Disorder )===")
        print(text1)
        return kembali_ke_menu(username)
    elif opsi == "2":
        print("\n===( Data Sampel Sleep Disorder )===")
        return menu_data_sampel(username)
    elif opsi == "3":
        print("\n===( Pencarian Data Sampel )===")
        return menu_cari_data(username)
    elif opsi == "4":
        print("\n==( Skrining Mandiri )===")
        return menu_skrining(username)
    elif opsi == "5":
        print("\n===( Pembobotan Kategori )===")
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

def kembali_ke_menu(username):
    print("\n1. Back to Menu")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("Kembali ke menu utama.")
        return menu_utama(username)
    else:
        while opsi != "1":
            print("Menu tidak tersedia!")
            opsi = input("\nPilih menu yang tersedia: ").strip()
            if opsi == "1":
                print("Kembali ke menu utama.")
                return menu_utama(username)

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

def Klasifikasi_status_user(total_skor_apnea,total_skor_insomnia):
    if total_skor_apnea >= 5 or total_skor_insomnia >= 5:
        if total_skor_apnea > total_skor_insomnia:
            status_user = "Sleep Apnea"
        elif total_skor_insomnia > total_skor_apnea:
            status_user = "Insomnia"
        else:
            status_user = "Both"
    else:
        status_user = "Normal"
    return status_user

def menu_skrining(username):
    print("Silahkan masukkan data yang dibutuhkan dengan benar!")
    print("Catatan: 1. Ketik dengan lengkap untuk Jenis Kelamin dan Berat Badan.")
    print("         2. Pada tekanan darah, angka kiri harus lebih besar dari angka kanan.")
    gender =             input("jenis Kelamin (Male/Female)           : ").strip()
    age =            int(input("Umur Pengguna (tahun)                 : ").strip())
    sleep_duration = int(input("Durasi Tidur (1-24 jam)               : ").strip())
    sleep_quality =  int(input("Kualitas Tidur (1-10)                 : ").strip())
    activity_level = int(input("Tingkat Aktivitas (1-100)             : ").strip())
    stress_level =   int(input("Tingkat Stress (1-10)                 : ").strip())
    bmi_category =       input("Berat Badan (Normal/Overweight/Obese) : ").strip()
    blood_pressure =     input("Tekanan Darah (Contoh: 115/86)        : ").strip()
    heart_rate =     int(input("Detak Jantung (20-220 bpm)            : ").strip())
    daily_steps =    int(input("Perkiraan Langkah Harian              : ").strip())

    while not validasi_data(gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,heart_rate,daily_steps):
        print("Terdapat kesalahan pada data yang Anda input. Mohon Diperhatikan Lagi!")
        print("Catatan: 1. Ketik dengan lengkap untuk Jenis Kelamin dan Berat Badan.")
        print("         2. Pada tekanan darah, angka kiri harus lebih besar dari angka kanan.")
        gender =             input("jenis Kelamin (Male/Female)           : ").strip()
        age =            int(input("Umur Pengguna (tahun)                 : ").strip())
        sleep_duration = int(input("Durasi Tidur (1-24 jam)               : ").strip())
        sleep_quality =  int(input("Kualitas Tidur (1-10)                 : ").strip())
        activity_level = int(input("Tingkat Aktivitas (1-100)             : ").strip())
        stress_level =   int(input("Tingkat Stress (1-10)                 : ").strip())
        bmi_category =       input("Berat Badan (Normal/Overweight/Obese) : ").strip()
        blood_pressure =     input("Tekanan Darah (Contoh: 115/86)        : ").strip()
        heart_rate =     int(input("Detak Jantung (20-220 bpm)            : ").strip())
        daily_steps =    int(input("Perkiraan Langkah Harian              : ").strip())

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
    status_user = Klasifikasi_status_user(total_skor_apnea,total_skor_insomnia)
    
    parameter = {
        "gender": gender, 
        "age": age, 
        "sleep_duration": sleep_duration, 
        "sleep_quality": sleep_quality, 
        "activity_level": activity_level, 
        "stress_level": stress_level, 
        "bmi_category": bmi_category, 
        "blood_pressure": blood_pressure, 
        "heart_rate": heart_rate, 
        "daily_steps": daily_steps
        }
    path = simpan_riwayat(username,parameter,total_skor_apnea,total_skor_insomnia,status_user)
    tambah_ke_dataset(parameter)
    print(f"\nHasil Skrining Anda disimpan ke: {os.path.abspath(path)}")

    print(f"\n[Hasil Skrining Pengguna: {username}]")                
    print(f"Total Skor Sleep Apnea    : {total_skor_apnea}")
    print(f"Total Skor Insomnia       : {total_skor_insomnia}")
    print(f"Status Pengguna           : {status_user}")
    print(buat_rekomendasi(status_user,sleep_duration,activity_level,stress_level,bmi_category,daily_steps))

    return kembali_ke_menu(username)

def buat_rekomendasi(status_user,sleep_duration,activity_level,stress_level,bmi_category,daily_steps):
    print("\nBerikut Rekomendasi dari Kami: ")
    if status_user in ["Normal", "Sleep Apnea", "Insomnia", "Both"]:
        if sleep_duration > 9:
            print("Kurangi durasi tidur menuju 7-9 jam per malam, termasuk akhir pekan.")
        elif sleep_duration < 7:
            print("Tambah durasi tidur menuju 7-9 jam per malam, termasuk akhir pekan.")
        if activity_level < 30:
            print("Targetkan aktivitas fisik minimal 30 menit per hari, seperti olahraga ringan).")
        if stress_level >= 7:
            print("Lakukan latihan pernafasan dan relaksasi setiap hari, serta atur pola tidur yang baik.")
        elif bmi_category == "Obese":
            print("Terapkan pola makan sehat! Hindari makanan yang mengandung banyak lemak dan gula, perbanyak makan sayur dan buah.")
        if daily_steps < 3000:
            print("Naikkan langkah harian secara bertahap, misalnya tambah 1.000 langkah tiap minggu.")
    else:
        print("Tidak ada yang perlu diperbaiki lagi! Semoga tidur Anda menjadi lebih baik kedepannya.")
    return "Note: Hasil ini hanya skrining awal berbasis skor, bukan diagnosis medis!"

def path_riwayat(username):
    name = re.sub(r"[^A-Za-z0-9_-]", "_", username)
    return os.path.join(folder_riwayat, f"riwayat_{username}.csv")

def simpan_riwayat(username,parameter,total_skor_apnea,total_skor_insomnia,status_user):
    os.makedirs(folder_riwayat, exist_ok=True)
    path = path_riwayat(username)
    file_baru = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=kolom_riwayat)
        if file_baru:
            writer.writeheader()
        writer.writerow({
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **parameter,
            "total_skor_apnea": total_skor_apnea,
            "total_skor_insomnia": total_skor_insomnia,
            "status_user": status_user,
        })
    return path

def tambah_ke_dataset(p):
    with open(file_csv, "r", encoding="utf-8-sig") as f:
        id_baru = len(f.readlines())
    with open(file_csv, "a", encoding="utf-8") as f:
        f.write(f"{id_baru};{p['gender']};{p['age']};{p['sleep_duration']};{p['sleep_quality']};{p['activity_level']};{p['stress_level']};{p['bmi_category']};{p['blood_pressure']};{p['heart_rate']};{p['daily_steps']}\n")

def baca_riwayat(username):
    path = path_riwayat(username)
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def menu_riwayat(username):
    riwayat = baca_riwayat(username)
    if len(riwayat) == 0:
        print("Belum ada riwayat pemeriksaan. Silakan lakukan Skrining Mandiri terlebih dahulu!")
        return kembali_ke_menu(username)

    print(f"[TABEL RIWAYAT SKRINING USER: {username}]")
    print("=" * 179)
    print(f"|{'No':<4}|{'Tanggal':<20}|{'Gender':<6}|{'Age':<3}|{'Sleep Duration':<14}|{'Sleep Quality':<13}|{'Activity Level':<14}|{'Stress Level':<12}|{'BMI Category':<12}|{'Blood Pressure':<14}|{'Heart Rate':<10}|{'Daily Steps':<11}|{'Sleep Apnea':<11}|{'Insomnia':<8}|{'Status':<11}|")
    print("=" * 179)
    for nomor, row in enumerate(riwayat, start=1):
        print(f"|{nomor:<4}|{row['tanggal']:<20}|{row['gender']:<6}|{row['age']:<3}|{row['sleep_duration']:<14}|{row['sleep_quality']:<13}|{row['activity_level']:<14}|{row['stress_level']:<12}|{row['bmi_category']:<12}|{row['blood_pressure']:<14}|{row['heart_rate']:<10}|{row['daily_steps']:<11}|{row['total_skor_apnea']:<11}|{row['total_skor_insomnia']:<8}|{row['status_user']:<11}|")
    print("=" * 179)

    print(f"Jumlah Pemeriksaan  : {len(riwayat)}")
    print(f"Status Terbaru      : {riwayat[-1].get('status_user', '-')}")
    if len(riwayat) >= 2:
        sebelum = riwayat[-2].get("status_user", "-")
        sekarang = riwayat[-1].get("status_user", "-")
        if sebelum not in urutan_status or sekarang not in urutan_status:
            perubahan = "-"
        elif urutan_status[sekarang] < urutan_status[sebelum]:
            perubahan = f"Membaik ({sebelum} -> {sekarang})"
        elif urutan_status[sekarang] > urutan_status[sebelum]:
            perubahan = f"Memburuk ({sebelum} -> {sekarang})"
        else:
            perubahan = f"Tetap ({sekarang})"
        print(f"Dibanding sebelummnya: {perubahan}")
    print("Note: Hasil ini hanya skrining awal berbasis skor, bukan diagnosis medis!")

    return kembali_ke_menu(username)

def menu_data_sampel(username):
    data_sampel = muat_data_sampel()
    if not os.path.exists(file_csv):
        print("File CSV tidak Ditemukan")
    elif len(data_sampel) == 0:
        print("\nDataset tidak valid!")
    else:
        cetak_tabel_sampel(data_sampel, "TABEL SAMPEL RISIKO SLEEP DISORDER")
        daftar_status = ["Sleep Apnea", "Insomnia", "Both", "Normal"]
        jumlah = {s: sum(1 for r in data_sampel if r["status"] == s) for s in daftar_status}
        print("\n[RINGKASAN TABEL SAMPEL]")
        print(f"{'Jumlah Data':<28}: {len(data_sampel)}")
        for s in daftar_status:
            print(f"{'Jumlah ' + s:<28}: {jumlah[s]}")
        for s in daftar_status:
            print(f"{'Persentase ' + s:<28}: {jumlah[s] / len(data_sampel) * 100:.2f}%")
    return kembali_ke_menu(username)

def muat_data_sampel():
    hasil = []
    if not os.path.exists(file_csv):
        return hasil
    with open(file_csv, "r", newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            try:
                row["person_id"]
                semua_skor = [klasifikasi_gender(row["gender"]), klasifikasi_age(int(row["age"])), klasifikasi_sleep_duration(float(row["sleep_duration"])), klasifikasi_sleep_quality(int(row["sleep_quality"])), klasifikasi_activity_level(int(row["activity_level"])), klasifikasi_stress_level(int(row["stress_level"])), klasifikasi_bmi_category(row["bmi_category"]), klasifikasi_blood_pressure(row["blood_pressure"]), klasifikasi_heart_rate(int(row["heart_rate"])), klasifikasi_daily_steps(int(row["daily_steps"]))]
            except (KeyError, ValueError):
                continue
            row["total_skor_apnea"] = sum(skor[0] for skor in semua_skor)
            row["total_skor_insomnia"] = sum(skor[1] for skor in semua_skor)
            row["status"] = Klasifikasi_status_user(row["total_skor_apnea"], row["total_skor_insomnia"])
            hasil.append(row)
    return hasil

def cetak_tabel_sampel(rows, judul):
    print(f"[{judul}]")
    print("=" * 179)
    print(f"|{'No':<4}|{'Person ID':<10}|{'Gender':<6}|{'Age':<3}|{'Sleep Duration':<14}|{'Sleep Quality':<13}|{'Activity Level':<14}|{'Stress Level':<12}|{'BMI Category':<12}|{'Blood Pressure':<15}|{'Heart Rate':<10}|{'Daily Steps':<11}|{'Skor Sleep Apnea':<12}|{'Skor Insomnia':<15}|{'Status':<12}|")
    print("=" * 179)
    for nomor, row in enumerate(rows, start=1):
        print(f"|{nomor:<4}|{row['person_id']:<10}|{row['gender']:<6}|{row['age']:<3}|{row['sleep_duration']:<14}|{row['sleep_quality']:<13}|{row['activity_level']:<14}|{row['stress_level']:<12}|{row['bmi_category']:<12}|{row['blood_pressure']:<15}|{row['heart_rate']:<10}|{row['daily_steps']:<11}|{row['total_skor_apnea']:<12}|{row['total_skor_insomnia']:<15}|{row['status']:<12}|")
    print("=" * 179)

def menu_cari_data(username):
    data_sampel = muat_data_sampel()
    if len(data_sampel) == 0:
        print("File CSV tidak ditemukan atau dataset tidak valid!")
        return kembali_ke_menu(username)

    parameter = ["person_id", "gender", "age", "sleep_duration", "sleep_quality", "activity_level", "stress_level", "bmi_category", "blood_pressure", "heart_rate", "daily_steps", "status"]
    rentang_durasi = [("Kurang dari 6 jam", 0, 6), ("6 - 6,9 jam", 6, 7), ("7 - 8,9 jam", 7, 9), ("9 jam atau lebih", 9, 100)]

    print("Cari data berdasarkan parameter:")
    for no, kolom in enumerate(parameter, start=1):
        print(f"{no}. {kolom}")
    opsi = input("Pilih parameter: ").strip()
    if not opsi.isdigit() or not 1 <= int(opsi) <= len(parameter):
        print("Menu tidak tersedia!")
        return menu_cari_data(username)
    kolom = parameter[int(opsi) - 1]

    if kolom == "sleep_duration":
        for no, (label, bawah, atas) in enumerate(rentang_durasi, start=1):
            print(f"{no}. {label}")
        pilihan = input("Pilih rentang durasi tidur: ").strip()
        if not pilihan.isdigit() or not 1 <= int(pilihan) <= len(rentang_durasi):
            print("Menu tidak tersedia!")
            return menu_cari_data(username)
        _, bawah, atas = rentang_durasi[int(pilihan) - 1]
        hasil = [r for r in data_sampel if bawah <= float(r["sleep_duration"]) < atas]
    else:
        kata = input(f"\nMasukkan {kolom} yang dicari: ").strip().lower()
        hasil = [r for r in data_sampel if r[kolom].strip().lower() == kata]

    if len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        cetak_tabel_sampel(hasil, "\nHASIL PENCARIAN DATA SAMPEL")
        print(f"Jumlah data ditemukan: {len(hasil)}")
    return kembali_ke_menu(username)

print("\n========( Sleep Disorder Risk Screening System )========")
print("Selamat datang di sistem skrining risiko gangguan tidur!")    
menu_awal = menu_awal()
#Mini Project Sleep Health and Lifestyle Dataset
import csv
import os
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
    "daily_steps", "total_skor_apnea", "total_skor_insomnia"
    ]
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_riwayat = "C:\Users\Admin\Downloads\Mini Project\riwayat"
file_akun = "C:\Users\Admin\Downloads\Mini Project\akun.json"

data = []
skor_apnea = 0
skor_insomnia = 0
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

def menu_awal():
    print("\n===( Beranda )===")
    print("1. Log In")
    print("2. Register")
    print("3. Exit Program")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("\n===( Login )===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        if username in user_awal and user_awal[username] == password:
            print(f"Login berhasil! Selamat Datang, {username}")
            return menu_utama(username)
        else:
            print("Username atau password salah!")
            return menu_awal()             
    elif opsi == "2":
        print("\n===( Register )===")
        username = input("Buat Username Baru: ").strip()
        if username in user_awal:
            print("Username sudah dipakai") 
            return menu_awal()
        password = input("Buat Password: ").strip()
        user_awal[username] = password
        print("Register berhasil! Silahkan Login.")
        return menu_awal()
    elif opsi == "3":
        print("\nTerima kasih telah menggunakan sistem skrining risiko gangguan tidur!")
    else:
        print("\nMenu tidak tersedia!")
        return menu_awal()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def muat_akun():
    if os.path.exists(file_akun):
        with open(file_akun, "r", encoding="utf-8") as file:
            return json.load(file)
    return{
        "admin": hash_password("admin123"),
        "user": hash_password("user123")
    }

user_awal = muat_akun()

def simpan_akun():
    with open(file_akun, "w", encoding="utf-8") as file:
        json.dump(user_awal, file, indent=4)

def menu_utama(username):
    print("\n=====( Menu Utama )=====")
    print(f"Username: {username}")
    print("1. Mengenal Sleep Disorder")
    print("2. Data Sampel Sleep Disorder")
    print("3. Pencarian Data Sampel")
    print("4. Skrining Mandiri")
    print("5. Status Kategori")
    print("6. Riwayat Pemeriksaan Saya")
    print("7. Log Out")
    opsi = input("Pilih menu yang tersedia: ").strip()
    if opsi == "1":
        print("\n===( Mengenal Sleep Disorder )===")
        print(text1)
        return kembali_ke_menu(username)
    elif opsi == "2":
        print("\n===( Data Sampel Sleep Disorder )===")
        return menu_data_sampel()
    elif opsi == "3":
        print("\n===( Pencarian Data Sampel )===")
        return menu_cari_data()
    elif opsi == "4":
        print("\n==( Skrining Mandiri )===")
        return menu_skrining(username)
    elif opsi == "5":
        print("\n===( Status Kategori )===")
        print(text2)
        return kembali_ke_menu()
    elif opsi == "6":
        print("\n===( Riwayat Pemeriksaan Saya )===")
        return menu_riwayat(username)
    elif opsi == "7":
        print(f"\n{username} berhasil Log Out. Kembali ke Beranda")
        return menu_awal()
    else:
        print("\nMenu tidak tersedia!")
        return menu_utama(username)

def menu_cari_data():
    print("Coming Soon")
    return kembali_ke_menu(username)

def menu_skrining(username):
    print("Silahkan masukkan data yang dibutuhkan dengan benar!")
    print("Note: N = Normal, K = Kegemukan, O = Obesitas")
    print("      Ketik lengkap untuk Jenis Kelamin dan Berat Badan")
    gender = input("jenis Kelamin (Male/Female) : ").strip()
    age = int(input("Umur                        : ").strip())
    sleep_duration = int(input("Durasi Tidur (1-10)         : ").strip())
    sleep_quality = int(input("Kualitas Tidur (1-10)       : ").strip())
    activity_level = int(input("Tingkat Aktivitas (1-100)   : ").strip())
    stress_level = int(input("Tingkat Stress (1-10)       : ").strip())
    bmi_category = input("Kategori Berat Badan (N/K/O): ").strip()
    blood_pressure = input("Tekanan Darah (ex: 115/86)  : ").strip()
    heart_rate = int(input("Detak Jantung (20-220)      : ").strip())
    daily_steps = int(input("Perkiraan Langkah Harian    : ").strip())

    while not validasi_data(gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,heart_rate,daily_steps):
        print("Terdapat kesalahan pada data yang Anda input. Mohon Diperhatikan Lagi!")
        print("Note: N = Normal, K = Kegemukan, O = Obesitas")
        print("      Ketik lengkap untuk Jenis Kelamin dan Berat Badan")
        gender = input("jenis Kelamin (Male/Female) : ").strip()
        age = int(input("Umur                        : ").strip())
        sleep_duration = int(input("Durasi Tidur (1-10)         : ").strip())
        sleep_quality = int(input("Kualitas Tidur (1-10)       : ").strip())
        activity_level = int(input("Tingkat Aktivitas (1-100)   : ").strip())
        stress_level = int(input("Tingkat Stress (1-10)       : ").strip())
        bmi_category = input("Kategori Berat Badan (N/K/O): ").strip()
        blood_pressure = input("Tekanan Darah (ex: 115/86)  : ").strip()
        heart_rate = int(input("Detak Jantung (20-220)      : ").strip())
        daily_steps = int(input("Perkiraan Langkah Harian    : ").strip())


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

    print("\n[Hasil Skrining Pengguna]")                
    print(f"Total Skor Sleep Apnea    : {total_skor_apnea}")
    print(f"Total Skor Insomnia       : {total_skor_insomnia}")
    print(f"Status Pengguna           : {status_user}")
    print(buat_rekomendasi(status_user,sleep_duration,activity_level,stress_level,bmi_category,daily_steps))

    return kembali_ke_menu(username)

def menu_riwayat(username):
    print("Tabel Riwayat Skrining Pengguna")
    return kembali_ke_menu(username)

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

def buat_rekomendasi(status_user,sleep_duration,activity_level,stress_level,bmi_category,daily_steps):
    if status_user == "Normal":
        print("Risiko Anda terbilang kecil. Pertahankan pola hidup yang sehat ini!")
    elif status_user == "Sleep Apnea":
        print("Anda memiliki risiko lebih besar terkena gangguan Sleep Apnea")
    elif status_user == "Insomnia":
        print("Anda memiliki risiko lebih besar terkena gangguan Insomnia")
    else:
        print("Anda memiliki risiko terkena kedua jenis gangguan tidur ini")
    
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
        print("Tidak ada yang perlu diperbaiki lagi! Semoga tidur Anda menjadi lebih baik.")
    return "\n={Data disimpan ke dalam riwayat skrining Anda}="

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

def menu_data_sampel():
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

print("\n========( Sleep Disorder Risk Screening System )========")
print("Selamat datang di sistem skrining risiko gangguan tidur!")    
menu_awal = menu_awal()
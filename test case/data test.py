import csv
import io

def baca_data(nama_file):
    with open(nama_file, "r", encoding="utf-8-sig") as file:
        teks_bersih = file.read().replace('"', "")
        return list(csv.DictReader(io.StringIO(teks_bersih)))

def cek_durasi(durasi):
    if durasi < 0 or durasi > 24:
        return "Durasi Negatif, Data Tidak Valid."
    elif durasi < 6:
        return "Kurang"
    else:
        return "Baik"

def cek_kualitas(kualitas):
    if kualitas < 1 or kualitas > 10:
        return "Data Tidak Valid (Skala 1-10)"
    elif kualitas < 6:
        return "Buruk"
    else:
        return "Baik"

def cek_stres(stres):
    if stres < 1 or stres > 10:
        return "Data Tidak Valid (Skala 1-10)"
    elif stres < 8:
        return "Sedang"
    else:
        return "Tinggi"

data = baca_data(r"C:\Users\Admin\Downloads\Analisis-Risiko-Gangguan-Tidur-Berdasarkan-Faktor-Gaya-Hidup-dan-Kesehatan\test case\Sleep_health_and_lifestyle_dataset(rev).csv")

def uji_baris(baris):
    pid = baris["person_id"]
    try:
        durasi = float(baris["sleep_duration"])
        kualitas = float(baris["sleep_quality"])
        stres = float(baris["stress_level"])

        if durasi < 0 or durasi > 24:
            return f"ID {pid} ({durasi}, {kualitas}, {stres}) -> Durasi Negatif"
        
        return (f"ID {pid} ({durasi}, {kualitas}, {stres}) -> "
                f"{cek_durasi(durasi)}, {cek_kualitas(kualitas)}, {cek_stres(stres)}")
    except ValueError:
        kolom_kosong = [k for k, v in baris.items() if v == ""]
        if kolom_kosong:
            return f"ID {pid} -> Dibuang. Data Kosong pada Kolom: {', '.join(kolom_kosong)}"
        return f"ID {pid} -> Dibuang. Format Tidak Valid."

print("TEST 1 - Data Normal dan Lengkap:")
print("TC-1.1:", uji_baris(data[5]))
print("TC-1.2:", uji_baris(data[7]))

print("\nTEST 2 - Data Batas:")
print("TC-2.1:", uji_baris(data[4]))
print("TC-2.2:", uji_baris(data[2]))

print("\nTEST 3 - Dataset Kosong / Hanya Header:")

def cek_teks_csv_kosong_atau_header(teks_csv):
    pembaca = list(csv.DictReader(io.StringIO(teks_csv)))
    if len(pembaca) == 0:
        return "Data Kosong / Hanya Header"
    return f"Terdapat {len(pembaca)} Data"

data_hanya_header = "person_id,gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,blood_pressure,heart_rate,daily_steps\n"
data_kosong_total = ""
    
print("TC-3.1 (Hanya Header):", cek_teks_csv_kosong_atau_header("data_hanya_header"))
print("Tc-3.2 (Kosong Total):", cek_teks_csv_kosong_atau_header("data_kosong_total"))

print("\nTEST 4 - Data Tidak Valid:")
print("TC-4.1:", uji_baris(data[1]))
print("TC-4.2:", uji_baris(data[15]))

print("\nTEST 5 - Data Regresi:")
print("TC-5.1 (Bug input Desimal 6.1) :", uji_baris(data[0]))
print("TC-5.2 (Bug input Desimal 6.5) :", uji_baris(data[3]))
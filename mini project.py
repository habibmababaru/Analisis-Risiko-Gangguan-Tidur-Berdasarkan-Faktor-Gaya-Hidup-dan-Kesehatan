import csv
import os

file_csv = r"C:\Users\Admin\Downloads\Sleep_health_and_lifestyle_dataset(rev).csv"
kolom_wajib = [ 
    "gender", "age", 
    "sleep_quality", 
    "activity_level", 
    "stress_level", 
    "bmi_category", 
    "blood_pressure", 
    "heart_rate", 
    "daily_steps", 
    ]

data = []
data_tidak_valid = 0

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
    if gender == "Male":
        skor_apnea += 2
        skor_insomnia += 0
    elif gender == "Female":
        skor_apnea += 0
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

def klasifikasi_age(age):
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
    if activity_level >= 30:
        skor_apnea += 0
        skor_insomnia += 0
    else:
        skor_apnea += 1
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

def stress_level(stress_level):
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
    if diastolik >= 90:
        skor_apnea += 3
        skor_insomnia += 0
    elif diastolik >= 80:
        skor_apnea += 2
        skor_insomnia += 0
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_heart_rate(heart_rate):
    if heart_rate >= 100:
        skor_apnea += 1
        skor_insomnia += 1
    else:
        skor_apnea += 0
        skor_insomnia += 0
    return skor_apnea, skor_insomnia

def klasifikasi_daily_steps(daily_steps):
    if daily_steps >= 5000:
        skor_apnea += 0
        skor_insomnia += 0
    else:
        skor_apnea += 1
        skor_insomnia += 1
    return skor_apnea, skor_insomnia

if not os.path.exists(file_csv):
    print("File CSV tidak Ditemukan")

else:
    with open(file_csv, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("Header dalam File tidak Ditemukan")

        elif not all(kolom in reader.fieldnames for kolom in kolom_wajib):
            kolom_kosong = [kolom for kolom in kolom_wajib if kolom not in reader.fieldnames]
            print("Kolom dalam File tidak Ditemukan")
            for kolom in kolom_kosong:
                print(f"- {kolom}")

        else:
            for nomor_baris, row in enumerate(reader, start=2):
                try:
                    person_id = row["person_id"]
                    gender = row["gender"]
                    age = int(row["age"])
                    sleep_quality = int(row["sleep_quality"])
                    activity_level = int(row["activity_level"])
                    stress_level = int(row["stress_level"])
                    bmi_category = row["bmi_category"]
                    blood_pressure = row["blood_pressure"]
                    heart_rate = int(row["heart_rate"])
                    daily_steps = int(row["daily_steps"])

                except (ValueError, TypeError, AttributeError):
                    print(f"Peringatan! Sample dengan Person ID ({person_id}): "
                        "salah satu nilai tidak valid!")
                    data_tidak_valid += 1
                    continue

                if not validasi_data(gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,heart_rate,daily_steps):
                    print(f"Peringatan! Sample dengan Person ID ({person_id}): "
                        "data tidak valid!")
                    data_tidak_valid += 1
                    continue

                data.append(row)
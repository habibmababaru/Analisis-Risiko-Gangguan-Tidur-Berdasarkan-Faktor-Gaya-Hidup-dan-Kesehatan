#Mini Project Sleep Health and Lifestyle Dataset
import csv
import os

file_csv = r"C:\Users\Admin\Downloads\Sleep_health_and_lifestyle_dataset(rev).csv"
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

data = []
data_tidak_valid = 0
skor_apnea = 0
skor_insomnia = 0

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
                data_tidak_valid += 1

        else:
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

                except (ValueError, TypeError, AttributeError):
                    print(f"Peringatan! Sample dengan Person ID ({person_id}): "
                        "salah satu nilai tidak valid!")
                    data_tidak_valid += 1
                    continue

                if not validasi_data(gender,age,sleep_duration,sleep_quality,activity_level,stress_level,bmi_category,heart_rate,daily_steps):
                    print(f"Peringatan! Sample dengan Person ID ({person_id}): "
                        "salah satudata tidak valid!")
                    data_tidak_valid += 1
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


                print("\nDATA EVALUASI SLEEP HEALTH")
                print("=" * 179)
                print(f"|{'No':<4}|{'Person ID':<10}|{'Gender':<6}|{'Age':<3}|{'Sleep Duration':<14}|{'Sleep Quality':<13}|{'Activity Level':<14}|{'Stress Level':<12}|{'BMI Category':<12}|{'Blood Pressure':<15}|{'Heart Rate':<10}|{'Daily Steps':<11}|{'Total Apnea':<12}|{'Total Insomnia':<15}|{'Status':<12}|")
                print("=" * 179)
                for nomor, row in enumerate(data, start=1):
                    print(f"|{nomor:<4}|{row['person_id']:<10}|{row['gender']:<6}|{row['age']:<3}|{row['sleep_duration']:<14}|{row['sleep_quality']:<13}|{row['activity_level']:<14}|{row['stress_level']:<12}|{row['bmi_category']:<12}|{row['blood_pressure']:<15}|{row['heart_rate']:<10}|{row['daily_steps']:<11}|{row['total_skor_apnea']:<12}|{row['total_skor_insomnia']:<15}|{row['status']:<12}|")
                print("=" * 179)
                print("\nRINGKASAN EVALUASI DATA SLEEP HEALTH")
                print(f"Jumlah data valid           : {len(data)}")
                print(f"Jumlah data tidak valid     : {data_tidak_valid}")
                print(f"Jumlah Sleep Apnea          : {total_apnea}")
                print(f"Jumlah Insomnia             : {total_insomnia}")
                print(f"Jumlah Both                 : {total_both}")
                print(f"Jumlah Normal               : {total_normal}")
                print(f"Persentase Sleep Apnea      : {persentase_apnea:.2f}%")
                print(f"Persentase Insomnia         : {persentase_insomnia:.2f}%")
                print(f"Persentase Both             : {persentase_both:.2f}%")
                print(f"Persentase Normal           : {persentase_normal:.2f}%")
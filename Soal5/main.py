import csv


def baca_log(nama_file):
    data_valid = []
    data_ditolak = []

    with open(nama_file, "r", newline="", encoding="utf-8-sig") as file:
        pembaca = csv.reader(file)

        for nomor, baris in enumerate(pembaca, start=1):
            if nomor == 1:
                continue

            alasan = []

            if len(baris) != 2:
                alasan.append("Jumlah kolom harus dua")
            else:
                try:
                    debit = float(baris[1].strip())

                    if not 5 <= debit <= 25:
                        alasan.append("Debit di luar rentang 5 sampai 25")

                except ValueError:
                    alasan.append("Nilai debit bukan angka")

            if alasan:
                data_ditolak.append({
                    "nomor": nomor,
                    "isi": baris,
                    "alasan": ", ".join(alasan)
                })
            else:
                data_valid.append(debit)

    return data_valid, data_ditolak


def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh nol")

    return abs((hasil - acuan) / acuan) * 100


data_valid, data_ditolak = baca_log("log_debit.csv")

print("Jumlah data valid:", len(data_valid))
print("Jumlah data ditolak:", len(data_ditolak))

for data in data_ditolak:
    print(
        f"Baris {data['nomor']}: "
        f"{data['isi']} -> {data['alasan']}"
    )

if data_valid:
    hasil = sum(data_valid) / len(data_valid)

    print(f"Rata-rata data valid: {hasil:.2f}")

    acuan = 13.5714
    absolut = galat_absolut(hasil, acuan)
    relatif = galat_relatif(hasil, acuan)

    status = "LULUS" if relatif <= 0.5 else "TIDAK LULUS"

    print(f"Galat absolut: {absolut:.8f}")
    print(f"Galat relatif: {relatif:.6f}%")
    print(f"Status: {status}")
else:
    print("Tidak ada data valid.")
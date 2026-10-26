data_debit = [12.5, 14.0, 13.5, 15.0, 11.0]


def hitung_rata_rata(data):
    """Menghitung rata-rata data.

    Input:
        data: list berisi angka.
    Output:
        Nilai rata-rata data.
    """
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    return total / len(data)


def cari_terendah(data):
    """Mencari nilai terendah dalam data.

    Input:
        data: list berisi angka.
    Output:
        Nilai terkecil dalam data.
    """
    terendah = data[0]
    for nilai in data:
        if nilai < terendah:
            terendah = nilai
    return terendah


def cek_status(debit):
    """Menentukan status berdasarkan nilai debit.

    Input:
        debit: nilai debit air.
    Output:
        RENDAH jika debit < 10,
        NORMAL jika debit >= 10 dan debit <= 20,
        TINGGI jika debit > 20.
    """
    if debit < 10:
        return "RENDAH"
    elif debit <= 20:
        return "NORMAL"
    else:
        return "TINGGI"


if __name__ == "__main__":
    rata = hitung_rata_rata(data_debit)
    print("Rata-rata :", rata)
    print("Terendah  :", cari_terendah(data_debit))
    print("Status    :", cek_status(rata))
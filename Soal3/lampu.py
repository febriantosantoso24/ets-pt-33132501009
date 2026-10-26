class Lampu:
    jumlah_lampu = 0

    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.kecerahan = 0
        Lampu.jumlah_lampu += 1

    def nyalakan(self):
        self.aktif = True
        self.kecerahan = 100

    def matikan(self):
        self.aktif = False
        self.kecerahan = 0

    def atur(self, nilai):
        if self.aktif and 0 <= nilai <= 100:
            self.kecerahan = nilai

    def __str__(self):
        return (
            f"Lampu {self.nama}: aktif = {self.aktif}, "
            f"kecerahan = {self.kecerahan}"
        )
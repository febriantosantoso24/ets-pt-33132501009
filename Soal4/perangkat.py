class Perangkat:
    def __init__(self, nama):
        self.nama = nama
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

    def proses(self):
        raise NotImplementedError(
            "Method proses() harus dibuat pada class turunan"
        )


class SensorSuhu(Perangkat):
    def proses(self):
        return max(self.data)


class SensorDebit(Perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        return sum(self.data) / len(self.data)
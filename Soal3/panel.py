from lampu import Lampu


class PanelLampu:
    def __init__(self):
        self.lampu_merah = Lampu("merah")
        self.lampu_hijau = Lampu("hijau")

    def nyalakan_semua(self):
        self.lampu_merah.nyalakan()
        self.lampu_hijau.nyalakan()

    def tampilkan(self):
        print(self.lampu_merah)
        print(self.lampu_hijau)


panel = PanelLampu()

panel.nyalakan_semua()
panel.lampu_hijau.atur(30)
panel.tampilkan()
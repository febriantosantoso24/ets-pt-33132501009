from perangkat import SensorSuhu, SensorDebit

suhu = SensorSuhu("Suhu")
debit = SensorDebit("Debit", "L/menit")

suhu.baca(30.1)
suhu.baca(30.6)
suhu.baca(30.3)

debit.baca(12.0)
debit.baca(15.0)
debit.baca(15.0)

perangkat = [suhu, debit]

for p in perangkat:
    print(f"{p.nama} -> {p.proses()}")
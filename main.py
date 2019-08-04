# GENERATE RANDOM DATA using RANDOM MODULE
# :D

import random

nama_depan = ['Aji', 'Dhani', 'Dhika', 'Andhika', 'Andhani', 'Arfani', 'Ega', 'Egi', 'Ari', 'Rifqi', 'Lia', 'Randi', 'Afka', 'Hakim', 'Nur', 'Aula', 'Fajar', 'Fandi', 'Fila', 'Linda', 'Indi', 'Lindi', 'Laura', 'Eri', 'Silvi']
nama_belakang = ['Andi', 'Wulia', 'Lin', 'Kurnia', 'Alkaf', 'Anshari', 'Naufal', 'Reksa', 'Wahid', 'Bamas', 'Bambang', 'Aula', 'Hasan', 'Prasetyo', 'Prayogo', 'Darmawan', 'Tiran', 'Dirgantara', 'Prakoso', 'Andhika', 'Dewi', 'Setya', 'Hary', 'Heri', 'Haryanto', 'Harris', 'Martin']
nama_jalan = ['KH. Ahmad Dahlan', 'Timah', 'Nikel', 'Letjend S. Parman', 'Sulfat', 'Pasar Besar', 'Pondok', 'La. Sucipto', 'Tanjung', 'Sudirman', 'KH. Zen']
nama_kota = ['Jakarta', 'Lamongan', "Surabaya", 'Bandung', 'Bogor', 'Semarang', 'Yogyakarta', 'Batu', 'Nganjuk', 'Bali', 'Aceh', 'Medan', 'Palembang', 'Banyuwangi', 'Probolinggo', 'Klaten', 'Trenggalek', 'Gresik', 'Banten', 'Lampung', 'Serang', 'Blitar', 'Tulung Agung', 'Cirebon', 'Sidoarjo', 'Bengkulu‎', 'Mataram']

for num in range(100):
    first = random.choice(nama_depan)
    last = random.choice(nama_belakang)
    telepon = f'0{random.randint(80, 89)}-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(100, 999)}'
    nomor_jalan = random.randint(100, 999)
    jalan = random.choice(nama_jalan)
    kota = random.choice(nama_kota)
    kode_pos = random.randint(10000, 99999)
    address = f'Jl. {jalan}, No.{nomor_jalan}, {kota}, Kode Pos: {kode_pos}'
    email = first.lower() + '.' + last.lower() + '@mail.com'

    print(f'{first} {last}\n{telepon}\n{address}\n{email}\n')
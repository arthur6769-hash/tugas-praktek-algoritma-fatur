#PROGRAM PENILAIAN MAHASISWA

print('======PENILAIAN MAHASISWA======')

# Input data mahasiswa
tugas = float(input('Nilai tugas     : '))
uts = float(input('Nilai UTS     : '))
uas = float(input('Nilai UAS     : '))
kehadiran = float(input('kehadiran(%)     : '))

# menghitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Menentukan status kelulusan
if nilai_akhir < 75 or kehadiran < 80 : 
    status = 'BELUM LULUS'

# Memeriksa syarat dan status
elif (
    nilai_akhir >= 85
    and kehadiran >= 90
    and nilai_akhir .is_integer()
    and int(nilai_akhir) % 2 == 0
): 
    status = 'LULUS DENGAN PREDIKAT'
else:
    status = 'LULUS'

# Menampilkan hasil
print('\n=== HASIL PENILAIAN ===')
print(f'Nilai Akhir : {nilai_akhir:.1f}')
print(f'status      : {status}')
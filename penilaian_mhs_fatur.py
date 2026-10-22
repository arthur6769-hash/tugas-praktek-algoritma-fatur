#PROGRAM PENILAIAN MAHASISWA

print('======PENILAIAN MAHASISWA======')

# 1. Input data mahasiswa
tugas = float(input('Nilai tugas     : '))
uts = float(input('Nilai UTS     : '))
uas = float(input('Nilai UAS     : '))
kehadiran = float(input('kehadiran(%)     : '))

# 2. menghitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

#3. Menentukan status kelulusan
if nilai_akhir < 75 or kehadiran < 80 : 
    status = 'BELUM LULUS'

#4. Memeriksa syarat predikat
elif (
    nilai_akhir >= 85
    and kehadiran >= 90
    and nilai_akhir .is_integer()
    and int(nilai_akhir) % 2 == 0
): 
    status = 'LULUS DENGAN PREDIKAT'

#5. Jika lulus tetapi tidak mendapat predikat
else:
    status = 'LULUS'

#6. Menampilkan hasil
print('\n=== HASIL PENILAIAN ===')
print(f'Nilai Akhir : {nilai_akhir:.1f}')
print(f'status      : {status}')

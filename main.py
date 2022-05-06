class Data:
    def __init__(self,pin,id,rekening,nama,saldo,limit,password):
        self.pin = pin
        self.id = id
        self.rekening = rekening
        self.nama = nama
        self.saldo = saldo
        self.limit = limit
        self.password = password

    def menu_utama():
        print('''\n__menu__\n\t1. Penarikan Tunai 
        2. Setor Tunai
        3. Informasi
        4. Transfer
        5. Keluar dari profil
                    ''')

    def copying_main(self):
        while True:
            Data.menu_utama()
            try:
                choice = int(input('Pilih: '))
                # 1.Penarikan, 2.Setor, 3.Informasi, 4.transfer, 5. Keluar
                if choice == 1: # Penarikan tunai
                    print('\n__Penarikan tunai__ \n\t1. Rp. 100.000.00 \n\t2. Rp. 300.000.00 \n\t3. Rp. 500.000.00 \n\t4. Pilihan Lainnya \
                            \n\t5. Kembali ke Menu utama')
                    while True:
                        choice = int(input('Pilih: '))
                        
                        if choice == 1: # 100k
                            if self.saldo < 100000:
                                print('/---Saldo anda tidak cukup')
                                continue
                            elif self.saldo >= 100000:
                                # konfirmasi
                                print('Anda akan melakukan penarikan sebesar: Rp. 100.000.00')
                                while True:
                                    konfirmasi = input("Konfirmasi 'ya/tidak' : ")
                                    if konfirmasi == 'ya':
                                        self.saldo = self.saldo - 100000
                                        print('/---Penarikan tunai berhasil')
                                        break 
                                    elif konfirmasi == 'tidak':
                                        print('/---Anda membatalkan penarikan')
                                        break
                                    else:
                                        print('Masukkan keyword yang benar!')
                                        continue
                            break

                        elif choice == 2: # 300k
                            if self.saldo < 300000:
                                print('/---Saldo anda tidak cukup')
                                continue
                            elif self.saldo >= 300000:
                                # konfirmasi
                                print('Anda akan melakukan penarikan sebesar: Rp. 300.000.00')
                                while True:
                                    konfirmasi = input("Konfirmasi 'ya/tidak' : ")
                                    if konfirmasi == 'ya':
                                        self.saldo = self.saldo - 300000
                                        print('/---Penarikan tunai berhasil')
                                        break 
                                    elif konfirmasi == 'tidak':
                                        print('/---Anda membatalkan penarikan')
                                        break
                                    else:
                                        print('Masukkan keyword yang benar!')
                                        continue
                            break

                        elif choice == 3: # 500k
                            if self.saldo < 500000:
                                print('/---Saldo anda tidak cukup')
                                continue
                            elif self.saldo >= 500000:
                                # konfirmasi
                                print('Anda akan melakukan penarikan sebesar: Rp. 500.000.00')
                                while True:
                                    konfirmasi = input("Konfirmasi 'ya/tidak' : ")
                                    if konfirmasi == 'ya':
                                        self.saldo = self.saldo - 500000
                                        print('/---Penarikan tunai berhasil')
                                        break 
                                    elif konfirmasi == 'tidak':
                                        print('/---Anda membatalkan penarikan')
                                        break
                                    else:
                                        print('Masukkan keyword yang benar!')
                                        continue
                            break

                        elif choice == 4: # lainnya
                            jumlah = int(input('Jumlah penarikan: Rp. '))
                            if self.saldo < jumlah:
                                print('/---Saldo anda tidak cukup')
                                continue
                            elif self.saldo >= jumlah:
                                # konfirmasi
                                print('\n/Anda akan melakukan penarikan sebesar: Rp. {}'.format(jumlah))
                                while True:
                                    konfirmasi = input("Konfirmasi 'ya/tidak' : ")
                                    if konfirmasi == 'ya':
                                        self.saldo = self.saldo - jumlah
                                        print('/---Penarikan tunai berhasil')
                                        break 
                                    elif konfirmasi == 'tidak':
                                        print('/---Anda membatalkan penarikan')
                                        break
                                    else:
                                        print('Masukkan keyword yang benar!')
                                        continue
                            break
                        elif choice == 5:
                            break
                    continue        
                elif choice == 2: # Setor tunai
                    while True:
                        print('\n__Setor tunai__')
                        setor_tunai = int(input('\tJumlah setor: Rp. '))
                        #konfirmasi
                        print('\n/Anda akan melakukan setoran sebesar: Rp. {}'.format(setor_tunai))
                        while True:
                            konfirmasi = input("Konfirmasi 'ya/tidak' : ")
                            if konfirmasi == 'ya':
                                
                                if setor_tunai <= self.limit and (self.saldo + setor_tunai) <= 60:
                                    self.saldo = self.saldo + setor_tunai
                                    print('/---Setor tunai berhasil')
                                    break
                                elif setor_tunai > 60 or (self.saldo + setor_tunai) > 60:
                                    print('\n/---Jumlah setoran melebihi limit saldo anda! \
                                        \n\tsilahkan melakukan penambahan limit')
                                    break

                            elif konfirmasi == 'tidak':
                                print('/---Anda membatalkan Setor tunai')
                                break
                            else:
                                print('Masukkan keyword yang benar!')
                                continue

                        break
                    continue
                elif choice == 3: # Informasi
                    while True:
                        print('\n__informasi__ \n\t1. Cek saldo \n\t2. Info Pribadi \n\t3. Kembali ke Menu utama')
                        choice = int(input('Pilih: '))

                        if choice == 1: # Cek saldo
                            print(f"\t/---Saldo anda: Rp. {self.saldo}")
                            continue
                        elif choice == 2: # info Pribadi
                            # nama, id, limit, no rekening
                            print(f"\n\t/Nama: {self.nama} \n\t/ID: {self.id} \
                                    \n\t/Limit: {self.limit} \n\t/Cek Rekening: ketik 'rekening'")

                            while True:
                                choice2 = input('input kembali/rekening: ').lower()
                                if choice2 == 'kembali':
                                    break
                                elif choice2 == 'rekening':
                                    while True:
                                        getpass = input('Masukkan password: ')
                                        if getpass == self.password:
                                            print(f"\t/---Rekening anda: {self.rekening}")
                                            break
                                        else:
                                            print('password salah')
                                            continue
                                    break
                                else: 
                                    print('kata-kata salah')
                                    continue
                            continue
                                

                        elif choice == 3: #kembali
                            break
                    continue
                elif choice == 4: # Transfer
                    print('/fitur Transfer belum tersedia')
                    continue
                elif choice == 5: # keluar
                    print('\tKonfirmasi keluar dari profil anda')
                    konfirmasi = input("Anda akan diminta pin kembali untuk masuk. 'keluar/tidak' : ")
                    if konfirmasi == 'keluar':
                        print('/Keluar dari profil..')
                        break
                    elif konfirmasi == 'tidak':
                        continue
                else:
                    print('Masukkan keyword yang benar.')
                    continue 

                break
            except:
                print('invalid')
                continue



data_user = {
    'nicky': Data(1234, 527819, 231910, 'Nicky Lauda', 0, 60000000, 'contohrek'),
    'edward': Data(4321, 527761, 990607, 'Edward Joe', 0, 90000000, 'cekrekening')
}


while True:
    try:
        entering_pin = int(input('\n< Bank Mariejoa >\ninput your pin: '))

        if entering_pin == data_user['nicky'].pin:
            Data.copying_main(data_user['nicky'])
            continue

        elif entering_pin == data_user['edward'].pin:
            Data.copying_main(data_user['edward'])
            continue
        else:
            print('\tthe pin is invalid')
            continue 
    except:
        print('invalid')
        continue

import os, sys
P  =  cetak
Ok  =  os . system
sementara  benar:
    P ( " " )
    P ( " " )
    c  =  masukan ( "A)dd, E)dit, D)elete, S)search, L)ist, Q)uit: " )
    jika c . lebih rendah ()=='q':
        merusak
    elif  c . lebih rendah () ==  'l' :
        i  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        P ( " ╔═════════════════════════════════════╗" )
        P ( " ╠════════════DAFTAR KONTAK ═══════════╣" )
        P ( " ╠══════════════════╦══════════════════╣" )
        P ( " ║ NAMA ║ NOMOR ║" )
        P ( " ╠══════════════════╬══════════════════╬" )
        untuk  aku  di  aku :
            jika  l  ==  '' :
                lulus
            lain :
                l1  =  l . ganti ( 'Nama : ' , '' ). ganti ( 'Nomor : ' , '' ) =  l1 . strip (). pisahkan ( '|' )
                P (( ' ║ ' ) + ( na [: 15 ]). l just ( 17 , '.' ) + ( '║ ' ) + ( no ). l just ( 17 ) + ( '║ ' ))
        P ( " ╚═════════════════════════════════════╩══ ═══════╩═══════╩═══════╝" )
    elif  c . lebih rendah () ==  's' :
        cari  =  input ( ' Mencari : ' )
        i  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        P ( " ╔═════════════════════════════════════╗" )
        P ( " ╠════════════DAFTAR KONTAK ═══════════╣" )
        P ( " ╠══════════════════╦══════════════════╣" )
        P ( " ║ NAMA ║ NOMOR ║" )
        P ( " ╠══════════════════╬══════════════════╬" )
        untuk  aku  di  aku :
            jika  l  ==  '' :
                lulus
            elif  cari  di  l :
                l1  =  l . ganti ( 'Nama : ' , '' ). ganti ( 'Nomor : ' , '' ) =  l1 . strip (). pisahkan ( '|' )
                P (( ' ║ ' ) + ( na ). l just ( 17 ) + ( '║ ' ) + ( no ). l just ( 17 ) + ( '║ ' ))
        P ( " ╚═════════════════════════════════════╩══ ═══════╩═══════╩═══════╝" )
    elif  c . lebih rendah () ==  'd' :
        u  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        target  =  input ( 'Masukan Nama : ' )
        nm  = []
        untuk  aku  di dalam  kamu :
            jika  l  ==  '' :
                lulus
            lain :
                l1  =  l . ganti ( 'Nama : ' , '' ). ganti ( 'Nomor : ' , '' ) =  l1 . strip (). pisahkan ( '|' )
                jika  str ( na ) ==  str ( target ):
                    P ( 'BERHASIL MENGHAPUS Data %s' % ( target ))
                    lulus
                lain :
                    nm . tambahkan ( str ( l ) + ' \n ' )
        baru  =  buka ( 'database.txt' , 'w' )
        baru . tulis ( str ( nm ))
        baru . tutup ()
        baru  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        baru1  =  buka ( 'database.txt' , 'w' )
        baru1 . tutup ()
        new2  =  buka ( 'database.txt' , 'a' )
        untuk  saya  di  baru :
            i2  =  saya . ganti ( "['" , "" ). ganti ( " \\ n', '" , " \n " ). ganti ( "']" , "" ). ganti ( " \\ n" , '' )
            baru2 . tulis ( i2 )
        baru2 . tutup ()
    elif  c . rendah () ==  'e' :
        u  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        target  =  input ( 'Masukan Nama : ' )
        nm  = []
        untuk  aku  di dalam  kamu :
            jika  l  ==  '' :
                lulus
            lain :
                l1  =  l . ganti ( 'Nama : ' , '' ). ganti ( 'Nomor : ' , '' )
                na , tidak ada  =  l1 . strip (). pisahkan ( '|' )
                jika  na  ==  target :
                    P ( ' Mengedit Data %s' % ( target ))
                    sementara ( Benar ):
                        nama  =  input ( " Nama : " )
                        jika  nama  ==  '' :
                            P ( ' Dimasukkan Dengan Nama Dengan Benar' )
                        lain :
                            merusak
                    sementara ( Benar ):
                        coba :
                            nomor   =  int ( input ( " Nomor : " ))
                            jika  nomor  ==  '' :
                                P ( ' Masukan Nomor dengan Angka' )
                        kecuali  ValueError :
                            P ( ' Masukan Nomor dengan Angka' )
                        lain :
                            merusak
                    akhir  =  bulat (( float ( nomor ) *  0 )
                    edit   = ( 'Nama : ' + nama + '|Nomor : ' + str ( nomor ) + ' \n ' )
                    nm . tambahkan ( edit + ' \n ' )
                lain :
                    nm . tambahkan ( str ( l ) + ' \n ' )
        baru  =  buka ( 'database.txt' , 'w' )
        baru . tulis ( str ( nm ))
        baru . tutup ()
        baru  =  buka ( 'database.txt' , 'r' ). baca (). garis pemisah ()
        baru1  =  buka ( 'database.txt' , 'w' )
        baru1 . tutup ()
        new2  =  buka ( 'database.txt' , 'a' )
        untuk  saya  di  baru :
            i2  =  saya . ganti ( "['" , "" ). ganti ( " \\ n', '" , " \n " ). ganti ( "']" , "" ). ganti ( " \\ n" , " \n " )
            baru2 . tulis ( i2 + ' \n ' )
        baru2 . tutup ()
    elif  c . rendah () ==  'a' :
        i  =  buka ( 'database.txt' , 'a' )
        P ( " Tambah Kontak" )
        sementara ( Benar ):
            nama  =  input ( " Nama : " )
            jika  nama  ==  '' :
                P ( ' Dimasukkan Dengan Nama Dengan Benar' )
            lain :
                merusak
        sementara ( Benar ):
            coba :
                nomor   =  int ( input ( " NOMOR : " ))
                jika  nomor  ==  '' :
                    P ( ' Masukan Nomor dengan Angka' )
            kecuali  ValueError :
                P ( ' Masukan Nomor dengan Angka' )
            lain :
                merusak
        akhir  =  bulat (( float ( nomor ) *  0 )
        saya . tulis ( ' \n Nama : ' + nama + '|Nomor : ' + str ( nomor ) + ' \n ' )
        saya . tutup ()
        Ok ( "bersihkan" )
    lain :
        P ( "Pilih menu yang tersedia" )
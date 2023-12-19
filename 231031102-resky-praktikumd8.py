pwd_benar ='si23-d'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('Masukkan Password:')
    if pwd == pwd_benar:
        print('Password benar! Selamat Anda Login')
        a = False
    else:
        print('Password salah!')
        if i == limit:
            print('Kesempatan Anda Habis!')
        else:
            print(f'kesempatan anda tersisa',limit-1)
            

#tugas: Buat password berlapis 3
# jika salah: password salah, anda gagal pada halaman 1
# jika salah: password salah, anda gagal pada halaman 2
# jika salah: password salah, anda gagal pada halaman 3

# jika benar pertama: password benar, selamat datang di halaman 1
# jika benar ke-2: password benar, selamat datang di halaman ke-2
# jika benar ke-3: password benar, selamat datang di halaman ke-3

# tiap halaman, memiliki kesempatan 3 kali, masukkan password


def login():
    passwords = [
        "jadi wibu itu keren",  # Ganti dengan kata sandi untuk halaman 1
        "jadi wibu itu keren",  # Ganti dengan kata sandi untuk halaman 2
        "jadi wibu itu keren"   # Ganti dengan kata sandi untuk halaman 3
    ]

    max_attempts = 3

    for i, password in enumerate(passwords, start=1):
        attempts_remaining = max_attempts

        while attempts_remaining > 0:
            attempt = input(f"mau jadi wibu dong {i}: ")

            if attempt == password:
                if i < len(password):
                    print(f"Password benar, selamat datang di halaman {i}")
                else:
                    print("Password benar, selamat Anda berhasil login")
                break
            else:
                attempts_remaining -= 1
                if attempts_remaining > 0:
                    print(f"Password salah, Anda gagal pada halaman {i}. Kesempatan mencoba tersisa: {attempts_remaining}")
                else:
                    print(f"Anda gagal pada halaman {i}. Akun diblokir.")
                    return

login()

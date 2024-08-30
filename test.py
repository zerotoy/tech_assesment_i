def max_skills(j_skill, list_skills, list_bonus):
    pemain = sorted(zip(list_skills, list_bonus), key=lambda x: x[0])

    for skill, bonus in pemain:
        if j_skill >= skill:
            j_skill += bonus
        else:
            break
    return j_skill

if __name__ == "__main__":
    while True:
        try:
            total, skill = map(int, input("Masukkan jumlah lawan dan kemahiran awal Juned (N M): ").split())
            list_skills = list(map(int, input(f"Masukkan tingkat kemahiran {total} lawan: ").split()))
            list_bonus = list(map(int, input(f"Masukkan bonus kemahiran dari {total} lawan: ").split()))
        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan dua angka yang dipisahkan dengan spasi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")
        if len(list_skills)!=total:
            print("Anda salah memasukan jumlah kemahiran pemain. Silahkan coba lagi!")
            continue
        if len(list_bonus)!=total:
            print("Anda salah memasukan jumlah bonus pemain. Silahkan coba lagi!")
        result = max_skills( skill, list_skills, list_bonus)
        print(f"Tingkat kemahiran maksimal yang didapatkan Juned adalah: {result}")
        while True:
            retry = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
            if retry == 'y':
                break
            elif retry == 'n':
                print("Program selesai (⌐■_■)")
                exit()
            else:
                print("Pilihan tidak valid. Masukkan 'y' untuk mencoba lagi atau 'n' untuk keluar.")
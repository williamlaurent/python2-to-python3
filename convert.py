import subprocess
import sys
import lib2to3.main

# Perlu diingat bahwa konversi otomatis tidak selalu sempurna
# Kamu perlu memeriksa hasilnya secara manual.
# Pastikan untuk membuat salinan cadangan kode Anda sebelum mencoba konversi.

def convert_python2_to_python3(input_file, output_file=None):
    try:
        subprocess.check_call([sys.executable, "-m", "lib2to3", "-w", input_file])
        print(f"Kode Python 2 di {input_file} berhasil dikonversi ke Python 3.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Konversi kode Python 2 ke Python 3 gagal. Detail: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan: python converter.py <nama_file_input.py> [nama_file_output.py]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    convert_python2_to_python3(input_file, output_file)

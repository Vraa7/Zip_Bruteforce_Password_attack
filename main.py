import zipfile
import os

def extract_zip(zip_file_path, password_file_path, output_directory):
    try:
        with open(password_file_path, 'r', encoding='latin-1') as password_file:
            passwords = password_file.readlines()
    except FileNotFoundError:
        print(f"Error: File {password_file_path} tidak ditemukan.")
        return False
    except Exception as e:
        print(f"Error saat membuka file kata sandi: {e}")
        return False

    os.makedirs(output_directory, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file_path) as zip_file:
            for password in passwords:
                password = password.strip()  
                try:
                    zip_file.extractall(path=output_directory, pwd=password.encode('latin-1'))
                    print(f"File ZIP berhasil diekstrak dengan kata sandi: {password}")
                    return True
                except (RuntimeError, zipfile.BadZipFile):
                    continue  
                except Exception as e:
                    print(f"Error saat mencoba kata sandi '{password}': {e}")
                    continue  

        print("Kata sandi tidak ditemukan di dalam daftar.")
        return False
    
    except FileNotFoundError:
        print(f"Error: File {zip_file_path} tidak ditemukan.")
        return False
    except zipfile.BadZipFile:
        print(f"Error: File {zip_file_path} bukan file ZIP yang valid.")
        return False
    except Exception as e:
        print(f"Error saat membuka file ZIP: {e}")
        return False

def main():
    zip_file_path = 'nama_file.zip' 
    password_file_path = 'nama_wordlist.txt'  
    output_directory = 'extracted_files'  

    print(f"Mencoba mengekstrak {zip_file_path} dengan kata sandi dari {password_file_path}...")
    extract_zip(zip_file_path, password_file_path, output_directory)

if __name__ == '__main__':
    main()

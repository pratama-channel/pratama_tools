import os
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
from tqdm import tqdm
from time import sleep
import shutil

def install_zip():
    os.system("sudo apt update")
    os.system("sudo apt install -y zip")
    sleep(2)

def install_chrome():
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    result = os.system("sudo apt install -f -y")
    os.system("rm google-chrome-stable_current_amd64.deb")
    sleep(2)
    return result

def export_profile_link():
    link = "https://drive.google.com/file/d/12OXELzXTHuLcGmOQqZdlfRhj60PNvAcu/view?usp=drive_link"
    with open("profile_link.txt", "w") as f:
        f.write(link)

def extract_chrome_config():
    src_zip = "/home/user/Downloads/chrome_config.zip"
    dst_dir = "/home/user/.config/google-chrome/"
    if os.path.exists(src_zip) and os.path.exists(dst_dir):
        shutil.unpack_archive(src_zip, dst_dir)
        messagebox.showinfo("Copy Profile", "Ekstraksi berhasil.")
    else:
        messagebox.showerror("Error", "File chrome_config.zip atau direktori /home/user/.config/google-chrome/ tidak ditemukan.")

def open_chrome():
    os.system("google-chrome")

def kill_chrome():
    os.system("pkill chrome")

def clear_history_and_data():
    shutil.rmtree("/home/user/.config/google-chrome/Default")
    messagebox.showinfo("Clear History & Browsing Data", "History, cache, dan browsing data telah dihapus untuk semua profil Chrome.")

def uninstall_chrome():
    os.system("sudo apt-get purge google-chrome-stable")
    os.system("rm -rf /home/user/.config/google-chrome")
    messagebox.showinfo("Uninstall Chrome", "Chrome telah berhasil di-uninstall dan semua data pengguna dihapus.")

def show_progress_bar(func):
    progress_bar_window = tk.Toplevel()
    progress_bar_window.title("Progress")
    progress_bar_window.geometry("300x100")
    progress_label = tk.Label(progress_bar_window, text=f"Progress {func.__name__}", font=("Helvetica", 14))
    progress_label.pack(pady=10)

    progress_bar = tqdm(total=100, desc="", ncols=100, leave=False)

    def update_progress_bar():
        for _ in range(100):
            progress_bar.update(1)
            progress_bar_window.update()
            sleep(0.1)
        progress_bar.close()
        progress_bar_window.destroy()

    threading.Thread(target=func).start()
    threading.Thread(target=update_progress_bar).start()

def download_profile():
    export_profile_link()
    try:
        with open("profile_link.txt", "r") as f:
            link = f.read().strip()
            os.system(f"xdg-open '{link}'")
            messagebox.showinfo("Download Profil", "Copy link terus download di chrome")
    except FileNotFoundError:
        messagebox.showerror("Error", "File profile_link.txt tidak ditemukan.")

def install_zip_and_chrome():
    if os.path.exists("google-chrome-stable_current_amd64.deb"):
        os.remove("google-chrome-stable_current_amd64.deb")

    zip_result = install_zip()
    chrome_result = install_chrome()

    if chrome_result == 0:
        messagebox.showinfo("Instalasi Selesai", "Instalasi zip dan Google Chrome berhasil.")
    else:
        messagebox.showerror("Instalasi Gagal", "Instalasi zip dan Google Chrome gagal.")

def check_password_and_show_message(window):
    password = simpledialog.askstring("Password", "Masukkan password:", show="*")
    if password == "pratama":
        window.lift()  # Memastikan tampilan menu utama muncul di atas pop-up password
        messagebox.showinfo("Subscribe @Pratama__Channel", "Udah Subscribe Pratama Channel?")
        show_menu(window)
    else:
        messagebox.showerror("Error", "Password salah!")
        window.destroy()

def show_menu(window):
    window.destroy()

    menu_window = tk.Tk()
    menu_window.title("Menu Utama")
    menu_window.geometry("300x500")

    label = tk.Label(menu_window, text="Pilih opsi instalasi:", font=("Helvetica", 14))
    label.pack(pady=10)

    menu_items = [
        ("1. Install zip dan Google Chrome", install_zip_and_chrome),
        ("2. Download profil", download_profile),
        ("3. Copy Profile", extract_chrome_config),
        ("4. Buka Chrome", open_chrome),
        ("5. Kill Chrome", kill_chrome),
        ("6. Clear History & Browsing data", clear_history_and_data),
        ("7. Uninstall Chrome", uninstall_chrome),
    ]

    for menu_item in menu_items:
        button = tk.Button(menu_window, text=menu_item[0], command=lambda func=menu_item[1]: show_progress_bar(func))
        button.pack(pady=5, anchor=tk.W)

    footer_label = tk.Label(menu_window, text="Subscribe @Pratama__Channel", font=("Helvetica", 12))
    footer_label.pack(pady=20)

    menu_window.mainloop()

def display_menu():
    window = tk.Tk()
    window.title("Menu Instalasi")
    window.geometry("300x500")

    check_password_and_show_message(window)  # Menampilkan dialog untuk memasukkan password saat script pertama kali dijalankan

if __name__ == "__main__":
    display_menu()

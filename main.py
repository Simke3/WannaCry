import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Wana Decrypt0r 2.0")
window_width = 690
window_height = 470
root.focus_force()
root.grab_set()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

import ctypes

user32 = ctypes.windll.user32

def desktop_icons(show):
    progman = user32.FindWindowW("Progman", "Program Manager")
    desktop = user32.FindWindowExW(progman, 0, "SHELLDLL_DefView", None)

    if not desktop:
        worker = user32.FindWindowExW(0, 0, "WorkerW", None)
        while worker:
            desktop = user32.FindWindowExW(worker, 0, "SHELLDLL_DefView", None)
            if desktop:
                break
            worker = user32.FindWindowExW(0, worker, "WorkerW", None)

    icons = user32.FindWindowExW(desktop, 0, "SysListView32", None)

    if icons:
        user32.ShowWindow(icons, 5 if show else 0)
desktop_icons(False)

def close(event=None):
    desktop_icons(True)
    root.destroy()

root.bind("'", close)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)
root.configure(bg="#d58b91")
root.attributes("-topmost", True)
import os

korisnik = os.getlogin()

import ctypes

def promeni_pozadinu(slika):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, slika, 3
    )
promeni_pozadinu(r"C:\Users\{korisnik}\Downloads\WannaCry 2.0v\root\images.png ")
root.overrideredirect(True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.bind("<quoteright>", lambda event: root.destroy())


BG = "#8f1111"
DARK_RED = "#650909"
RED = "#a51212"
LIGHT_RED = "#c92a2a"
PINK = "#d58b91"
WHITE = "#ffffff"
YELLOW = "#ffe600"
GREEN = "#00d000"
BLACK = "#111111"

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

header = tk.Frame(root, bg="#d58b91", height=28)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="Wana Decrypt0r 2.0",
    font=("Arial", 10),
    fg="#333333",
    bg="#d58b91"
).pack(side="top", pady=5)

# ---------------------------------------------------------
# MAIN RED BACKGROUND
# ---------------------------------------------------------

main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True)

# ---------------------------------------------------------
# TOP TITLE
# ---------------------------------------------------------

title_frame = tk.Frame(main, bg=BG)
title_frame.place(x=185, y=2, width=418, height=25)

tk.Label(
    title_frame,
    text="Ooops, your files have been encrypted!",
    font=("Arial", 16, "bold"),
    fg=WHITE,
    bg=BG
).pack()

# ---------------------------------------------------------
# LANGUAGE
# ---------------------------------------------------------

language = tk.StringVar(value="English")

lang = tk.OptionMenu(
    main,
    language,
    "English",
    "Serbian",
    "Deutsch",
    "Español"
)

lang.config(
    font=("Arial", 8),
    width=8,
    height=1,
    bg=WHITE,
    fg=BLACK,
    bd=1,
    relief="solid"
)

lang["menu"].config(
    font=("Arial", 8)
)

lang.place(x=600, y=2)

# ---------------------------------------------------------
# LEFT PANEL
# ---------------------------------------------------------

left = tk.Frame(
    main,
    bg=DARK_RED,
    highlightbackground="#e9b1b1",
    highlightthickness=1
)

left.place(x=5, y=7, width=180, height=425)

# ---------------------------------------------------------
# LOCK ICON
# ---------------------------------------------------------

lock_box = tk.Frame(
    left,
    bg="#cfcfcf",
    width=95,
    height=95,
    highlightbackground=WHITE,
    highlightthickness=2
)

lock_box.place(x=35, y=5)
lock_box.pack_propagate(False)

canvas = tk.Canvas(
    lock_box,
    width=91,
    height=91,
    bg="#cfcfcf",
    highlightthickness=0
)

canvas.pack()

# red bottom section
canvas.create_rectangle(
    0, 45, 91, 91,
    fill="#b51b1b",
    outline=""
)
# lock shackle
canvas.create_arc(
    32, 10, 59, 43,
    start=0,
    extent=180,
    style="arc",
    width=7,
    outline="white"
)

canvas.create_line(
    32, 26,
    32, 40,
    fill="white",
    width=7
)

canvas.create_line(
    59, 26,
    59, 40,
    fill="white",
    width=7
)

# lock body
canvas.create_rectangle(
    25, 35, 66, 75,
    fill="white",
    outline="white"
)

# keyhole
canvas.create_oval(
    43, 47, 49, 53,
    fill="#a00000",
    outline=""
)

canvas.create_polygon(
    46, 51,
    42, 65,
    50, 65,
    fill="#a00000",
    outline=""
)

# ---------------------------------------------------------
# TIMER 1
# ---------------------------------------------------------

timer1_box = tk.Frame(
    left,
    bg="#8c1010",
    highlightbackground="#dba0a0",
    highlightthickness=1
)

timer1_box.place(x=5, y=107, width=168, height=108)

tk.Label(
    timer1_box,
    text="Payment will be raised on",
    font=("Arial", 10, "bold"),
    fg=YELLOW,
    bg="#8c1010"
).pack(pady=(7, 3))

tk.Label(
    timer1_box,
    text="2/1/2027 00:47:55",
    font=("Arial", 8, "bold"),
    fg=WHITE,
    bg="#8c1010"
).pack()

tk.Label(
    timer1_box,
    text="Time Left",
    font=("Arial", 9),
    fg=WHITE,
    bg="#8c1010"
).pack(pady=(7, 0))

timer1 = tk.Label(
    timer1_box,
    text="02:23:57:37",
    font=("Courier New", 17),
    fg=WHITE,
    bg="#8c1010"
)

timer1.pack()

# green indicator
tk.Frame(
    timer1_box,
    bg=GREEN,
    width=10,
    height=35
).place(x=145, y=28)

# ---------------------------------------------------------
# TIMER 2
# ---------------------------------------------------------

timer2_box = tk.Frame(
    left,
    bg="#8c1010",
    highlightbackground="#dba0a0",
    highlightthickness=1
)

timer2_box.place(x=5, y=220, width=168, height=108)

tk.Label(
    timer2_box,
    text="Your files will be lost on",
    font=("Arial", 10, "bold"),
    fg=YELLOW,
    bg="#8c1010"
).pack(pady=(7, 3))

tk.Label(
    timer2_box,
    text="2/1/2027 00:47:55",
    font=("Arial", 8, "bold"),
    fg=WHITE,
    bg="#8c1010"
).pack()

tk.Label(
    timer2_box,
    text="Time Left",
    font=("Arial", 9),
    fg=WHITE,
    bg="#8c1010"
).pack(pady=(7, 0))

timer2 = tk.Label(
    timer2_box,
    text="06:23:57:37",
    font=("Courier New", 17),
    fg=WHITE,
    bg="#8c1010"
)

timer2.pack()

tk.Frame(
    timer2_box,
    bg=GREEN,
    width=10,
    height=35
).place(x=145, y=28)

# ---------------------------------------------------------
# LEFT LINKS
# ---------------------------------------------------------

tk.Label(
    left,
    text="About bitcoin",
    font=("Arial", 8, "underline"),
    fg=WHITE,
    bg=DARK_RED,
    cursor="hand2"
).place(x=18, y=350)

tk.Label(
    left,
    text="How to buy bitcoins?",
    font=("Arial", 8, "underline"),
    fg=WHITE,
    bg=DARK_RED,
    cursor="hand2"
).place(x=18, y=374)

tk.Label(
    left,
    text="Contact Us",
    font=("Arial", 10, "bold", "underline"),
    fg="#8eeaff",
    bg=DARK_RED,
    cursor="hand2"
).place(x=18, y=398)

# ---------------------------------------------------------
# RIGHT TEXT AREA
# ---------------------------------------------------------

text_frame = tk.Frame(
    main,
    bg=WHITE,
    highlightbackground="#dddddd",
    highlightthickness=1
)

text_frame.place(x=190, y=28, width=502, height=296)

scroll = tk.Scrollbar(text_frame)
scroll.pack(side="right", fill="y")

info = tk.Text(
    text_frame,
    wrap="word",
    font=("Arial", 12),
    bg=WHITE,
    fg=BLACK,
    bd=0,
    relief="flat",
    yscrollcommand=scroll.set
)

scroll.config(command=info.yview)

info.pack(fill="both", expand=True)

info.tag_config("bold_stil", font=("TkDefaultFont", 13, "bold"))
info.insert("end", "What Happened to My Computer?\n", "bold_stil")
info.insert(
    "end",
    "Your important files are encrypted.\n"
    "Many of your documents, photos, videos, databases and other files "
    "are no longer accessible because they have been encrypted.\n"
    "Nobody can recover your files without the required decryption information.\n\n"
)

info.insert("end", "Can I Recover My Files?\n", "bold_stil")
info.insert(
    "end",
    "You can recover your files using the appropriate decryption process.\n"
    "Please follow the instructions shown below.\n"
    "Do not close this window until you have finished reading the information.\n\n"
)

info.insert("end", "How Do I Pay?\n", "bold_stil")
info.insert(
    "end",
    "Payment information is displayed in the panel below.\n"
    "The amount shown is fictional and does not represent a real payment.\n"
    "Use the buttons below to interact with this interface.\n\n"
)

info.config(state="disabled")

# ---------------------------------------------------------
# BITCOIN AREA
# ---------------------------------------------------------

payment = tk.Frame(
    main,
    bg="#8c1010",
    highlightbackground="#e0a0a0",
    highlightthickness=1
)

payment.place(x=190, y=326, width=418, height=62)

# Bitcoin logo box
btc_logo = tk.Frame(
    payment,
    bg=WHITE,
    width=105,
    height=48
)

btc_logo.place(x=4, y=5)
btc_logo.pack_propagate(False)

tk.Label(
    btc_logo,
    text="₿",
    font=("Arial", 20, "bold"),
    fg="#f5a623",
    bg=WHITE
).place(x=5, y=4)

tk.Label(
    btc_logo,
    text="bitcoin",
    font=("Arial", 15, "bold", "italic"),
    fg="#777777",
    bg=WHITE
).place(x=29, y=3)

tk.Label(
    btc_logo,
    text="ACCEPTED HERE",
    font=("Arial", 6, "bold"),
    fg="#777777",
    bg=WHITE
).place(x=29, y=29)

# Payment text
tk.Label(
    payment,
    text="Send $300 worth of bitcoin to this address:",
    font=("Arial", 9, "bold"),
    fg=YELLOW,
    bg="#8c1010"
).place(x=113, y=4)

# Fake BTC address
btc_entry = tk.Entry(
    payment,
    font=("Arial", 9, "bold"),
    bg="#7c0b0b",
    fg=WHITE,
    insertbackground=WHITE,
    bd=1,
    relief="solid"
)

btc_entry.place(x=115, y=26, width=267, height=23)

btc_entry.insert(
    0,
    "7bc77yf868eg659dfh3e779fghr"
)

btc_entry.config(state="readonly")

def copy_address():
    root.clipboard_clear()
    root.clipboard_append("1FakeBTCAddress7F92A0DEMO")
    copy_btn.config(text="Copied")
    root.after(1200, lambda: copy_btn.config(text="Copy"))

copy_btn = tk.Button(
    payment,
    text="Copy",
    command=copy_address,
    font=("Arial", 8),
    bg="#eeeeee",
    fg=BLACK,
    bd=1,
    relief="raised"
)

copy_btn.place(x=385, y=26, width=29, height=23)

# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------

def check_payment():
    messagebox.showinfo(
        "Payment",
        "No payment detected."
    )

def decrypt():
    decrypt_window = tk.Toplevel(root)
    decrypt_window.title("Wana Decrypt0r")
    decrypt_window.geometry("500x250")
    decrypt_window.resizable(False, False)
    decrypt_window.configure(bg="#8f1111")

    tk.Label(
        decrypt_window,
        text="Decrypt",
        font=("Arial", 22, "bold"),
        fg=WHITE,
        bg="#8f1111"
    ).pack(pady=25)

    tk.Label(
        decrypt_window,
        text="Enter the decryption information:",
        font=("Arial", 11),
        fg=WHITE,
        bg="#8f1111"
    ).pack()

    entry = tk.Entry(
        decrypt_window,
        width=45,
        font=("Arial", 10)
    )

    entry.pack(pady=15)

    tk.Button(
        decrypt_window,
        text="Decrypt",
        font=("Arial", 11, "bold"),
        width=18,
        command=lambda: messagebox.showinfo(
            "Decrypt",
            "Wrong key!"
        )
    ).pack()

    tk.Button(
        decrypt_window,
        text="Close",
        command=decrypt_window.destroy,
        width=18
    ).pack(pady=10)

check_btn = tk.Button(
    main,
    text="Check Payment",
    font=("Arial", 11, "bold"),
    bg="#eeeeee",
    fg=BLACK,
    bd=1,
    relief="raised",
    command=check_payment
)

check_btn.place(x=200, y=391, width=195, height=23)

decrypt_btn = tk.Button(
    main,
    text="Decrypt",
    font=("Arial", 11, "bold"),
    bg="#eeeeee",
    fg=BLACK,
    bd=1,
    relief="raised",
    command=decrypt
)

decrypt_btn.place(x=399, y=391, width=195, height=23)

# ---------------------------------------------------------
# FAKE COUNTDOWN
# ---------------------------------------------------------

seconds = 2 * 24 * 60 * 60 + 23 * 3600 + 57 * 60 + 37

def update_timer():
    global seconds

    if seconds > 0:
        seconds -= 1

    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    timer1.config(
        text=f"{days:02d}:{hours:02d}:{minutes:02d}:{secs:02d}"
    )

    root.after(1000, update_timer)

update_timer()

root.mainloop()



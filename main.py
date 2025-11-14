import tkinter as tk
import json
import os
import time
import random

def initialization_ui():
    """
    Initialization UI settings
    """
    ui.title("Japanese Learning Helper")
    ui.iconbitmap("icon.ico")
    ui.resizable(False, False)
    ui.configure(bg="#dcdde1")

def set_screen_size(width, height):
    """
    Set the screen size
    """
    try:
        left = int((ui.winfo_screenwidth() - width) / 2)
        top = int((ui.winfo_screenheight() - height) / 2)
        ui.geometry(f"{width}x{height}+{left}+{top}")
    except Exception as e:
        print(f"[{debug_get_time()}] ERROR: set_screen_size\n{e}")

def clear_screen():
    """
    Clear all things of the UI
    """
    for i in ui.winfo_children():
        i.destroy()

def debug_get_time():
    """
    DEBUG
    """
    now = time.time()
    local_time = time.strftime("%H:%M:%S",time.localtime(now))
    ms = int((now - int(now)) * 1000)
    return f"{local_time}:{ms:03d}"

def load_data():
    """
    Load file
    """
    global HKR_dict, HKR_list
    HKR_dict = {"h": {}, "k": {}, "r": {}}
    HKR_list = {"h": [], "k": [], "r": []}
    files = {"hiragana_to_romaji.json": "h",
            "katakana_to_romaji.json": "k",
            "romaji_to_kana.json": "r",
            "HKR_list.txt": "list",}
    try:
        for fname, key in files.items():
            path = os.path.join(os.getcwd(), "data", fname)
            with open(path, "r", encoding="utf-8") as f:
                if fname.endswith(".json"):
                    HKR_dict[key] = json.load(f)
                elif fname.endswith(".txt"):
                    lines = []
                    for line in f:
                        line = line.strip()
                        if line:
                            lines.append(line)
                    if len(lines) >= 3:
                        HKR_list["h"] = lines[0].split(",")
                        HKR_list["k"] = lines[1].split(",")
                        HKR_list["r"] = lines[2].split(",")
    except Exception as e:
        print(f"[{debug_get_time()}] ERROR: load_data\n{e}")

def page_mode():
    """
    Main page of the tool
    """
    set_screen_size(640, 480)
    clear_screen()
    tk.Label(ui, text="=Choose The Mode=", font=("Microsoft YaHei",25,"bold"), bg="#dcdde1").pack(fill="x", side="top", pady=5)
    
    modes = tk.Frame(ui, bg="#dcdde1")
    line1 = tk.Frame(modes, bg="#dcdde1")
    tk.Button(line1, text="Guess Romaji from Hiragana", font=("Microsoft YaHei",12), width=24, height=2, command=page_GRFH).pack(side="left", pady=10, padx=20)
    tk.Button(line1, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line1.pack()
    
    line2 = tk.Frame(modes, bg="#dcdde1")
    tk.Button(line2, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line2, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line2.pack()
    
    line3 = tk.Frame(modes, bg="#dcdde1")
    tk.Button(line3, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line3, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line3.pack()
    
    line4 = tk.Frame(modes, bg="#dcdde1")
    tk.Button(line4, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line4, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line4.pack()
    
    line5 = tk.Frame(modes, bg="#dcdde1")
    tk.Button(line5, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line5, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line5.pack()
    modes.pack()

def page_GRFH():
    def ramdom():
        """
        For ready the answer and options
        """
        answer_H = random.choice(HKR_list["h"])
        text_H.set(answer_H)
        options = [HKR_dict["h"][answer_H]]
        while len(options) < 4:
            temp = random.choice(HKR_list["h"])
            if temp != answer_H and temp not in options:
                options.append(HKR_dict["h"][temp])
        random.shuffle(options)
        for i in range(4):
            text_ans[i].set(options[i])
    def check(choice):
        """
        For check the answer
        """
        nonlocal correct_times, wrong_times
        real_answer = HKR_dict["h"][text_H.get()]
        if choice == real_answer:
            correct_times += 1
        else:
            wrong_times += 1
        ramdom()
        text_scores.set(f"✔{correct_times} ✘{wrong_times}")
    """
    Mode page : Guess Romaji from Hiragana
    """
    text_H = tk.StringVar()
    text_scores = tk.StringVar()
    text_ans = []
    for i in range(4):
        text_ans.append(tk.StringVar())
    wrong_times = 0
    correct_times = 0
    set_screen_size(640, 480)
    clear_screen()
    ramdom()
    tk.Label(ui, text="=Guess Romaji from Hiragana=", font=("Microsoft YaHei",25,"bold"), bg="#dcdde1").pack(fill="x", side="top", pady=5)
    
    tk.Label(ui, textvariable=text_H, font=("Microsoft YaHei",80), relief="solid", bd=5, width=2, height=1).pack(side="top", pady=10)
    
    scores = tk.Frame(ui, bg="#dcdde1")
    tk.Label(scores, textvariable=text_scores, font=("Microsoft YaHei",20),bg="#dcdde1").pack(side="top")
    scores.pack(side="top")
    
    options = tk.Frame(ui, bg="#dcdde1")
    tk.Button(options, textvariable=text_ans[0], font=("Microsoft YaHei",28), relief="raised", bd=5, width=4, height=1, command=lambda:check(text_ans[0].get())).pack(side="left", pady=5, padx=20)
    tk.Button(options, textvariable=text_ans[1], font=("Microsoft YaHei",28), relief="raised", bd=5, width=4, height=1, command=lambda:check(text_ans[1].get())).pack(side="left", pady=5, padx=20)
    tk.Button(options, textvariable=text_ans[2], font=("Microsoft YaHei",28), relief="raised", bd=5, width=4, height=1, command=lambda:check(text_ans[2].get())).pack(side="left", pady=5, padx=20)
    tk.Button(options, textvariable=text_ans[3], font=("Microsoft YaHei",28), relief="raised", bd=5, width=4, height=1, command=lambda:check(text_ans[3].get())).pack(side="left", pady=5, padx=20)
    options.pack(side="top")
    
    btn = tk.Frame(ui, bg="#dcdde1")
    tk.Button(btn, text="=RESET=", font=("Microsoft YaHei",20), relief="raised", bd=2, width=10, height=1, command=ramdom).pack(side="left", padx=40)
    tk.Button(btn, text="=RETURN=", font=("Microsoft YaHei",20), relief="raised", bd=2, width=10, height=1, command=page_mode).pack(side="left", padx=40)
    btn.pack(side="top", pady=15)


def MAIN():
    """
    Main
    """
    global ui
    ui = tk.Tk()
    initialization_ui()
    load_data()
    page_mode()
    ui.mainloop()

if __name__ == "__main__":
    MAIN()
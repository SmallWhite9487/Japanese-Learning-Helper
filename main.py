import tkinter as tk
import json
import os
import time
import random
import sys

def initialization_ui():
    """
    Initialization UI settings
    """
    ui.title("Japanese Learning Helper")
    ui.iconbitmap(resource_path("icon.ico"))
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

def resource_path(relative_path):
    """
    Get file path
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

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
            path = resource_path(os.path.join("data", fname))
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

def page_difficulty(to_mode):
    """
    Difficulty selection page
    """
    def process(difficulty):
        nonlocal to_mode
        if to_mode in ("RFH","RFK"):
            to_mode = page_RFHK(to_mode,difficulty)
        else:
            page_mode()
    set_screen_size(560, 380)
    clear_screen()

    tk.Label(ui, text="=Choose The Difficulty=", font=("Microsoft YaHei",25,"bold"), bg="#dcdde1").pack(fill="x", side="top", pady=5)
    
    tk.Button(ui, text="Easy", font=("Microsoft YaHei",16,"bold"), width=24, height=2, command=lambda:process("e")).pack(side="top", pady=10, padx=20)
    tk.Button(ui, text="Medium", font=("Microsoft YaHei",16,"bold"), width=24, height=2, command=lambda:process("m")).pack(side="top", pady=10, padx=20)
    tk.Button(ui, text="Hard", font=("Microsoft YaHei",16,"bold"), width=24, height=2, command=lambda:process("h")).pack(side="top", pady=10, padx=20)

def page_mode():
    """
    Main page of the tool
    """
    set_screen_size(640, 480)
    clear_screen()
    tk.Label(ui, text="=Choose The Mode=", font=("Microsoft YaHei",25,"bold"), bg="#dcdde1").pack(fill="x", side="top", pady=5)
    
    line1 = tk.Frame(ui, bg="#dcdde1")
    tk.Button(line1, text="Guess Romaji from Hiragana", font=("Microsoft YaHei",12), width=24, height=2, command=lambda:page_difficulty("RFH")).pack(side="left", pady=10, padx=20)
    tk.Button(line1, text="Guess Romaji from Katakana", font=("Microsoft YaHei",12), width=24, height=2, command=lambda:page_difficulty("RFK")).pack(side="left", pady=10, padx=20)
    line1.pack()
    
    line2 = tk.Frame(ui, bg="#dcdde1")
    tk.Button(line2, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line2, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line2.pack()
    
    line3 = tk.Frame(ui, bg="#dcdde1")
    tk.Button(line3, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line3, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line3.pack()
    
    line4 = tk.Frame(ui, bg="#dcdde1")
    tk.Button(line4, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line4, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    line4.pack()
    
    line5 = tk.Frame(ui, bg="#dcdde1")
    tk.Button(line5, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_mode).pack(side="left", pady=10, padx=20)
    tk.Button(line5, text="***", font=("Microsoft YaHei",12), width=24, height=2, command=page_difficulty).pack(side="left", pady=10, padx=20)
    line5.pack()

def page_RFHK(mode="RFH",difficulty="e"):
    """
    Mode page : Guess Romaji from Hiragana/Katakana
    """
    def ramdom():
        answer = random.choice(temp_list)
        text_guess.set(answer)
        options = [temp_dict[answer]]
        while len(options) < 4:
            temp = random.choice(temp_list)
            if temp != answer and temp not in options:
                options.append(temp_dict[temp])
        random.shuffle(options)
        for i in range(4):
            text_ans[i].set(options[i])
    def check(choice):
        nonlocal correct_times, wrong_times
        real_answer = temp_dict[text_guess.get()]
        if choice == real_answer:
            correct_times += 1
        else:
            wrong_times += 1
        ramdom()
        text_scores.set(f"✔{correct_times} ✘{wrong_times}")

    temp_list = HKR_list["h"]
    temp_dict = HKR_dict["h"]
    title = "=Guess Romaji from Hiragana="
    if mode == "RFK":
        temp_list = HKR_list["k"]
        temp_dict = HKR_dict["k"]
        title = "=Guess Romaji from Katakana="

    text_guess = tk.StringVar()
    text_scores = tk.StringVar()
    text_ans = []
    for i in range(4):
        text_ans.append(tk.StringVar())

    wrong_times = 0
    correct_times = 0
    set_screen_size(640, 480)
    clear_screen()
    ramdom()
    tk.Label(ui, text=title, font=("Microsoft YaHei",25,"bold"), bg="#dcdde1").pack(fill="x", side="top", pady=5)
    tk.Label(ui, textvariable=text_guess, font=("Microsoft YaHei",80), relief="solid", bd=5, width=2, height=1).pack(side="top", pady=10)
    
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
    tk.Button(btn, text="=RESET=", font=("Microsoft YaHei",20), relief="raised", bd=2, width=10, height=1, command=page_RFHK).pack(side="left", padx=40)
    tk.Button(btn, text="=RETURN=", font=("Microsoft YaHei",20), relief="raised", bd=2, width=10, height=1, command=page_mode).pack(side="left", padx=40)
    btn.pack(side="top", pady=15)

def MAIN():
    """
    君指先跃动の光は、私の一生不変の信仰に、唯私の超電磁砲永世生き！
    """
    global ui
    ui = tk.Tk()
    initialization_ui()
    load_data()
    page_mode()
    ui.mainloop()

if __name__ == "__main__":
    MAIN()
import tkinter as tk
import random

kuji = ["大吉", "中吉", "小吉", "凶"]

def draw_kuji():
    result = random.choice(kuji)
    label_result.config(text=result)

# ウィンドウを作成

root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("800x600")

# タイトル

label_title = tk.Label(root, text="おみくじ", font=("Arial", 20))
label_title.pack(pady=10)

# 結果表示

label_result = tk.Label(root, text="ボタンを押してね", font=("Arial", 16))
label_result.pack(pady=10)

# ボタン

button = tk.Button(root, text="おみくじを引く", command=draw_kuji)
button.pack(pady=10)

root.mainloop()
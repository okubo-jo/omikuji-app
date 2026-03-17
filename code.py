import tkinter as tk
import random

kuji = ["超大吉", "大吉", "中吉", "小吉", "凶"]

#コメントを表示
comments = {
    "超大吉": "奇跡レベルの運勢です！",
    "大吉": "最高の一日になります！",
    "中吉": "良いことが起きるかも",
    "小吉": "小さなラッキーがあるかも",
    "凶": "今日は慎重に行動しよう……"
}
    
def draw_kuji():
    result = random.choice(kuji)

    if result == "超大吉":
        label_result.config(text=result, fg="gold")
    else:
        label_result.config(text=result, fg="black")
    
    label_comment.config(text=comments[result])

# ウィンドウを作成

root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("800x600")
root.configure(bg="#ffe4e4")

# タイトルの表示

label_title = tk.Label(root, text="おみくじ", font=("Arial", 20), bg="#ffe4e4")
label_title.pack(pady=10)

# 結果の表示

label_result = tk.Label(root, text="ボタンを押してね", font=("Arial", 35), bg="#ffe4e4")
label_result.pack(pady=10)
label_comment = tk.Label(root, text="", font=("Arial", 18), bg="#ffe4e4")
label_comment.pack(pady=10)

# ボタンの表示

button = tk.Button(
    root, 
    text="おみくじを引く", 
    command=draw_kuji,
    font=("Arial", 20),
    width=12,
    height=2
)
button.pack(pady=10)

root.mainloop()
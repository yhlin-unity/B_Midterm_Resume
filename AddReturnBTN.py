import os

# 請將此腳本放在「期中作品」資料夾下執行
root_dir = "."

back_button_html = '''
<!-- 自動注入返回主頁按鈕 -->
<style>
  .auto-back-btn {
    position: fixed;
    top: 16px;
    left: 16px;
    z-index: 99999;
    background: #2563eb;
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 9999px;
    text-decoration: none;
    font-family: sans-serif;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    transition: transform 0.2s;
  }
  .auto-back-btn:hover { transform: translateY(-2px); background: #1d4ed8; }
</style>
<a href="../index.html" class="auto-back-btn">← 返回作品總覽主頁</a>
'''

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        student_html = os.path.join(folder_path, "index.html")
        if os.path.exists(student_html):
            with open(student_html, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # 若尚未注入過返回按鈕，則在 <body> 後插入
            if "auto-back-btn" not in content:
                if "<body" in content.lower():
                    # 在 <body> 標籤開頭後插入
                    idx = content.lower().find(">", content.lower().find("<body")) + 1
                    new_content = content[:idx] + back_button_html + content[idx:]
                else:
                    new_content = back_button_html + content

                with open(student_html, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"已更新: {student_html}")

print("全部學生 index.html 返回按鈕注入完成！")
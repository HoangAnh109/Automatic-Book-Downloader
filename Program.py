# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BRYH-ELjnsCmXNUEWbx08FULADCFJ2Vy
"""

import pandas as pd
import requests
import os

# Nhập đường dẫn thư mục từ người dùng
folder = input("Nhập đường dẫn thư mục: ")

# Đọc file excel
df = pd.read_excel('LABELLED DATA.xlsx', engine='openpyxl')

# Tạo danh sách lưu các STT không tải được file PDF
khong_tai_duoc = []

# Kiểm tra và tạo thư mục nếu nó không tồn tại
if not os.path.exists(folder):
    os.makedirs(folder)

for index, row in df.iterrows():
    url = row['Link download']
    stt = row['Id']

    try:
        # Gửi yêu cầu GET đến URL
        response = requests.get(url)

        id = f'{stt}'.zfill(3)

        with open(os.path.join(folder, f"{id}.pdf"), 'wb') as f:
              f.write(response.content)

    except Exception as e:
        print(f"Lỗi khi tải file PDF từ {url}: {str(e)}")
        khong_tai_duoc.append(stt)

# Lưu danh sách các STT không tải được file PDF
with open('khong_tai_duoc.txt', 'w') as f:
    for stt in khong_tai_duoc:
        f.write(f"{stt}\n")
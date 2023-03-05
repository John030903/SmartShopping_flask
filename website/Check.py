import os

# Kiểm tra quyền truy cập vào file
if os.access('model.sav', os.R_OK):
    print("Bạn có quyền truy cập vào file model.sav")
else:
    print("Bạn không có quyền truy cập vào file model.sav")

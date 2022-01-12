import tkinter as tk  # 使用Tkinter前需要先匯入
from tkinter import filedialog
from PIL import Image
import os
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *

style = Style(theme='darkly')

window = style.master
# 例項化object，建立視窗window


# 標題
window.title('Transfer Software By.TabEtuc')

# 設定視窗的大小(長 * 寬)
window.geometry('500x150')  # 這裡的乘是小x


def ImportBrowseFiles():
    global ImportFile
    ImportFile = filedialog.askdirectory(initialdir = "/",
                                          title = "請選取一個資料夾",
                                          )
      
    # Change label contents
    button_Import.configure(text="已選取來源檔案路徑："+ImportFile)

def ExportBrowseFiles():
    global ExportFile
    ExportFile = filedialog.askdirectory(initialdir = "/",
                                          title = "請選取一個資料夾",
                                          )
      
    # Change label contents
    button_Export.configure(text="已輸出選取檔案路徑："+ExportFile)
def Enter():
    try:
        for imageName in os.listdir(ImportFile):
            imagePath = os.path.join(ImportFile, imageName)
            image = Image.open(imagePath)
            distImagePath = os.path.join(ExportFile, imageName[:-4] + '.jpg')
            print(imagePath)
            image.save(distImagePath)
    except NameError as err:
        if "ImportFile" in str(err): 
            ttk.dialogs.Messagebox(
                
            ).show_warning("請確認您已選擇來源資料夾",
                title='錯誤')
        elif "ExportFile" in str(err): 
            ttk.dialogs.Messagebox(
                
            ).show_warning("請確認您已選擇輸出資料夾",
                title='錯誤')
    except Exception as other:
        if "Permission denied" in str(other): 
            return ttk.dialogs.Messagebox(

                
            ).show_warning("缺少權限！請使用「以系統管理員身分執行」後再試一次。",
                title='錯誤')
        ttk.dialogs.Messagebox(
                
            ).show_warning("發生其他問題：{other}")


button_Import = ttk.Button(window,
                        text = "請選擇來源資料夾",
                        command = ImportBrowseFiles, 
                        bootstyle=(
                            INFO, OUTLINE
                        )
                )
button_Import.pack(side=TOP, padx=5, pady=10)
button_Export = ttk.Button(window,
                        text = "請選擇輸出資料夾",
                        command = ExportBrowseFiles,
                        bootstyle=(
                            INFO, OUTLINE
                        )
                )
button_Export.pack(side=TOP, padx=5, pady=10)
button_Enter = ttk.Button(window,
                        text = "轉換！",
                        command = Enter,
                        bootstyle=SUCCESS
                ).pack(side=TOP, padx=5, pady=10)
# 主視窗鎖定大小
window.resizable(width=False, height=False)
# 主視窗迴圈顯示
window.mainloop()

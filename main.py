import eel
import tkinter as tk
import tkinter.filedialog as filedialog

eel.init('asset')

@eel.expose
def choose_file():
    print('choose')
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.wm_withdraw()
    path = filedialog.askopenfilename(filetypes=[('mp4', '*.mp4'), ('All files', '*.*')])
    root.destroy()

    return path


eel.start('index.html', port=15000)
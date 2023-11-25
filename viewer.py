import ttkbootstrap as ttk
from pathlib import Path
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

PATH = Path(__file__).parent / 'resource'

# root.mainloop()

class bianjiqi(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        # 图片
        self.images = [
            ttk.PhotoImage(
                name='jiedian',
                file=PATH / 'jiedian.png'),
            ttk.PhotoImage(
                name='ganjian',
                file=PATH / 'ganjian.png'),
            ttk.PhotoImage(
                name='yueshu',
                file=PATH / 'yueshu.png'),
            ttk.PhotoImage(
                name='hezai',
                file=PATH / 'hezai.png'),
            ttk.PhotoImage(
                name='cailiao',
                file=PATH / 'cailiao.png'),
        ]

        # 表头
        top_frame = ttk.Frame(self, padding=5, style=SECONDARY)
        top_frame, grid(row=0, column=0, columnspan=5, sticky=EW)

        top_label = ttk.Label(
            master=top_frame,
        )
        top_label.pack(side=LEFT)

        # 命令栏
        mingling_frame = ttk.Frame(self)
        mingling_frame.grid(row=0, column=0, sticky=EW)

        wenjian = ttk.Button(
            master=mingling_frame,
            text='文件',
            style=SECONDARY
        )
        wenjian.pack(side=TOP, fill=BOTH,)















if __name__ == '__main__':

    app = ttk.Window("PC Cleaner", "pulse")
    bianjiqi(app)
    app.mainloop()























# root = tk.Window(themename='litera')
# root.geometry('800x900+850+50')
# root.title('编辑器')
# root.wm_attributes('-topmost', 0)
#
# frame1 = tk.Frame(root)
# frame1.pack()
#
# frame2 = tk.Frame(root)
# frame2.pack()
#
# img_jiedian = tk.PhotoImage(file='resource/jiedian.png')
# label_img_jiedian = tk.Label(frame1, image=img_jiedian)
# label_img_jiedian.pack(side=tk.LEFT, anchor=tk.N, padx=0, pady=0)
# label_img_jiedian1 = tk.Label(frame1, image=img_jiedian)
# label_img_jiedian1.pack(side=tk.LEFT, anchor=tk.N, padx=0, pady=100)

# jiedian = tk.StringVar()
# ganjian = tk.StringVar()





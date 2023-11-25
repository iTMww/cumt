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
        top_frame.grid(row=0, column=0, columnspan=5, sticky=EW)

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







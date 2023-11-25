import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from pathlib import Path
from ttkbootstrap.constants import *
from ttkbootstrap.style import Bootstyle
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

        ## 表头
        biaotou = ttk.Menu(app)
        app.config(menu=biaotou)

        ### 文件
        wenjian = ttk.Menu(biaotou)
        wenjian.add_command(label='新建')
        wenjian.add_command(label='打开')
        wenjian.add_command(label='关闭')
        wenjian.add_command(label='保存')
        wenjian.add_command(label='另存为')
        biaotou.add_cascade(label='文件(F)', menu=wenjian)


        ## 编辑
        bianji = ttk.Menu(biaotou)
        bianji.add_command(label='还原')
        bianji.add_command(label='剪切')
        bianji.add_command(label='复制')
        bianji.add_command(label='粘贴')
        bianji.add_command(label='清除')
        biaotou.add_cascade(label='编辑(E)',menu=bianji)

        ## 命令
        mingling = ttk.Menu(biaotou)
        mingling.add_command(label='结点')
        mingling.add_command(label='杆件')
        mingling.add_command(label='约束')
        mingling.add_command(label='荷载')
        mingling.add_command(label='材料')
        biaotou.add_cascade(label='命令(C)', menu=mingling)

        ## 求解
        qiujie = ttk.Menu(biaotou)
        qiujie.add_command(label='几何组成')
        qiujie.add_command(label='内力计算')
        qiujie.add_command(label='位移计算')
        qiujie.add_command(label='位移内力')
        biaotou.add_cascade(label='求解(S)', menu=qiujie)

        # 工具栏
        gongju = ttk.Frame(self)





        # # 表头
        # top_frame = ttk.Frame(self, padding=5, bootstyle=SECONDARY)
        # top_frame.grid(row=0, column=0, columnspan=5, sticky=EW)
        #
        # top_label = ttk.Label(
        #     master=top_frame,
        #     style=SECONDARY
        # )
        # top_label.pack(fill=Y, pady=1, side=TOP)

        # 命令栏
        mingling_frame = ttk.Frame(self)
        mingling_frame.grid(row=0, column=0, sticky=NSEW)

        wenjian = ttk.Button(
            master=mingling_frame,
            image='jiedian',
            style=LIGHT
        )
        wenjian.pack(side=TOP, fill=BOTH)

        bianji = ttk.Button(
            master=mingling_frame,
            text='编辑',
            style=(DARK,OUTLINE)
        )
        bianji.pack(side=TOP, fill=BOTH)

        chakan = ttk.Button(
            master=mingling_frame,
            text='查看',
            style=(SECONDARY,OUTLINE)
        )
        chakan.pack(side=TOP, fill=BOTH)

        mingling = ttk.Button(
            master=mingling_frame,
            text='命令',
            style=(SECONDARY, OUTLINE)
        )
        mingling.pack(side=TOP, fill=BOTH)

        qiujie = ttk.Button(
            master=mingling_frame,
            text='求解',
            style=(SECONDARY, OUTLINE)
        )
        qiujie.pack(side=LEFT, fill=BOTH)














if __name__ == '__main__':

    app = ttk.Window("PC Cleaner", "pulse")
    bianjiqi(app)
    app.mainloop()







from tkinter import *

from views.gui.gerir import produtos


# Menu do adiministrador
class AdminMenu:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(False, False)
        top.title("Sistema de Gestao de vendas")
        top.iconbitmap("public/imagens/shopping_cart.ico")

        self.label1 = Label(admMenu)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img2 = PhotoImage(file='public/imagens/menuBG.png')
        self.label1.configure(image=self.img2)

        self.lblUser = Label(admMenu, text="Administrador")
        self.lblUser.place(relx=0.046, rely=0.056, width=105, height=30)
        self.lblUser.configure(font="-family {Calibri} -size 12")
        self.lblUser.configure(background="#FE6B61", foreground="#ffffff")

        self.imgBtnProdutos = PhotoImage(file='public/imagens/btnProdutos.png')
        self.btnProdutos = Button(admMenu, image=self.imgBtnProdutos, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnProdutos.place(relx=0.14, rely=0.4, width=150, height=150)
        self.btnProdutos.configure(borderwidth="0", cursor="hand2")
        self.btnProdutos.configure(command=btnProdutos_click)

        self.imgBtnEmpregados = PhotoImage(file='public/imagens/btnEmpregados.png')
        self.btnEmpregados = Button(admMenu, image=self.imgBtnEmpregados, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnEmpregados.place(relx=0.338, rely=0.4, width=150, height=150)
        self.btnEmpregados.configure(borderwidth="0", cursor="hand2")

        self.imgBtnCategorias = PhotoImage(file='public/imagens/btnCategorias.png')
        self.btnCategorias = Button(admMenu, image=self.imgBtnCategorias, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnCategorias.place(relx=0.536, rely=0.4, width=150, height=150)
        self.btnCategorias.configure(borderwidth="0", cursor="hand2")

        self.btnEstatisicas = Button(admMenu, text="Estatisticas")
        self.btnEstatisicas.place(relx=0.732, rely=0.508, width=150, height=150)
        self.btnEstatisicas.configure(background="#ffffff", activebackground="#DEE2E6", borderwidth="0")
        self.btnEstatisicas.configure(cursor="hand2")
        self.btnEstatisicas.configure(font="-family {Calibri} -size 12")

        self.imgBtnVendas = PhotoImage(file='public/imagens/btnVendas.png')
        self.btnVendas = Button(admMenu, image=self.imgBtnVendas, bg='#3d8ea2', activebackground='#3d8ea2')
        self.btnVendas.place(relx=0.14, rely=0.63, width=150, height=150)
        self.btnVendas.configure(borderwidth="0", cursor="hand2")


def btnProdutos_click():
    admMenu.withdraw()
    produtos.callProdutos()


admMenu = Tk()
page = AdminMenu(admMenu)
admMenu.mainloop()
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from libs import database
from views.gui.gerir import produtos


class AddProduto:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Adicionar Produto")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="public/imagens/addProduto.png")
        self.label1.configure(image=self.img)

        self.labelTop = Label(p_add, text="Adicionar Produto")
        self.labelTop.place(x=485, y=75, width=400, height=70)
        self.labelTop.configure(font="-family {Poppins Bold} -size 31", background="#ffffff")

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000", background="#ffffff")

        self.txtIdProduto = Entry(p_add)
        self.txtIdProduto.place(relx=0.132, rely=0.296, width=450, height=30)
        self.txtIdProduto.configure(font="-family {Poppins} -size 12", relief="flat")
        self.txtIdProduto.config(state=DISABLED)

        self.txtNome = Entry(p_add)
        self.txtNome.place(relx=0.132, rely=0.413, width=450, height=30)
        self.txtNome.configure(font="-family {Poppins} -size 12", relief="flat")

        self.r2 = p_add.register(self.testint)

        self.txtDescricao = Entry(p_add)
        self.txtDescricao.place(relx=0.132, rely=0.529, width=450, height=120)
        self.txtDescricao.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtPreco = Entry(p_add)
        self.txtPreco.place(relx=0.527, rely=0.296, width=450, height=30)
        self.txtPreco.configure(font="-family {Poppins} -size 12", relief="flat")

        self.txtQuantStock = Entry(p_add)
        self.txtQuantStock.place(relx=0.527, rely=0.413, width=450, height=30)
        self.txtQuantStock.configure(font="-family {Poppins} -size 12", relief="flat")
        self.txtQuantStock.configure(validate="key", validatecommand=(self.r2, "%P"))

        val = []
        for i in database.lstCateg:
            val.append(i.nome)

        self.listCboCategoria=val
        self.cboCategoria=ttk.Combobox(p_add, values=self.listCboCategoria, state="readonly")
        self.cboCategoria.place(relx=0.527, rely=0.535, width=450, height=30)
        self.cboCategoria.configure(font="-family {Poppins} -size 12")

        self.txtCodBarras = Entry(p_add)
        self.txtCodBarras.place(relx=0.527, rely=0.646, width=450, height=30)
        self.txtCodBarras.configure(font="-family {Poppins} -size 12", relief="flat")
        self.txtCodBarras.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.btnAdicionar = Button(p_add, text="ADICIONAR", command=self.btnAdicionar_click)
        self.btnAdicionar.place(x=535, rely=0.836, width=120, height=34)
        self.btnAdicionar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnAdicionar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnAdicionar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

        self.btnLimpar = Button(p_add, text='LIMPAR', command=self.btnLimpar_click)
        self.btnLimpar.place(relx=0.526, rely=0.836, width=86, height=34)
        self.btnLimpar.configure(relief="flat", overrelief="flat", borderwidth="0")
        self.btnLimpar.configure(background="#CF1E14", activebackground="#CF1E14", foreground="#ffffff")
        self.btnLimpar.configure(cursor="hand2", font="-family {Poppins SemiBold} -size 14")

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def btnAdicionar_click(self):
        #idProduto = self.txtIdProduto.get()
        nomePro = self.txtNome.get()
        descricao = self.txtDescricao.get()
        preco = self.txtPreco.get()
        qtdStock = self.txtQuantStock.get()
        codBarras = self.txtCodBarras.get()
        listCtg = self.cboCategoria.get()

        categ = None
        for c in database.lstCateg:
            if listCtg == c.nome:
                categ = c.idCateg

        database.db.addProd(nomePro, descricao, preco, qtdStock, codBarras, categ)
        messagebox.showinfo("Sucesso!", "As informações foram adicionadas com sucesso.", parent=p_add)
        database.db.lerProduto()
        produtos.updList()
        p_add.destroy()

    def btnLimpar_click(self):
        self.txtIdProduto.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtDescricao.delete(0, END)
        self.txtPreco.delete(0, END)
        self.txtQuantStock.delete(0, END)
        #self.listCboCategoria.delete(0, END)
        #self.txtCodBarras.delete(0, END)


def callAddProdutos():
    global p_add
    global page3
    p_add = Toplevel()
    page3 = AddProduto(p_add)
    page3.time()
    p_add.mainloop()


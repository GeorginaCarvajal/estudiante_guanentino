
#  Georgina Estefania Carvajal Contreras :)

from tkinter import *
from tkinter import messagebox, ttk

def abrir_toplevel_calificaciones():
    global toplevel_calificaciones
    toplevel_calificaciones = Toplevel()
    toplevel_calificaciones.title("Calificaciones")
    toplevel_calificaciones.resizable(False, False)
    toplevel_calificaciones.geometry("500x400")
    toplevel_calificaciones.config(bg="black")
    
    frame_entrada1 = Frame(toplevel_calificaciones)
    frame_entrada1.config(bg="white", width=480, height=380)
    frame_entrada1.place(x=10, y=10)

    titulo = Label(toplevel_calificaciones, text="Informacion Academica")
    titulo.config(bg = "white",fg="black", font=("BlackJack", 12))
    titulo.place(x=175,y=15)

    lb_logo = Label(frame_entrada1, image=img, bg="white")
    lb_logo.place(x=25,y=75)

    toplevel_calificaciones.destroy

    lb_a = Label(frame_entrada1, text = "Asignatura : ")
    lb_a.config(bg="white", fg="purple4", font=("Abcissa", 13))
    lb_a.place(x=190, y=50)

    lista_desplegable = ttk.Combobox(frame_entrada1, width=20)
    lista_desplegable.place (x=300, y=50)
        
    opciones = ["Estadistica", "Trigonometria y Geometria Analitica", "Valores", "Filosofia", "Lengua Castellana", "Ingles", "Artistica", "Quimica", "Fisica", "Ed.Fisica", "Ed.Religiosa", "Sociales", "Politica"]
    lista_desplegable["values"]=opciones
    
    def nota_definitiva():
        cognitivo = float(entry_c.get())
        procedimental = float(entry_p.get())
        actitudinal = float(entry_a.get())
        autoevaluacion = float(entry_au.get())
        bimestral = float(entry_b.get())
        
        nota_definitiva = (0.3*cognitivo) + (0.3*procedimental) + (0.1*autoevaluacion) + (0.1*actitudinal) + (0.2*bimestral)
     
        lb_r = Label(frame_entrada1, text =("Nota definitiva: " + str(nota_definitiva) ))  
        lb_r.config(bg="white", fg="black", font=("Abcissa", 15))
        lb_r.place(x=200, y=300)

        if nota_definitiva < 30:
            messagebox.showinfo("Resultado", "El alumno reprobo la asignatura  :(")
        else:
             messagebox.showinfo("Resultado", "El alumno aprobo la asignatura :)")
      

    lb_c = Label(frame_entrada1, text = "Cognitivo : ")
    lb_c.config(bg="white", fg="blue", font=("Abcissa", 12))
    lb_c.place(x=220, y=140)

    entry_c = Entry(frame_entrada1, textvariable=c)
    entry_c.config(bg="white", fg="black", font=("Abcissa", 12), width=6)
    entry_c.focus_set()
    entry_c.place(x=360,y=140)

    lb_c = Label(frame_entrada1, text = "30%")
    lb_c.config(bg="white", fg="blue", font=("Abcissa", 12))
    lb_c.place(x=430, y=140)

    lb_p = Label(frame_entrada1, text = "Procedimental : ")
    lb_p.config(bg="white", fg="gold2", font=("Abcissa", 12))
    lb_p.place(x=220, y=170)

    entry_p = Entry(frame_entrada1, textvariable=p)
    entry_p.config(bg="white", fg="black", font=("Abcissa", 12), width=6)
    entry_p.focus_set()
    entry_p.place(x=360,y=170)

    lb_p = Label(frame_entrada1, text = "30% ")
    lb_p.config(bg="white", fg="gold2", font=("Abcissa", 12))
    lb_p.place(x=430, y=170)

    lb_a = Label(frame_entrada1, text = "Actitudinal : ")
    lb_a.config(bg="white", fg="magenta4", font=("Abcissa", 12))
    lb_a.place(x=220, y=200)

    entry_a = Entry(frame_entrada1, textvariable=a)
    entry_a.config(bg="white", fg="black", font=("Abcissa", 12), width=6)
    entry_a.focus_set()
    entry_a.place(x=360,y=200)

    lb_a = Label(frame_entrada1, text = "10%")
    lb_a.config(bg="white", fg="magenta4", font=("Abcissa", 12))
    lb_a.place(x=430, y=200)

    lb_au = Label(frame_entrada1, text = "Autoevaluacion : ")
    lb_au.config(bg="white", fg="green4", font=("Abcissa", 12))
    lb_au.place(x=220, y=230)

    entry_au = Entry(frame_entrada1, textvariable=au)
    entry_au.config(bg="white", fg="black", font=("Abcissa", 12), width=6)
    entry_au.focus_set()
    entry_au.place(x=360,y=230)

    lb_au = Label(frame_entrada1, text = "10%")
    lb_au.config(bg="white", fg="green4", font=("Abcissa", 12))
    lb_au.place(x=430, y=230)

    lb_b = Label(frame_entrada1, text = "Bimestral : ")
    lb_b.config(bg="white", fg="maroon", font=("Abcissa", 12))
    lb_b.place(x=220, y=260)

    entry_b = Entry(frame_entrada1, textvariable=b)
    entry_b.config(bg="white", fg="black", font=("Abcissa", 12), width=6)
    entry_b.focus_set()
    entry_b.place(x=360,y=260)

    lb_b = Label(frame_entrada1, text = "20%")
    lb_b.config(bg="white", fg="maroon", font=("Abcissa", 12))
    lb_b.place(x=430, y=260)

    bt_calcular = Button(frame_entrada1, text="Calcular", command=nota_definitiva)
    bt_calcular.place(x=250, y=90, width=70, height=40)

    bt_salir = Button(frame_entrada1, text="Salir",command=toplevel_calificaciones.destroy)
    bt_salir.place(x=350, y=90, width=70, height=40)
  

def abrir_toplevel_imc():
    global toplevel_imc
    toplevel_imc = Toplevel()
    toplevel_imc.title("IMC")
    toplevel_imc.resizable(False, False)
    toplevel_imc.geometry("500x300")
    toplevel_imc.config(bg="black")

    frame_entrada = Frame(toplevel_imc)
    frame_entrada.config(bg="white", width=480, height=280)
    frame_entrada.place(x=10, y=10)

    titulo = Label(frame_entrada, text="IMC")
    titulo.config(bg = "white",fg="black", font=("BlackJack", 12))
    titulo.place(x=320,y=15)

    lb_logo2 = Label(frame_entrada, image=img2, bg="white")
    lb_logo2.place(x=10,y=30)



    def imc():
        estatura = float(entry_e.get())
        peso = float(entry_p.get())
        imc = peso / estatura**2

        lb_r = Label(frame_entrada, text =("Imc: " + str(imc) ))
        lb_r.config(bg="white", fg="black", font=("Abcissa", 15))
        lb_r.place(x=225, y=200)
      
        if imc < 16:
            messagebox.showinfo("Resultado", "delgadez severa")
        elif imc < 17:
            messagebox.showinfo("Resultado", "delgadez moderada")
        elif imc < 18.5:
            messagebox.showinfo("Resultado", "delgadez ligera")
        elif imc < 25:
            messagebox.showinfo("Resultado", "Saludable")
        elif imc < 30:
            messagebox.showinfo("Resultado", "Sobrepeso")
        elif imc < 35:
            messagebox.showinfo("Resultado", "Obesidad grado I")
        elif imc < 40:
            messagebox.showinfo("Resultado", "Obesidad grado II (grave)")
        else:
             messagebox.showinfo("Resultado", "Obesidad grado III (mórbida)")

    lb_p = Label(frame_entrada, text = "Peso(kg) = ")
    lb_p.config(bg="white", fg="blue", font=("Abcissa", 15))
    lb_p.place(x=230, y=40)

    entry_p = Entry(frame_entrada, textvariable=p)
    entry_p.config(bg="white", fg="black", font=("Abcissa", 15), width=6)
    entry_p.focus_set()
    entry_p.place(x=375,y=40)

    lb_e = Label(frame_entrada, text = "Estatura(m) = ")
    lb_e.config(bg="white", fg="gold2", font=("Abcissa", 15))
    lb_e.place(x=230, y=80)

    entry_e = Entry(frame_entrada, textvariable=e)
    entry_e.config(bg="white", fg="black", font=("Abcissa", 15), width=6)
    entry_e.focus_set()
    entry_e.place(x=375,y=80)

    bt_calcular = Button(frame_entrada, text="Calcular", command=imc)
    bt_calcular.place(x=250, y=130, width=70, height=40)

    bt_salir = Button(frame_entrada, text="Salir", command=toplevel_imc.destroy)
    bt_salir.place(x=360, y=130, width=70, height=40)

ventana_principal = Tk()
ventana_principal.title("Georgina Carvajal :)")
ventana_principal.geometry("500x540")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

p = StringVar()
e = StringVar()
c = StringVar()
a = StringVar()
au = StringVar ()
b = StringVar()
global logo

# salir
def salir():
    messagebox.showinfo("Perfil Del Estudiante", "La app se va a cerrar")
    ventana_principal.destroy()

barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_separator()

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Salir", menu=menu_salir)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=220)
frame_entrada.place(x=10, y=10)

logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=40, y=60)

titulo = Label(ventana_principal, text="Datos basicos del estudiante")
titulo.config(bg = "white",fg="black", font=("BlackJack", 12))
titulo.place(x=145,y=15)

lb_c = Label(frame_entrada, text = "Nombre : ")
lb_c.config(bg="white", fg="green3", font=("Abcissa", 10))
lb_c.place(x=150, y=40)

entry_c = Entry(frame_entrada)
entry_c.config(bg="white", fg="black", font=("Abcissa", 10), width=25)
entry_c.focus_set()
entry_c.place(x=230,y=40)

lb_d = Label(frame_entrada, text = "Grado : ")
lb_d.config(bg="white", fg="blue2", font=("Abcissa", 10))
lb_d.place(x=150, y=70)

entry_d = Entry(frame_entrada)
entry_d.config(bg="white", fg="black", font=("Abcissa", 10), width=25)
entry_d.focus_set()
entry_d.place(x=230,y=70)

lb_k = Label(frame_entrada, text = "Edad : ")
lb_k.config(bg="white", fg="red3", font=("Abcissa", 10))
lb_k.place(x=150, y=100)

entry_k = Entry(frame_entrada)
entry_k.config(bg="white", fg="black", font=("Abcissa", 10), width=25)
entry_k.focus_set()
entry_k.place(x=230,y=100)

lb_r = Label(frame_entrada, text = "Dirección : ")
lb_r.config(bg="white", fg="purple3", font=("Abcissa", 10))
lb_r.place(x=150, y=130)

entry_r = Entry(frame_entrada)
entry_r.config(bg="white", fg="black", font=("Abcissa", 10), width=25)
entry_r.focus_set()
entry_r.place(x=230,y=130)

lb_h = Label(frame_entrada, text = "Teléfono : ")
lb_h.config(bg="white", fg="violet red", font=("Abcissa", 10))
lb_h.place(x=150, y=160)

entry_h = Entry(frame_entrada)
entry_h.config(bg="white", fg="black", font=("Abcissa", 10), width=25)
entry_h.focus_set()
entry_h.place(x=230,y=160)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=480, height=290)
frame_2.place(x=10, y=240)

img = PhotoImage(file="img/calificaciones.png")

botonCalificaciones = Button(frame_2, width=180, height=210, image=img,justify="center", command=abrir_toplevel_calificaciones)
botonCalificaciones.place(x=30, y=35)

img2 = PhotoImage(file="img/imc.png")

botonImc = Button(frame_2, width=190, height=180, image=img2,justify="center", command=abrir_toplevel_imc)
botonImc.place(x=250, y=50)

ventana_principal.mainloop()

from tkinter import *
from tkinter import messagebox

def abrir_toplevel_calificaciones():
    global toplevel_calificaciones
    toplevel_calificaciones = Toplevel()
    toplevel_calificaciones.title("Calificaciones")
    toplevel_calificaciones.resizable(False, False)
    toplevel_calificaciones.geometry("500x300")
    toplevel_calificaciones.config(bg="black")
    
    frame_entrada = Frame(toplevel_calificaciones)
    frame_entrada.config(bg="white", width=480, height=280)
    frame_entrada.place(x=10, y=10)

    titulo = Label(toplevel_calificaciones, text="Informacion Academica")
    titulo.config(bg = "white",fg="black", font=("BlackJack", 12))
    titulo.place(x=115,y=15)

    lb_logo = Label(frame_entrada, image=img, bg="white")
    lb_logo.place(x=10,y=35)

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

    titulo = Label(toplevel_imc, text="IMC")
    titulo.config(bg = "white",fg="black", font=("BlackJack", 12))
    titulo.place(x=320,y=15)

    lb_logo2 = Label(frame_entrada, image=img2, bg="white")
    lb_logo2.place(x=10,y=10)

    lb_p = Label(toplevel_imc, text = "Peso = ")
    lb_p.config(bg="white", fg="blue", font=("Abcissa", 15))
    lb_p.place(x=250, y=40)

    entry_p = Entry(toplevel_imc, textvariable=p)
    entry_p.config(bg="white", fg="black", font=("Abcissa", 15), width=6)
    entry_p.focus_set()
    entry_p.place(x=350,y=40)

    lb_e = Label(toplevel_imc, text = "Estatura = ")
    lb_e.config(bg="white", fg="gold2", font=("Abcissa", 15))
    lb_e.place(x=250, y=70)

    entry_e = Entry(toplevel_imc, textvariable=e)
    entry_e.config(bg="white", fg="black", font=("Abcissa", 15), width=6)
    entry_e.focus_set()
    entry_e.place(x=350,y=70)

ventana_principal = Tk()
ventana_principal.title("Perfil del Estudiante")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

p = StringVar()
e = StringVar()
global logo

barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

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
lb_c.config(bg="white", fg="green3", font=("Abcissa", 12))
lb_c.place(x=150, y=40)

entry_c = Entry(frame_entrada)
entry_c.config(bg="white", fg="black", font=("Abcissa", 12), width=25)
entry_c.focus_set()
entry_c.place(x=230,y=40)

lb_d = Label(frame_entrada, text = "Grado : ")
lb_d.config(bg="white", fg="blue2", font=("Abcissa", 12))
lb_d.place(x=150, y=70)

entry_d = Entry(frame_entrada)
entry_d.config(bg="white", fg="black", font=("Abcissa", 12), width=25)
entry_d.focus_set()
entry_d.place(x=230,y=70)

lb_k = Label(frame_entrada, text = "Edad : ")
lb_k.config(bg="white", fg="red3", font=("Abcissa", 12))
lb_k.place(x=150, y=100)

entry_k = Entry(frame_entrada)
entry_k.config(bg="white", fg="black", font=("Abcissa", 12), width=25)
entry_k.focus_set()
entry_k.place(x=230,y=100)

lb_r = Label(frame_entrada, text = "Dirección : ")
lb_r.config(bg="white", fg="purple3", font=("Abcissa", 12))
lb_r.place(x=150, y=130)

entry_r = Entry(frame_entrada)
entry_r.config(bg="white", fg="black", font=("Abcissa", 12), width=25)
entry_r.focus_set()
entry_r.place(x=230,y=130)

lb_h = Label(frame_entrada, text = "Teléfono : ")
lb_h.config(bg="white", fg="violet red", font=("Abcissa", 12))
lb_h.place(x=150, y=160)

entry_h = Entry(frame_entrada)
entry_h.config(bg="white", fg="black", font=("Abcissa", 12), width=25)
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

from tkinter import *
from tkinter import messagebox


ventana_principal = Tk()
ventana_principal.title("Perfil del Estudiante")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=200)
frame_entrada.place(x=10, y=10)

imagen = PhotoImage("/img/icono_persona.jpg")
imagen = Label(frame_entrada, imagen= imagen, bg="white")
imagen.place(x=75,y=350)

titulo = Label(ventana_principal, text="Datos basicos del estudiante")
titulo.config(bg = "white",fg="black", font=("Helvetica", 15))
titulo.place(x=125,y=15)


lb_c = Label(frame_entrada, text = "Nombre : ")
lb_c.config(bg="white", fg="green3", font=("Times New Roman", 10))
lb_c.place(x=125, y=40)

entry_c = Entry(frame_entrada)
entry_c.config(bg="white", fg="black", font=("Times New Roman", 10), width=20)
entry_c.focus_set()
entry_c.place(x=220,y=40)

lb_d = Label(frame_entrada, text = "Grado : ")
lb_d.config(bg="white", fg="blue2", font=("Times New Roman", 10))
lb_d.place(x=125, y=70)

entry_d = Entry(frame_entrada)
entry_d.config(bg="white", fg="black", font=("Times New Roman", 10), width=20)
entry_d.focus_set()
entry_d.place(x=220,y=70)

lb_k = Label(frame_entrada, text = "Edad : ")
lb_k.config(bg="white", fg="red3", font=("Times New Roman", 10))
lb_k.place(x=125, y=100)

entry_k = Entry(frame_entrada)
entry_k.config(bg="white", fg="black", font=("Times New Roman", 10), width=20)
entry_k.focus_set()
entry_k.place(x=220,y=100)

lb_r = Label(frame_entrada, text = "Dirección : ")
lb_r.config(bg="white", fg="purple3", font=("Times New Roman", 10))
lb_r.place(x=125, y=130)

entry_r = Entry(frame_entrada)
entry_r.config(bg="white", fg="black", font=("Times New Roman", 10), width=20)
entry_r.focus_set()
entry_r.place(x=220,y=130)

ventana_principal.mainloop()
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
def trace_courbe(f):
    try:
        #Conversion de la chaine de caracteres en une expression sympy
        x=sp.symbols('x')
        expr=sp.sympify(f)
        #Conversion de l'expression en une fonction lambda numpy
        f=sp.lambdify(x,expr,"numpy")
        #Generation des valeurs de x dans l'intervalle [-20, 20]
        x_vals=np.linspace(-20, 20, 400)
        y_vals=f(x_vals)
        #Trace de la courbe
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x)={f}', color='blue', linewidth=2)
        #Ajout des labels et legende
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Courbe de la fonction f(x)={expr}')
        plt.grid(True)
        plt.legend()
        #Affichage du graphique
        plt.show()
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur : {e}. Assurez-vous que la fonction est correctement définie.")
def on_button_click():
    f=entry_function.get()
    trace_courbe(f)
#Configuration de la fenetre tkinter
root=tk.Tk()
root.title("Trace de fonction")
#Cadre pour la saisie de la fonction
frame=tk.Frame(root, padx=10, pady=10)
frame.pack()
label=tk.Label(frame, text="Entrez la fonction f(x) à tracer (par exemple, 'x**2', 'sin(x)', 'exp(x)', etc) :")
label.pack()
entry_function=tk.Entry(frame, width=50)
entry_function.pack()
button_trace=tk.Button(frame, text="Tracer la courbe", command=on_button_click)
button_trace.pack()
#Demarrage de la boucle principale tkinter
root.mainloop()

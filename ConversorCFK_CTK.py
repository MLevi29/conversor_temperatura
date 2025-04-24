import customtkinter as ctk

# Passos
# 1. Configurar a aparência
# 2. Criação da janela principal
# 3. Criação dos campos
# 4. Criação das funções de funcionalidades
# 5. Iniciar a aplicação

class App(ctk.CTk):
    ctk.set_appearance_mode('dark') # system, light ou dar

    def __init__(self):
        super().__init__()
        self.geometry('250x300')
        self.minsize(width=250, height=300)
        self.title("Conversor CFK")

        # Temperatura de entrada
        self.temperatura = ctk.CTkLabel(self, text='Temperatura:')
        self.temperatura.pack(pady=10)

        self.texto1 = ctk.StringVar(value=0)
        self.temp1_valor = ctk.CTkEntry(self, textvariable=self.texto1, width=160)
        self.temp1_valor.bind("<KeyRelease>", self.converter1)
        self.temp1_valor.pack()
        
        self.temp1 = ctk.CTkOptionMenu(self, width=160,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"], command=self.converter2)
        self.temp1.pack()

        # Igual
        self.igual = ctk.CTkLabel(self, text='=')
        self.igual.pack()

        # Temperatura de saída
        self.texto2 = ctk.StringVar(value=0)
        self.temp2_valor = ctk.CTkEntry(self, textvariable=self.texto2, width=160)
        self.temp2_valor.bind("<KeyRelease>", self.converter2)
        self.temp2_valor.pack(pady=10)

        self.temp2 = ctk.CTkOptionMenu(self, width=160,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"], command=self.converter1)
        self.temp2.pack()

        # Botão para sair
        self.sair = ctk.CTkButton(self, text='Sair', command=self.quit)
        self.sair.pack(pady=5)
            

    def converter1(self, event):
        '''Recebe os valores da primeira temperatura e coloca o valor convertido na segunda temperatura.
        Também muda o valor da primeira temperatura caso mude a unidade de medida dela.'''
        if self.temp1_valor.get()=="":
            self.temp1_valor.configure(text_color='white')
            pass
        else:
            try:
                entrada = float(self.temp1_valor.get())

            except ValueError:
                self.temp1_valor.configure(text_color='red')
                pass

            else:
                self.temp1_valor.configure(text_color='white')
                self.temp2_valor.configure(text_color="white")

                lista = ["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"]
                t1 = lista.index(self.temp1.get())
                t2 = lista.index(self.temp2.get())

                if t1==t2:
                    self.texto2.set(round(entrada, 2))

                else:
                    if t1==0:
                        if t2 == 1:
                            self.texto2.set(round(round(entrada*1.8+32, 2), 2))
                        else:
                            self.texto2.set(round(entrada+273, 2))

                    elif t1 == 1:
                        if t2 == 0:
                            self.texto2.set(round((entrada-32)/1.8,2))
                        else:
                            self.texto2.set(round(((entrada-32)*5/9)+273, 2))
                    elif t1==2:
                        if t2==0:
                            self.texto2.set(round(entrada-273,2))
                        else:
                            self.texto2.set(round((entrada-273)*1.8+32, 2))


    def converter2(self, event):
        '''Recebe os valores da segunda temperatura e coloca o valor convertido na primeira temperatura.
        Também muda o valor da segunda temperatura caso mude a unidade de medida dela.'''
        if self.temp2_valor.get()=="":
            self.temp2_valor.configure(text_color="white")
            pass

        else:
            try:
                entrada = float(self.temp2_valor.get())

            except ValueError:
                self.temp2_valor.configure(text_color="red")
                pass
            
            else:
                self.temp2_valor.configure(text_color="white")
                self.temp1_valor.configure(text_color="white")

                lista = ["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"]
                t1 = lista.index(self.temp1.get())
                t2 = lista.index(self.temp2.get())

                if t2==t1:
                    self.texto1.set(round(entrada, 2))

                else:
                    if t2==0:
                        if t1 == 1:
                            self.texto1.set(round(round(entrada*1.8+32, 2), 2))
                        else:
                            self.texto1.set(round(entrada+273, 2))

                    elif t2 == 1:
                        if t1 == 0:
                            self.texto1.set(round((entrada-32)/1.8,2))
                        else:
                            self.texto1.set(round(((entrada-32)*5/9)+273, 2))
                    elif t2==2:
                        if t1==0:
                            self.texto1.set(round(entrada-273,2))
                        else:
                            self.texto1.set(round((entrada-273)*1.8+32, 2))


conversor = App()
conversor.mainloop()
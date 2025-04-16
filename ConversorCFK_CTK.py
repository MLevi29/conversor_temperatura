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
        self.temp1_valor = ctk.CTkEntry(self, textvariable=self.texto1)
        self.temp1_valor.bind("<KeyRelease>", self.converter)
        self.temp1_valor.pack()
        
        self.temp1 = ctk.CTkOptionMenu(self,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"], command=self.converter)
        self.temp1.pack()

        # Igual
        self.igual = ctk.CTkLabel(self, text='=')
        self.igual.pack()

        # Temperatura de saída
        self.texto2 = ctk.StringVar(value=0)
        self.temp2_valor = ctk.CTkEntry(self, textvariable=self.texto2)
        self.temp2_valor.pack(pady=10)

        self.temp2 = ctk.CTkOptionMenu(self,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"])
        self.temp2.pack()

        # Botão para sair
        self.sair = ctk.CTkButton(self, text='Sair', command=self.quit)
        self.sair.pack(pady=5)
            
    def converter(self, event):
        if self.temp1_valor.get()=="":
            self.texto1.set(0)

        else:
            entrada = float(self.temp1_valor.get())

            lista = ["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"]
            t1 = lista.index(self.temp1.get())
            t2 = lista.index(self.temp2.get())

            if t1==t2:
                self.texto2.set(entrada)

            else:
                if t1==0:
                    if t2 == 1:
                        self.texto2.set(entrada*1.8+32)
                    else:
                        self.texto2.set(entrada+273)

                elif t1 == 1:
                    if t2 == 0:
                        self.texto2.set((entrada-32)/1.8)
                    else:
                        self.texto2.set(((entrada-32)*5/9)+273)
                elif t1==2:
                    if t2==0:
                        self.texto2.set(entrada-273)
                    else:
                        self.texto2.set((entrada-273)*1.8+32)


conversor = App()
conversor.mainloop()
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

        self.valor1 = ctk.StringVar(value=0)
        self.temp1_valor = ctk.CTkEntry(self, textvariable=self.valor1)
        self.temp1_valor.pack()

        self.temp1 = ctk.CTkOptionMenu(self,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"])
        self.temp1.pack()

        self.igual = ctk.CTkLabel(self, text='=')
        self.igual.pack()

        # Temperatura de saída
        self.valor2 = ctk.StringVar(value=0)
        self.temp2_valor = ctk.CTkEntry(self, textvariable=self.valor1)
        self.temp2_valor.pack(pady=10)

        self.temp2 = ctk.CTkOptionMenu(self,
                        values=["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"])
        self.temp2.pack()

        # Botão para sair
        self.sair = ctk.CTkButton(self, text='Sair', command=self.quit)
        self.sair.pack(pady=5)
        

    def conversao(self):
        temps = ["Graus Celsius (°C)", "Graus Fahrenheit (°F)", "Kelvin (K)"]
        i_temp = (temps.index(self.temp1.get()), temps.index(self.temp2.get()))

        match i_temp:
            # get retorna uma string, fazer tratamento
            # quando não coloco valor na entrada, ele considera uma string '' que não pode ser transformada em float
            case (0,0):
                self.temp2_valor.configure(placeholder_text=self.temp1_valor.get())      

            case (0,1):
                valor = float(self.temp1_valor.get())*1.8+32
                self.temp2_valor.configure(placeholder_text=valor)

            case (0,2):
                valor = float(self.temp1_valor.get()) + 273
                self.temp2_valor.configure(placeholder_text=valor)

            case (1,0):
                valor = (float(self.temp1_valor.get())-32)/1.8
                self.temp2_valor.configure(placeholder_text=valor)

            case (1,1):
                self.temp2_valor.configure(placeholder_text=self.temp1_valor.get()) 

            case (1,2):
                valor = ((float(self.temp1_valor.get())-32)*5/9)+273
                self.temp2_valor.configure(placeholder_text=valor)

            case (2,0):
                valor = float(self.temp1_valor.get())-273
                self.temp2_valor.configure(placeholder_text=valor)

            case (2,1):
                valor = (float(self.temp1_valor.get())-273)*1.8+32
                self.temp2_valor.configure(placeholder_text=valor)

            case (2,2):
                self.temp2_valor.configure(placeholder_text=self.temp1_valor.get())
            


conversor = App()
conversor.mainloop()
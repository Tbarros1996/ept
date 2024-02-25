# EPT - Estado Plano de Tensões - EPT - Versão 1.0 

# Software de Cálculo de Tensões e Deformações em um Estado Plano Utilizando o Círculo de Mohr

# Instituto Federal de Pernambuco - IFPE - Campus Recife
# Curso Superior de Bacharelado em Engenharia Mecânica
# Disciplina de Mecânica dos Sólidos II - 2023.1

###################################################

# Linguagem de Programação: Python 3.11
# Data de Inicio do Desenvolvimento: 25/04/2023
# Data de Finalização do Desenvolvimento: 20/05/2023

# Projeto Desenvolvido Utilizando a Bibliografia Resistência dos Materiais do RC. Hibbler - 10º Edição


# Termo de Isenção de Reponsabilidades

"""

O uso deste código, ou qualquer outro material fornecido, é de total responsabilidade do usuário. 
O presente texto tem como objetivo esclarecer que o código disponibilizado é fornecido "no estado em que se encontra" 
e sem quaisquer garantias expressas ou implícitas.
Embora tenhamos nos esforçado para fornecer um código de qualidade e confiabilidade, 
não podemos garantir que o mesmo esteja livre de erros ou atenda a todas as suas necessidades específicas. 
O uso deste código é realizado por conta e risco do usuário.
Não recomendamos a utilização em ambientes industriais onde projetos devem ser realizados utilizando parâmetros estabelecidos por normas técnicas
nacionais ou internacionais.


Recife, 20 de Maio de 2023


"""

###########################################################


# Histórico de Revisões:


"""
    # Rev00: Criação do algoritmo principal como menu e separação de módulos de cálculo em subrotinaspara separação do código. Criação do primeiro módulo
        de cálculo utilizando o Dash - 12/05/2023 
        
    # Rev01: Unificação das subrotinas em um único algoritmo. Criação do Setup compilador para criação do arquivo executável usando a biblioteca CXFREEZE
    
    # Rev02: Melhoria dos Gráficos. Remoção dos eixos de tensão e deformação devido a problemas de resolução entre o Tkinter e Matplotilib para o problema Proposto
    
    # Rev03: Criação de Um Sistema de Verificação de Licença
    
"""



import tkinter as tk
from tkinter import messagebox
import os
import numpy as np 
import math as mt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


"""
Comentário :

Os módulos anteriores serão utilizados para as seguintes finalidades abaixo:

Tkinter -> Biblioteca interna do Python. Será responsável por criar os ambientes gráficos onde o usuário irá interage com o programa, realizando a entrada de dados e retornando a saida os dados
calculados e o gráfico do circulo de mohr. Devido a simplicidade de criação de códigos, foi utilizada devido ao tempo curto de desenvolvimento. Em versões futuras, pretende-se utilizar o PyQT que 
tem com base a DE GNU-KDE

OS - Biblioteca interna do Python. Será utilizada para criar interações entre o software e o sistema operacional, retirando ou inserindo algumas informações. Essa biblioteca será usada no módulo de
licenciamento do sotware

Numpy -> Biblioteca matemático para realização de cálculos e geração de funções e valores para criação dos gráficos. Numpy tem como finalidade aproximar a linguagem Python de funcionalidades
presentes na linguagem MATLAB®. Para versões futuras, serão utilizadas as funcionalidades do Numpy para realização dos problemas utilizando o tensor de tensões de Cauchy

Math -> Modulo matemático interno do Python. Possui funções internas para cálculos matemáticos. 

Matplotlib -> Biblioteca responsável por plotar gráficos. É a responsável por gerar os Círculos de Mohr. Está configurada para interagir dentro do objeto gráfico do Tkinter e não externamente.


"""


# Premissa Geral:

"""
Para o entendimento do código abaixo, é necessário entender a lógica empregada no desenvolvimento do mesmo.
Para a construção, foi impregado o paradigma funcional. Apesar de ser também prático construir
o código usando Orientação a Objetos, tal paradigma está implícito na construção do programa. 

O programa está separado em camadas onde a camada mais externa é o módulo de acesso e a camada mais interna é o módulo de cálculo. 


 Programa é Executado>
 
                    Módulo de Licenciamento é Carregado > 
                    
                        Verifica se o programa possui registro (Na primeira execução o serial é solicitado. Após o registro, um bitcode é criado nos arquivos do programa)
                        
                            > Se o programa está registrado > Módulo Principal é executado
                            > Caso Contrário > É solicitado o registro com uso da inserção do serial válido informado no discritivo técnico do programa para o cliente.
                        
Após o registro, a mensagem de solicitação de registro não aparece. O módulo principal é executado diretamente. Em caso de desinstalação, será necessário registrar novamente.


O módulo principal possui 4 submódulos impregados para funcionalidades diferentes.

    - Módulo de Tensões
    - Módulo de Deformações
    - Módulo de Métodos de Falha
    - Módulo de Informações.
    

"""


def programa_principal():
    
    def modulo_secundario_1_():
    
        m1 = tk.Toplevel(root)
        
        plot = tk.Toplevel(m1)
        
        plot.geometry("600x600")
        plot.resizable(False, False)
        plot.title('Gráfico Mohr')
        
        fig = Figure(figsize=(20,20), dpi=100)
        ax = fig.add_subplot(111)
        
        canvas = FigureCanvasTkAgg(fig, master=plot)
        canvas.get_tk_widget().pack()
        
        def x_linha(sigmax = float ,sigmay = float,tauxy = float,angulo = float ,sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                sigma_xlinha = ((sigmax + sigmay)/2) + ((sigmax - sigmay)/2)*mt.cos((np.deg2rad(angulo*2))) + tauxy*mt.sin((np.deg2rad(angulo*2)))
                
                return sigma_xlinha
            
            else: # Sentido Horário
                sigma_xlinha = ((sigmax + sigmay)/2) + ((sigmax - sigmay)/2)*mt.cos(-(np.deg2rad(angulo*2))) + tauxy*mt.sin(-(np.deg2rad(angulo*2)))
                
                return sigma_xlinha
            
        def y_linha(sigmax = float ,sigmay = float,tauxy = float,angulo = float ,sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                sigma_ylinha = ((sigmax + sigmay)/2) - ((sigmax - sigmay)/2)*mt.cos((np.deg2rad(angulo*2))) - tauxy*mt.sin((np.deg2rad(angulo*2)))
                
                return sigma_ylinha
            
            else: # Sentido Horário
                
                sigma_ylinha = ((sigmax + sigmay)/2) - ((sigmax - sigmay)/2)*mt.cos(-(np.deg2rad(angulo*2))) - tauxy*mt.sin(-(np.deg2rad(angulo*2)))
                return sigma_ylinha
            
    
        def tau_linha(sigmax = float ,sigmay = float, tauxy = float, angulo = float ,sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                
                novo_tauxy = (-1)*((sigmax-sigmay)/2)*mt.sin(2*mt.radians(angulo))+tauxy*mt.cos(2*mt.radians(angulo))
                
                return novo_tauxy
            
            else: # Sentido Horário
                
                novo_tauxy = (-1)*((sigmax-sigmay)/2)*mt.sin(-2*mt.radians(angulo))+tauxy*mt.cos(-2*mt.radians(angulo))
                
                return  novo_tauxy
    
        def tau_maximo(sigmax ,sigmay , tauxy):
            a = (sigmax - sigmay)/2
            taumaximo = mt.sqrt(a**2 + tauxy**2)
            return taumaximo
        
        def sigma_medio(sigmax = float, sigmay = float):
            sigma_medio = (sigmax+sigmay)/2
            return sigma_medio   
        
        entrada_sigma_x = tk.DoubleVar()
        entrada_sigma_y = tk.DoubleVar()
        entrada_tau_xy = tk.DoubleVar()
        entrada_teta = tk.DoubleVar()
        entrada_sentido = tk.BooleanVar() 
        
        def botao_calculo():
            
            sx = entrada_sigma_x.get()
            sy = entrada_sigma_y.get()
            tau_xy = entrada_tau_xy.get()
            angulo_teta = entrada_teta.get()
            sentido_de_giro = entrada_sentido.get()
            
            tensao_x_linha.config(text=float(round(x_linha(sx,sy,tau_xy,angulo_teta,sentido_de_giro),2)))
            tensao_y_linha.config(text=float(round(y_linha(sx,sy,tau_xy,angulo_teta,sentido_de_giro),2)))
            cisa_y_linha.config(text=float(round(tau_linha(sx,sy,tau_xy,angulo_teta,sentido_de_giro),2)))
            cisa_max_linha.config(text=float(round(tau_maximo(sx,sy,tau_xy),2)))
            sigma_1_linha.config(text=float(round(sigma_medio(sx,sy)+tau_maximo(sx,sy,tau_xy),2)))
            sigma_2_linha.config(text=float(round(sigma_medio(sx,sy)-tau_maximo(sx,sy,tau_xy),2)))
            sigma_med.config(text = float(round(sigma_medio(sx,sy))))

        def botao_mohr():
            
            ax.clear()
            sx = entrada_sigma_x.get()
            sy = entrada_sigma_y.get()
            tau_xy = entrada_tau_xy.get()
            x_cent_cir= float(round(sigma_medio(sx,sy)))
            raio = float(round(tau_maximo(sx,sy,tau_xy),2))
            y_cent_cir = 0
            """
            p = 1.5
            f = 1.5
            x1 = [-f*2*raio, f*2*raio]  
            y1 = [0, 0]   
            x2 = [0, 0]   
            y2 = [-p*raio, p*raio]
            ax.plot(x1, y1, 'r', label=r'Eixo $\sigma$')
            ax.plot(x2, y2, 'b', label=r'Eixo $\gamma$')
            """
            pontos_do_circulo = np.linspace(0, 2 * np.pi, 100)
            ax.scatter(x_cent_cir,y_cent_cir)
            circ_x = x_cent_cir + raio * np.cos(pontos_do_circulo)
            circ_y = y_cent_cir + raio * np.sin(pontos_do_circulo)
            ax.plot(circ_x, circ_y, 'g', label='Circunferência')
            ext_esq_x = x_cent_cir + raio * np.cos(np.pi)
            ext_esq_y = y_cent_cir + raio * np.sin(np.pi)
            ext_dir_x = x_cent_cir + raio * np.cos(0)
            ext_dir_y = y_cent_cir + raio * np.sin(0)
            ax.plot(ext_esq_x, ext_esq_y, 'bo', label='Extremidade Esquerda')
            ax.plot(ext_dir_x, ext_dir_y, 'yo', label='Extremidade Direita')
            ax.text(ext_dir_x, ext_dir_y, f'({ext_dir_x:.1f}, {ext_dir_y:.1f})', ha='left', va='bottom')
            ax.text(ext_esq_x, ext_esq_y, f'({ext_esq_x:.1f}, {ext_esq_y:.1f})', ha='right', va='bottom')
            ax.invert_yaxis()
            
            
            ax.plot(sx,tau_xy,'ro',label = r"$\theta = 0°$")
            ax.plot([sx,x_cent_cir],[tau_xy,y_cent_cir],'b-',label = f"{raio}")
            ax.text(sx, tau_xy, f'({sx:.1f}, {tau_xy:.1f})', ha='right', va='bottom')
            
            ax.axis("on")
            ax.set_title('Circulo de Mohr')
            ax.set_xlabel("Eixo Sigma")
            ax.set_ylabel("Eixo Tau ")
            ax.grid(True, linestyle='-', linewidth=1, color='black')
            canvas.draw()

        m1.configure(bg="white")

        m1.geometry('930x680')
        m1.resizable(width=False, height=False)

        titulo = tk.Label(m1,\
            text="Módulo de Cálculo de Tensões Utilizando do Círculo de Mohr", anchor=tk.S, bg="white", font=("Arial",14))
        titulo.pack(side=tk.TOP, pady = 25)

        a = 240
        b = 650
        
        imagem1 = tk.PhotoImage(file = "imagem1.png").subsample(2,2)

        imagem2 = tk.PhotoImage(file = "imagem2.png").subsample(2,2)

        imagem3 = tk.PhotoImage(file = "imagem3.png").subsample(2,2)

        imagem4 = tk.PhotoImage(file = "imagem4.png").subsample(2,2)
        
        imagem5 = tk.PhotoImage(file = "imagem5.png").subsample(2,2)

        imagem6 = tk.PhotoImage(file = "imagem6.png").subsample(2,2)

        imagem7 = tk.PhotoImage(file = "imagem7.png").subsample(2,2)

        imagem8 = tk.PhotoImage(file = "imagem8.png").subsample(3,3)
        
        imagem9 = tk.PhotoImage(file = "imagem9.png").subsample(2,2)
        
        imagem10 = tk.PhotoImage(file = "imagem10.png").subsample(2,2)
        
        imagem20 = tk.PhotoImage(file = "imagem20.png").subsample(3,3)
        
        
        tensao_texto_x = tk.Label(m1, image=imagem1, compound='left', font=("Arial", 12), bg="white")
        tensao_texto_x.place(x = a-120, y = 125)
        tensao_x = tk.Entry(m1, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_sigma_x)
        tensao_x.place(x = a, y = 125)
        
        tensao_texto_y = tk.Label(m1, image=imagem2, compound='left', font=("Arial", 12), bg="white")
        tensao_texto_y.place(x = a-120, y = 205)
        tensao_y = tk.Entry(m1, bd = 5, width=10,font=("Arial", 30) , textvariable=entrada_sigma_y)
        tensao_y.place(x = a, y = 205)

        cisa_texto_xy = tk.Label(m1, image=imagem3, compound='left', font=("Arial", 12), bg="white")
        cisa_texto_xy.place(x = a-120, y = 285)
        cisa_xy = tk.Entry(m1, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_tau_xy)
        cisa_xy.place(x = a, y = 285)
        
        teta_texto = tk.Label(m1, image=imagem4, compound='left', font=("Arial", 12), bg="white")
        teta_texto.place(x = a-120, y = 365)
        teta = tk.Entry(m1, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_teta)
        teta.place(x = a, y = 365)

        giro_texto = tk.Label(m1, text="Defina o Sentido de Giro:" , compound='left', font=("Arial", 15), bg="white")
        giro_texto.place(x = 80, y = 445)
        
        check1 = tk.Radiobutton(m1, text="Horário",  font=("Arial", 15), bg="white", value = False, variable= entrada_sentido)
        check1.place(x = 80, y = 490)
        
        check2 = tk.Radiobutton(m1, text="Anti - Horário", font=("Arial", 15), bg="white", value = True, variable= entrada_sentido)
        check2.place(x = 280, y = 490)
        
        plotar_grafico = tk.Button(m1, text="Plotar Circulo de Mohr", bg = "blue", width=25, height=2, font = ("Comic", 15), command=botao_mohr, fg = "red")
        plotar_grafico.pack(side=tk.LEFT, anchor="sw")
    
        botao_calculos = tk.Button(m1, text="Calcular Valores", bg = "white", width=25, height=2, font = ("Comic", 15), command=botao_calculo, fg = "green")
        botao_calculos.pack(side=tk.LEFT, anchor="sw")
    
        botao_mohr_saida = tk.Button(m1, text="Externar Gráfico", bg = "gray", width=25, height=2, font = ("Comic", 15) , fg = "blue")
        botao_mohr_saida.pack(side=tk.LEFT, anchor="sw")
        
        tensao_x_linha_texto = tk.Label(m1, image=imagem5, compound='left', font=("Arial", 12), bg="white")
        tensao_x_linha_texto.place(x = b-120, y = 110)
        tensao_x_linha = tk.Label(m1, bd = 10,width=10,font=("Arial", 30) )
        tensao_x_linha.place(x = b, y = 120)

        tensao_y_linha_texto = tk.Label(m1, image=imagem6, compound='left', font=("Arial", 12), bg="white")
        tensao_y_linha_texto.place(x = b-120, y = 180)
        tensao_y_linha = tk.Label(m1, bd = 10, width=10,font=("Arial", 30))
        tensao_y_linha.place(x = b, y = 190)
        
        cisa_y_linha_texto = tk.Label(m1, image=imagem7, compound='left', font=("Arial", 12), bg="white")
        cisa_y_linha_texto.place(x = b-120, y = 260)
        cisa_y_linha = tk.Label(m1, bd = 10, width=10,font=("Arial", 30) )
        cisa_y_linha.place(x = b, y = 260)

        cisa_max_linha_texto = tk.Label(m1, image=imagem8, compound='left', font=("Arial", 12), bg="white")
        cisa_max_linha_texto.place(x = b-120, y = 350)
        cisa_max_linha = tk.Label(m1, bd = 10, width=10,font=("Arial", 30))
        cisa_max_linha.place(x = b, y = 330)

        sigma_1_linha_texto = tk.Label(m1, image=imagem9, compound='left', font=("Arial", 12), bg="white")
        sigma_1_linha_texto.place(x = b-120, y = 420)
        sigma_1_linha = tk.Label(m1, bd = 10, width=10,font=("Arial", 30))
        sigma_1_linha.place(x = b, y = 400)
        
        sigma_2_linha_texto = tk.Label(m1, image=imagem10, compound='left', font=("Arial", 12), bg="white")
        sigma_2_linha_texto.place(x = b-120, y = 480)
        sigma_2_linha = tk.Label(m1, bd = 10, width=10,font=("Arial", 30) )
        sigma_2_linha.place(x = b, y = 470)

        sigma_med_texto = tk.Label(m1, image=imagem20, compound='left', font=("Arial", 12), bg="white")
        sigma_med_texto.place(x = b-120, y =550)
        sigma_med = tk.Label(m1, bd = 10, width=10,font=("Arial", 30))
        sigma_med.place(x = b, y = 540)
        
        m1.mainloop()
 
    def modulo_secundario_2_():
        
        # Atentar que para associar uma subjanela a janela pricipal, tem que usar o comando Toplevel
        
        m2 = tk.Toplevel(root)
        
        plot2 = tk.Toplevel(m2)
        
        plot2.geometry("600x600")
        plot2.resizable(False, False)
        plot2.title('Gráfico Mohr para Deformação')
        
        fig2 = Figure(figsize=(12,12), dpi=100)
        ax = fig2.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig2, master=plot2)
        canvas.get_tk_widget().pack()
        
        
        def ex_linha(ex = float , ey = float, gamaxy = float, angulo = float , sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                
                e_xlinha = ((ex + ey)/2) + ((ex - ey)/2)*mt.cos((np.deg2rad(angulo*2))) + (gamaxy/2)*mt.sin((np.deg2rad(angulo*2)))
            
                return e_xlinha
            
            else: # Sentido Horário
                
                e_xlinha = ((ex + ey)/2) + ((ex - ey)/2)*mt.cos(-(np.deg2rad(angulo*2))) + (gamaxy/2)*mt.sin(-(np.deg2rad(angulo*2)))
            
                return e_xlinha
            
        def ey_linha(ex = float , ey = float, gamaxy = float, angulo = float , sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                
                ey_ylinha = ((ex+ ey)/2) - ((ex - ey)/2)*mt.cos((np.deg2rad(angulo*2))) -  (gamaxy/2)*mt.sin((np.deg2rad(angulo*2)))
                
                return ey_ylinha
            
            else: # Sentido Horário
                
                ey_ylinha = ((ex+ ey)/2) - ((ex - ey)/2)*mt.cos(-(np.deg2rad(angulo*2))) -  (gamaxy/2)*mt.sin(-(np.deg2rad(angulo*2)))
                
                return ey_ylinha
            
    
        def gamaxy_linha(ex = float , ey = float, gamaxy = float, angulo = float , sentido = bool):
            
            if sentido == True: # Sentido Anti Horário
                
                seno_1 = mt.sin(2*np.deg2rad(angulo))
                coseno_1 = mt.cos(2*np.deg2rad(angulo))
                novo_gamaxy = (-1)*((ex-ey)/2)*seno_1 + (gamaxy/2)*coseno_1
                ngamaxy = novo_gamaxy*2
            
                return ngamaxy
            
            else: # Sentido Horário
                seno_1 = mt.sin(2*np.deg2rad(-angulo))
                coseno_1 = mt.cos(2*np.deg2rad(-angulo))
                novo_gamaxy = (-1)*((ex-ey)/2)*seno_1 + (gamaxy/2)*coseno_1
                ngamaxy = novo_gamaxy*2
        
                return ngamaxy
    
    
        def gama_maximo(ex , ey , gamaxy):
            primeirotermo = (ex- ey)/2
            gamamaximo = (mt.sqrt(primeirotermo**2 + (gamaxy/2)**2))
            return gamamaximo 

        
        def epslon_medio(ex = float, ey = float):
            e_medio = (ex+ey)/2
            return e_medio   
        
        entrada_e_x = tk.DoubleVar()
        entrada_e_y = tk.DoubleVar()
        entrada_gamma_xy = tk.DoubleVar()
        entrada_teta = tk.DoubleVar()
        entrada_sentido = tk.BooleanVar() 
        
        def botao_calculo():
            
            ex = entrada_e_x.get()
            ey = entrada_e_y.get()
            gamma_xy = entrada_gamma_xy.get()
            angulo_teta = entrada_teta.get()
            sentido_de_giro = entrada_sentido.get()
            
            def_x_linha.config(text=float(round(ex_linha(ex,ey,gamma_xy,angulo_teta,sentido_de_giro),2)))
            def_y_linha.config(text=float(round(ey_linha(ex,ey,gamma_xy,angulo_teta,sentido_de_giro),2)))
            defcisa_y_linha.config(text=float(round(gamaxy_linha(ex,ey,gamma_xy,angulo_teta,sentido_de_giro),2)))
            defcisa_max_linha.config(text=float(round(gama_maximo(ex,ey,gamma_xy),2)))
            e_1_linha.config(text=float(round(epslon_medio(ex,ey)+gama_maximo(ex,ey,gamma_xy),2)))
            e_2_linha.config(text=float(round(epslon_medio(ex,ey)-gama_maximo(ex,ey,gamma_xy),2)))
            e_med.config(text = float(round(epslon_medio(ex,ey))))

        def botao_mohr():
            
            ax.clear()
            ex = entrada_e_x.get()
            ey = entrada_e_y.get()
            gamma_xy = entrada_gamma_xy.get()
            x_cent_cir= float(round(epslon_medio(ex,ey)))
            
            raio = float(round(gama_maximo(ex,ey,gamma_xy),2))
            y_cent_cir = 0
            p = 1.5
            f = 1.5
            """
            x1 = [-f*2*raio, f*2*raio]  
            y1 = [0, 0]   
            x2 = [0, 0]   
            y2 = [-p*raio, p*raio]
            ax.plot(x1, y1, 'r', label=r'Eixo $\epislon$')
            ax.plot(x2, y2, 'b', label=r'Eixo $\gamma$')
            """
            pontos_do_circulo = np.linspace(0, 2 * np.pi, 100)
            ax.scatter(x_cent_cir,y_cent_cir)
            circ_x = x_cent_cir + raio * np.cos(pontos_do_circulo)
            circ_y = y_cent_cir + raio * np.sin(pontos_do_circulo)
            ax.plot(circ_x, circ_y, 'g', label='Circunferência')
            ext_esq_x = x_cent_cir + raio * np.cos(np.pi)
            ext_esq_y = y_cent_cir + raio * np.sin(np.pi)
            ext_dir_x = x_cent_cir + raio * np.cos(0)
            ext_dir_y = y_cent_cir + raio * np.sin(0)
            ax.plot(ext_esq_x, ext_esq_y, 'bo', label='Extremidade Esquerda')
            ax.plot(ext_dir_x, ext_dir_y, 'yo', label='Extremidade Direita')
            ax.text(ext_dir_x, ext_dir_y, f'({ext_dir_x:.1f}, {ext_dir_y:.1f})', ha='left', va='bottom')
            ax.text(ext_esq_x, ext_esq_y, f'({ext_esq_x:.1f}, {ext_esq_y:.1f})', ha='right', va='bottom')
            ax.invert_yaxis()
            
        
            ax.plot(ex,gamma_xy*0.5,'ro',label = r"$\theta = 0°$")
            ax.plot([ex,x_cent_cir],[gamma_xy*0.5,y_cent_cir],'b-',label = f"{raio}")
            ax.text(ex, gamma_xy, f'({ex:.1f}, {gamma_xy:.1f})', ha='right', va='bottom')
            ax.axis('on')
                        
            ax.axis("on")
            ax.set_title('Circulo de Mohr')
            ax.grid(True, linestyle='-', linewidth=1, color='black')
            ax.set_xlabel("Eixo Épslon")
            ax.set_ylabel("Eixo Gama")
            canvas.draw()

            ax.set_title('Circulo de Mohr')
            canvas.draw()

        m2.configure(bg="white")

        m2.geometry('930x680')
        m2.resizable(width=False, height=False)


        titulo = tk.Label(m2,\
            text="Módulo de Cálculo de Deformações Utilizando do Círculo de Mohr", anchor=tk.S, bg="white", font=("Arial",14))
        titulo.pack(side=tk.TOP, pady = 25)

        a = 240
        b = 650
        
        imagem11 = tk.PhotoImage(file = "imagem11.png").subsample(2,2)

        imagem12 = tk.PhotoImage(file = "imagem12.png").subsample(2,2)

        imagem13 = tk.PhotoImage(file = "imagem13.png").subsample(2,2)

        imagem14 = tk.PhotoImage(file = "imagem14.png").subsample(2,2)
        
        imagem15 = tk.PhotoImage(file = "imagem15.png").subsample(2,2)

        imagem16 = tk.PhotoImage(file = "imagem16.png").subsample(2,2)

        imagem17 = tk.PhotoImage(file = "imagem17.png").subsample(2,2)

        imagem18 = tk.PhotoImage(file = "imagem18.png").subsample(3,3)
        
        imagem19 = tk.PhotoImage(file = "imagem19.png").subsample(3,3)
        
        imagem21 = tk.PhotoImage(file = "imagem21.png").subsample(3,3)
        
        imagem4 = tk.PhotoImage(file = "imagem4.png").subsample(2,2)
        
        defor_x_texto = tk.Label(m2, image=imagem11, compound='left', font=("Arial", 12), bg="white")
        defor_x_texto.place(x = a-120, y = 125)
        epslon_x = tk.Entry(m2, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_e_x)
        epslon_x.place(x = a, y = 125)
        
        defor_y_texto = tk.Label(m2, image=imagem12, compound='left', font=("Arial", 12), bg="white")
        defor_y_texto.place(x = a-120, y = 205)
        epslon_y = tk.Entry(m2, bd = 5, width=10,font=("Arial", 30) , textvariable=entrada_e_y)
        epslon_y.place(x = a, y = 205)

        gamma_texto_xy = tk.Label(m2, image=imagem17, compound='left', font=("Arial", 12), bg="white")
        gamma_texto_xy.place(x = a-120, y = 285)
        def_gamma_xy = tk.Entry(m2, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_gamma_xy)
        def_gamma_xy.place(x = a, y = 285)
        
        teta_texto = tk.Label(m2, image=imagem4, compound='left', font=("Arial", 12), bg="white")
        teta_texto.place(x = a-120, y = 365)
        teta = tk.Entry(m2, bd = 5, width=10,font=("Arial", 30), textvariable=entrada_teta)
        teta.place(x = a, y = 365)

        giro_texto = tk.Label(m2, text="Defina o Sentido de Giro:" , compound='left', font=("Arial", 15), bg="white")
        giro_texto.place(x = 80, y = 445)
        
        check1 = tk.Radiobutton(m2, text="Horário",  font=("Arial", 15), bg="white", value = False, variable= entrada_sentido)
        check1.place(x = 80, y = 490)
        
        check2 = tk.Radiobutton(m2, text="Anti - Horário", font=("Arial", 15), bg="white", value = True, variable= entrada_sentido)
        check2.place(x = 280, y = 490)
        
        plotar_grafico = tk.Button(m2, text="Plotar Mohr de Deformação", bg = "green", width=25, height=2, font = ("Comic", 15), command=botao_mohr, fg = "red")
        plotar_grafico.pack(side=tk.LEFT, anchor="sw")
    
        botao_calculos = tk.Button(m2, text="Calcular Deformação", bg = "white", width=25, height=2, font = ("Comic", 15), command=botao_calculo, fg = "green")
        botao_calculos.pack(side=tk.LEFT, anchor="sw")
    
        botao_mohr_saida = tk.Button(m2, text="Externar Gráfico", bg = "gray", width=25, height=2, font = ("Comic", 15) , fg = "blue")
        botao_mohr_saida.pack(side=tk.LEFT, anchor="sw")
        
        def_x_linha_texto = tk.Label(m2, image=imagem13, compound='left', font=("Arial", 12), bg="white")
        def_x_linha_texto.place(x = b-120, y = 110)
        def_x_linha = tk.Label(m2, bd = 10,width=10,font=("Arial", 30) )
        def_x_linha.place(x = b, y = 120)

        def_y_linha_texto = tk.Label(m2, image=imagem14, compound='left', font=("Arial", 12), bg="white")
        def_y_linha_texto.place(x = b-120, y = 180)
        def_y_linha = tk.Label(m2, bd = 10, width=10,font=("Arial", 30))
        def_y_linha.place(x = b, y = 190)
        
        defcisa_y_linha_texto = tk.Label(m2, image=imagem18, compound='left', font=("Arial", 12), bg="white")
        defcisa_y_linha_texto.place(x = b-120, y = 260)
        defcisa_y_linha = tk.Label(m2, bd = 10, width=10,font=("Arial", 30) )
        defcisa_y_linha.place(x = b, y = 260)

        defcisa_max_linha_texto = tk.Label(m2, image=imagem19, compound='left', font=("Arial", 12), bg="white")
        defcisa_max_linha_texto.place(x = b-120, y = 350)
        defcisa_max_linha = tk.Label(m2, bd = 10, width=10,font=("Arial", 30))
        defcisa_max_linha.place(x = b, y = 330)

        e_1_linha_texto = tk.Label(m2, image=imagem15, compound='left', font=("Arial", 12), bg="white")
        e_1_linha_texto.place(x = b-120, y = 420)
        e_1_linha = tk.Label(m2, bd = 10, width=10,font=("Arial", 30))
        e_1_linha.place(x = b, y = 400)
        
        e_2_linha_texto = tk.Label(m2, image=imagem16, compound='left', font=("Arial", 12), bg="white")
        e_2_linha_texto.place(x = b-120, y = 480)
        e_2_linha = tk.Label(m2, bd = 10, width=10,font=("Arial", 30) )
        e_2_linha.place(x = b, y = 470)

        e_med_texto = tk.Label(m2, image=imagem21, compound='left', font=("Arial", 12), bg="white")
        e_med_texto.place(x = b-120, y =550)
        e_med = tk.Label(m2, bd = 10, width=10,font=("Arial", 30))
        e_med.place(x = b, y = 540)
        
        m2.mainloop()

    def modulo_secundario_3_():
        
        m3 = tk.Toplevel(root)
        m3.configure(bg="#00CED1")
        m3.maxsize(700,600)
        m3.resizable(False, False)
        altura = 400
        largura= 400
        largura_tela = m3.winfo_screenwidth()
        altura_tela = m3.winfo_screenheight()
        pos_x = int(largura_tela / 2 - largura / 2)
        pos_y = int(altura_tela / 2 - altura / 2)
        m3.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        m3.title("Informações EPT 1.0")
        texto = tk.Text(m3, wrap=tk.WORD)
        texto.pack(fill=tk.BOTH, expand=True)
        
        info = """
        
        Estado Plano de Tensões -  EPT \n \n Versão do Software 1.0 \n \n
        
        Desenvolvido por alunos do curso de Engenharia Mecânica do IFPE Para a Disciplina de Mecânica dos Sólidos II 2023.1 \n
        
        Aviso de Software para Fins Educacionais

        Este software foi desenvolvido exclusivamente para fins educativos e de aprendizado. Ele é destinado a ser usado como uma ferramenta de ensino, proporcionando uma experiência prática e interativa para a compreensão de conceitos e práticas relacionadas a resistência dos materiais.

        Ao utilizar este software para fins educativos, é importante estar ciente das seguintes informações:

        1. Propósito Educacional: O software foi criado com o objetivo de fornecer uma plataforma de aprendizado e simulação. Ele não deve ser utilizado em ambientes de trabalho ou em situações em que a precisão, confiabilidade ou segurança sejam critérios essenciais.

        2. Ausência de Garantias: O software é fornecido "no estado em que se encontra", sem garantias de qualquer tipo, expressas ou implícitas. Não nos responsabilizamos por quaisquer danos ou prejuízos decorrentes do uso deste software para fins educativos.

        3. Limitações Funcionais: O software educacional pode ter limitações em termos de funcionalidades, recursos ou desempenho, uma vez que seu principal objetivo é fornecer uma experiência de aprendizado e não atender a todas as necessidades de um ambiente de trabalho real.

        4. Não Responsabilidade: Não nos responsabilizamos por quaisquer consequências resultantes do uso deste software para fins educativos, incluindo, mas não se limitando a, perda de dados, danos ao sistema ou qualquer outro tipo de dano direto, indireto ou incidental.

        5. Recomendação de Uso Responsável: Ao utilizar este software para fins educativos, recomendamos que você o utilize de forma responsável, respeitando as leis, regulamentações e direitos autorais aplicáveis. Além disso, sempre verifique a precisão e valide as informações obtidas por meio do software antes de utilizá-las em qualquer contexto.

        Ao prosseguir com o uso deste software para fins educativos, você concorda em assumir toda a responsabilidade e risco associados ao seu uso. Se você não concorda com os termos deste aviso, recomendamos que interrompa imediatamente o uso deste software para fins educativos.

        """
        texto.insert(tk.END, info)
        texto.configure(state=tk.DISABLED)
        m3.mainloop()
    
    def modulo_secundario_4_():
        
        m4 = tk.Toplevel(root)
        m4.configure(bg="#00CED1")
        m4.maxsize(700,600)
        m4.resizable(False, False)
        altura = 400
        largura= 400
        largura_tela = m4.winfo_screenwidth()
        altura_tela = m4.winfo_screenheight()
        pos_x = int(largura_tela / 2 - largura / 2)
        pos_y = int(altura_tela / 2 - altura / 2)
        m4.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        m4.title("Módulo de Cargas Combinadas")
        texto2 = tk.Text(m4, wrap=tk.WORD)
        texto2.pack(fill=tk.BOTH, expand=True)
        info = """Módulo em Desenvolvimento - Copyright (C) 2023 IFPE - Engenharia Mecânica"""
        texto2.insert(tk.END, info)
        texto2.configure(state=tk.DISABLED)
        m4.mainloop()

    root = tk.Tk()
    root.title("EPT - Versão 1.0")

    titulo = tk.Label(root,\
        text="Estado Plano de Tensões - Versão 1.0 \n IFPE - Engenharia Mecânica", \
            anchor=tk.S, bg="#00CED1", font=("Arial",15))
    titulo.pack(side=tk.TOP, pady = 25,)

    rodape = tk.Label(root,\
        text="Copyright (C) 2023 IFPE - Engenharia Mecânica", anchor=tk.S, bg="#00CED1")
    rodape.pack(side=tk.BOTTOM)

    icone = tk.PhotoImage(file="imagem1.png")
    root.iconphoto(True, icone)

    root.configure(bg="#00CED1")
    root.maxsize(700,600)
    root.resizable(False, False)
    altura = 800
    largura= 600
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = int(largura_tela / 2 - largura / 2)
    pos_y = int(altura_tela / 2 - altura / 2)
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def botao1():
        modulo_secundario_1_()
        pass

    def botao2():
        modulo_secundario_2_()
        pass

    def botao3():
        modulo_secundario_3_()
        pass

    def botao4():
        modulo_secundario_4_()
    
        pass

    a = 5
    b = 17
    c = 6

    grupo_esquerdo = tk.Frame(root, bg="#00CED1")
    grupo_esquerdo.pack(side="left",padx=10)

    grupo_direito = tk.Frame(root,bg="#00CED1")
    grupo_direito.pack(side="right",padx=10)

    botao_1 = tk.Button(grupo_direito, command=botao1,text="Tensões", bd=c, height=a, width=b, font=("Arial",20), background="#ADD8E6")
    botao_1.pack(pady = 10)

    botao_2 = tk.Button(grupo_direito, command=botao2,text="Deformações", bd=c, height=a, width=b, font=("Arial",20), background="#ADD8E6")
    botao_2.pack(pady = 10)

    botao_3 = tk.Button(grupo_esquerdo, command=botao3,text="Suporte", bd=c, height=a, width=b, font=("Arial",20), background="#ADD8E6")
    botao_3.pack(pady = 10)

    botao_4 = tk.Button(grupo_esquerdo, command=botao4,text="Cargas \n Combinadas", bd=c, height=a, width=b, font=("Arial",20), background="#ADD8E6")
    botao_4.pack(pady = 10)

    root.mainloop()
    

def check_serial(serial):
    
    valid_serial = "ABC-123"

    if serial == valid_serial:
        return True
    else:
        return False

def save_serial(serial):
 
    with open("serial.bin", "wb") as file:
        file.write(serial.encode())

def load_serial():
    
    if os.path.isfile("serial.bin"):
        with open("serial.bin", "rb") as file:
            return file.read().decode()
    return ""

def verify_serial():
    serial = entry1.get() + "-" + entry2.get()

    if check_serial(serial):
        save_serial(serial)
        messagebox.showinfo("Licença Ativada", "Licença Ativada.")
        messagebox.showinfo("EPT 1.0.","Obrigado por Adquirir Nosso Software.")

        window_serial.destroy()
        programa_principal()
        
    else:
        messagebox.showerror("Serial Inválido", "Serial inválido.")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window_serial = tk.Tk()
window_serial.title("EPT - Versão 1.0 - Verificação de Licença")

icone = tk.PhotoImage(file="imagem1.png")
window_serial.iconphoto(True, icone)

window_serial.geometry("400x200")
window_serial.resizable(False, False)  

rodape = tk.Label(window_serial,\
    text="Copyright (C) 2023 IFPE - Engenharia Mecânica", anchor=tk.S)
rodape.pack(side=tk.BOTTOM)

label_title = tk.Label(window_serial, text="Insira o Serial", font=("Arial", 20))
label_title.pack(pady=20)

frame = tk.Frame(window_serial)
frame.pack()

entry1 = tk.Entry(frame, width=10, font=("Arial", 16))
entry1.pack(side=tk.LEFT)

label_hyphen = tk.Label(frame, text="-", font=("Arial", 16))
label_hyphen.pack(side=tk.LEFT)

entry2 = tk.Entry(frame, width=10, font=("Arial", 16))
entry2.pack(side=tk.LEFT)

button = tk.Button(window_serial, text="Ativar Licença", command=verify_serial, font=("Arial", 16))
button.pack(pady=20)

saved_serial = load_serial()

if saved_serial:
    window_serial.destroy()
    programa_principal()

center_window(window_serial)
window_serial.mainloop()






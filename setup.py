# Software de Cálculo de Tensões e Deformações em um Estado Plano Utilizando o Círculo de Mohr

# Instituto Federal de Pernambuco - IFPE - Campus Recife
# Departamento de Processos e Controles Industriais
# Curso Superior de Bacharelado em Engenharia Mecânica
# Disciplina de Mecânica dos Sólidos II - 2023.1

###################################################

# Projeto desenvolvido por :
 

# Linguagem de Programação: Python 3.11
# Data de Inicio do Desenvolvimento: 25/04/2023
# Data de Finalização do Desenvolvimento: 20/05/2023


# Projeto Desenvolvido Utilizando a Bibliografia Resistência dos Materiais do RC. Hibbler - 10º Edição

# Todos os direitos pertencem aos seus respectivos autores

###########################################################


# Histórico de Revisões:


"""
 
    # Rev00: Criação do algoritmo principal como menu e separação de módulos de cálculo em subrotinaspara separação do código. Criação do primeiro módulo
        de cálculo utilizando o Dash - 12/05/2023 
        
    # Rev01: Unificação das subrotinas em um único algoritmo. Criação do Setup compilador para criação do arquivo executável usando a biblioteca CXFREEZE
    
    
    
"""

import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
includefiles = ['imagem1.png','imagem2.png','imagem3.png','imagem4.png','imagem5.png','imagem6.png','imagem7.png','imagem8.png',\
                
                'imagem9.png','imagem10.png','imagem11.png','imagem12.png','imagem13.png','imagem14.png','imagem15.png','imagem16.png',\
                    
                'imagem17.png','imagem18.png','imagem19.png','imagem20.png','imagem21.png']

# Dependências e bibliotecas

build_options = {
    "packages": ["tkinter","numpy","math","matplotlib","os"],
    "optimize": 1 ,
    'include_files': includefiles
}
    

setup(
    name="EPT",
    version="1.0",
    description="Software de Cálculos Utilizando o Círculo de Mohr",
    options={"build_exe": build_options},
    executables= [Executable("main.py", base=base, copyright="Copyright (C) 2023 IFPE - Engenharia Mecânica", icon="ico.ico")]
    
)

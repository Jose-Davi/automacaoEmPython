#Bibliotecas = Pacotes de Codigos

#Passo 1: Entrar no site da empresa
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write(link)
pyautogui.press("enter")

#fazer uma pausar maior para esperar o site carregar

time.sleep(5)


#Passo 2: Fazer Login no sistema
pyautogui.click(x=721, y=463)
pyautogui.write("daviti@gmail.com")
pyautogui.press("tab")
pyautogui.write("daviti123")
#pyautogui.click(x=944, y=669)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)
#Passo 3: Abrir a base de dados
#pip install pandas openpyxl
#ler e armazenar as informações na variavel tabela
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
#Passo 4: cadastrar  1 produto  
#Passo 5: Repetir o passo 4 ate acabar a lista de produtos


    pyautogui.click(x=629, y=313)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if str(tabela.loc[linha,"obs"]) != "nan":
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    #voltar para o inicio da tela
    pyautogui.scroll(5000)





    




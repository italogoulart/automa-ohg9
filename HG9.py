import pyautogui
import time

#Definir o tempo de espera entre os comandos
pyautogui.PAUSE = 1

#abrir chrome 
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press("enter")

#esperar carregar 
time.sleep (3)

#abrir pagina do roteador
pyautogui.write("192.168.1.1")
pyautogui.press ("enter")

#esperar carregar
time.sleep (5)

#acessar roteador
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.press("enter")

#esperar carregar 
time.sleep (8)

#importar dados (Nome ; Senha ; PPOE)
import pandas as pd 
teste = pd.read_excel("C:\\Users\\Acer\\Desktop\\Configuração auto rot\\HG9\\dados.xlsx")

#Configurar 5G
#Nome 5G
pyautogui.click(x=376 , y=207)
pyautogui.tripleClick(x=725,y=435)
pyautogui.write(teste.loc[0,"dgname"]) #Digite aqui o nome do wifi 5G
pyautogui.click(x=749,y=467)
pyautogui.click(x=713,y=503)
pyautogui.click(x=699,y=504)
pyautogui.click(x=686,y=568)
pyautogui.click(x=526,y=610)

time.sleep(20)

#Senha 5G
pyautogui.click(x=284,y=398)
pyautogui.tripleClick(x=744,y=518)
pyautogui.write(str(teste.loc[0,"password"])) #Digite aqui a senha do wifi
pyautogui.click(x=526,y=562)

time.sleep(20)

#Configurar 2G

#Nome 2G
pyautogui.click(x=291,y=565)
pyautogui.tripleClick(x=725,y=435)
pyautogui.write(teste.loc[1,"dgname"]) #Digite aqui o nome do wifi 2G
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=700,y=486)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=668,y=451)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(20)

#Senha 
pyautogui.click(x=266,y=436)
pyautogui.tripleClick(x=744,y=518)
pyautogui.write(str(teste.loc[1,"password"])) #Digite aqui a senha do wifi
pyautogui.click(x=526,y=562)

time.sleep(20)

#DNS
pyautogui.click(x=550,y=212)
pyautogui.click(x=855,y=608)
pyautogui.press("tab")
pyautogui.write("138.59.232.4")
pyautogui.press("tab")
pyautogui.write("8.8.4.4")
pyautogui.press("tab")
pyautogui.write("8.8.8.8")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

pyautogui.scroll(1000)

#PPOE
pyautogui.click(x=451,y=214)
pyautogui.tripleClick(x=718,y=382)
pyautogui.write("0")
pyautogui.click(x=685,y=344)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=712,y=499)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.click(x=683,y=580)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write(teste.loc[2,"dgname"]) #Digite aqui o PPOE
pyautogui.press("tab")
pyautogui.write(str(teste.loc[2,"password"])) #Digite aqui a senha do PPOE
pyautogui.press("enter")
pyautogui.scroll(1000)
pyautogui.click(x=718,y=382)













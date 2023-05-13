from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

chrome_driver_path = r"C:\Users\gabri\AppData\Local\Selenium\chromedriver"

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)


def pesquisa_google(pesquisa):
    driver.minimize_window()
    driver.get("https://www.google.com")
    caixa_busca = driver.find_element(By.XPATH, r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
    caixa_busca.send_keys(pesquisa)
    caixa_busca.submit()


pesquisa_google("Dolar Real")
XPATH_MOEDA = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]"
moeda_conver = driver.find_element(By.XPATH, XPATH_MOEDA).text


pesquisa_google("Clima Navegantes")
XPATH_CLIMA = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/span/div[3]/span"
XPATH_CLIMA2 = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div"
Clima = driver.find_element(By.XPATH, XPATH_CLIMA).text
Clima2 = driver.find_element(By.XPATH, XPATH_CLIMA2).text
Clima2 = Clima2[:-2]

driver.quit()

now = datetime.datetime.now()
hora = now.strftime("%H")
hora_d = now.strftime("%H:%M")

def determinar_saudacao(hora):
    if hora >= "06" and hora <= "12":
        return "Bom dia!"
    elif hora > "12" and hora < "18":
        return "Boa Tarde!"
    else:
        return "Boa Noite!"


# Abrir o arquivo para escrita
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    # Escrever as variáveis no arquivo
    arquivo.write(f"moeda; {moeda_conver}\n")
    arquivo.write(f"Clima2; {Clima2}\n")
    arquivo.write(f"Clima; {Clima}\n")
    arquivo.write(f"hora; {hora_d}\n")

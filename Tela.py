from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from art import text2art as art_
from os import system
import datetime
import time

# Função pra patronizar a pesquisa
while True:

# Caminho para o driver do Chrome
    chrome_driver_path = r"C:\Users\gabri\AppData\Local\Selenium\chromedriver"

# Criar um objeto Service para o driver do Chrome
    service = Service(executable_path=chrome_driver_path)

# Criar uma instância do navegador Chrome com o objeto Service
    driver = webdriver.Chrome(service=service)
    driver.minimize_window()

    def search_box(pesquisa):

        animation = ["|", "/", "-", "\\"]

        for i in range(30):

# Seleciona o próximo caractere da animação
            character = animation[i % len(animation)]

# Define o texto da animação

            text = f"Carregando... {character}"
            print(text, end='\r')
            time.sleep(0.1)

# Minimiza a tela e abra uma aba no "Google" e faz a pesquisa
        driver.minimize_window()
        driver.get("https://www.google.com")
        time.sleep(1)
        search_box = driver.find_element(By.XPATH, r"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
        search_box.send_keys(pesquisa)
        search_box.submit()

# Limpa a Tela
    system("cls")

# Texto da cotação
    search_box("Dolar Real")
    XPATH_MOEDA = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]"
    moeda_conver = driver.find_element(By.XPATH, XPATH_MOEDA).text

# Texto Clima
    search_box("Clima Navegantes")
    XPATH_CLIMA = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/span/div[3]/span"
    XPATH_CLIMA2 = r"/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div"
    Clima = driver.find_element(By.XPATH, XPATH_CLIMA).text
    Clima2 = driver.find_element(By.XPATH, XPATH_CLIMA2).text
    Clima2 = Clima2[:-2]

# Fecha o navegador
    driver.quit()

# Visual dos Dados
    now = datetime.datetime.now()
    hora = now.strftime("%H")

    def determinar_saudacao(hora):
        if hora >= "06" and hora <= "12":
            return "Bom dia!"
        elif hora > "12" and hora < "18":
            return "Boa Tarde!"
        else:
            return "Boa Noite!"

    def imprimir_informacoes_gerais():
        horario_atual = now.strftime("%Y-%m-%d %H:%M:%S")
        print("\033[4mSobre Hoje\033[0m\n")
        print("\033[33m◼\033[0m \033[4mHorário atual\033[0m:", horario_atual)
        print("\033[33m◼\033[0m \033[4mClima de Hoje\033[0m: {} - {}".format(Clima, Clima2))
        print("\033[33m◼\033[0m \033[4mCotação\033[0m: {} igual a 1,00 Dolar".format(moeda_conver))

    saudacao = determinar_saudacao(hora)
    system("cls")
    print("\033[34m")
    print("{}".format(art_("{}".format(saudacao))))
    print("\033[0m")
    imprimir_informacoes_gerais()

    input_saida = input("\n\033[36m◼\033[0m \033[1mDeseja atualizar\033[0m? \033[32mS\033[0m/\033[31mN\033[31m: ").upper()

# Exit
    if input_saida == "N":
        print("                          ", end="")
        for letra in "Byeeee (>‿◠)✌ ":
            print(letra, end="", flush=True)
            time.sleep(0.1)
        exit()
    elif "S":
        True
    else:
        print("             Apenas \033[32mS\033[0m ou \033[31mN\033[0m !")
        input_saida = input("\n\033[36m◼\033[0m \033[1mDeseja atualizar\033[0m? \033[32mS\033[0m/\033[31mN\033[0m: ").upper()
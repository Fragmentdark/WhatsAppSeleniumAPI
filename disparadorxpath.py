import os
import pandas as pd
import time
import random
import subprocess
import undetected_chromedriver as uc  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

# --- Função para mover o mouse 
def mover_mouse(driver):
    try:
        actions = ActionChains(driver)
        # Padrão de movimento mais natural (pequenos deslocamentos)
        actions.move_by_offset(random.randint(-5, 5), random.randint(-5, 5)).perform()
        actions.move_by_offset(random.randint(-3, 3), random.randint(-3, 3)).perform()
        time.sleep(random.uniform(0.1, 0.3))
    except Exception as e:
        pass  # Ignora erros para não quebrar o fluxo

# Caminhos de arquivos (adicione o caminho do chrome driver, da planilha e do relatório aqui)
caminho_chromedriver = "CAMINHOchromedriver"
caminho_planilha = "CAMINHO/para/sua/planilha.xlsx"
caminho_relatorio = "relatorio_envio.txt"


# Lista de mensagens variantes (adicione seus scripts aqui, importante não conter links para o whatsapp nao indentificar como spam)
mensagens = mensagens = [
    "Olá! Tudo bem?",
    "Bom dia! Passando para compartilhar novidades com você.",
    "Olá! Esta é uma mensagem automática enviada via Python e Selenium.",
]

# Configurações de disfarce e privacidade
USER_AGENTS = [
    # Chrome no Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # Firefox no Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    
    # Microsoft Edge no Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/119.0.0.0 Safari/537.36",
    
    # Opera no Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/90.0.0.0 Safari/537.36",
    
    # Chrome no Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # Firefox no Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.1; rv:109.0) Gecko/20100101 Firefox/109.0",
    
]

# Função para atualizar o relatório
def atualizar_relatorio(mensagem):
    with open(caminho_relatorio, "a", encoding="utf-8") as relatorio:
        relatorio.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {mensagem}\n")
    print(mensagem)


# Função para iniciar o navegador
def iniciar_navegador():
    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-dns-prefetch")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222") 
  
   
    try:
        driver = uc.Chrome(
            options=options,
            use_subprocess=True,
            headless=False
        )
        return driver
    except Exception as e:
        print(f"Erro ao iniciar navegador: {e}")
        exit()

# Inicializa o navegador
driver = iniciar_navegador()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Pressione ENTER após escanear o QR Code...")
mover_mouse(driver)  # Movimento inicial para simular humano

# Carrega a planilha de contatos (A planilha precisa conter duas colunas, Nome e Tel_1)
df = pd.read_excel(caminho_planilha)

if 'Tel_1' not in df.columns:
    atualizar_relatorio("❌ ERRO: A planilha deve conter a coluna 'Tel_1' com os números de telefone.")
    driver.quit()
    exit()


# Função para enviar o contato (pelo xpath do navegador)
def enviar_contato(driver, nome_do_contato):
    try:
        # 1. Clicar no botão de "Anexar" (ícone de clipe na parte inferior direita da conversa) ou inspencionar em cima do anexar, depois com o botão direito do mouse no elemento e copie o xpath (Cut))
        # 🔧 Substitua o XPATH abaixo conforme o elemento correspondente no WhatsApp Web atual
        botao_anexo = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 'XPATH_DO_BOTAO_ANEXAR'))
        )
        botao_anexo.click()
        time.sleep(random.uniform(3, 5))

        # 2. Selecionar a opção "Contato" no menu de anexos (Clique F12 passe o mouse em cima da opção contatos, indentifique o elemento, cut e copie o xpath)
        # 🔧 Este item geralmente aparece como "Contato" em texto. Use contains(text(), "Contato") ou semelhante
        opcao_contato = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 'XPATH_DA_OPCAO_CONTATO'))
        )
        opcao_contato.click()
        time.sleep(random.uniform(3, 5))

        # 3. Localizar o campo de busca de contatos (o campo de busca para o nome do contato)
        # 🔧 Geralmente é um campo com 'data-testid="search-input"' ou algo semelhante
        campo_pesquisa = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, 'XPATH_DO_CAMPO_PESQUISA_CONTATO'))
        )
        campo_pesquisa.click()

        # 4. Digitar o nome do contato no campo de busca (selecione o nome do contato que você vai automar e enviar manualmente)
        campo_pesquisa.send_keys(nome_do_contato)
        time.sleep(random.uniform(2, 3))

        # 5. Selecionar o contato listado no resultado da busca
        # 🔧 Normalmente é o primeiro elemento da lista com role="option"
        resultado = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 'XPATH_DO_RESULTADO_CONTATO'))
        )
        resultado.click()
        time.sleep(random.uniform(2, 3))

        # 6. Clicar no primeiro botão de "Enviar" (inspencionar no peimeiro botão de envio)
        # 🔧 Ícone de envio (paper plane) dentro do modal de compartilhamento
        botao_enviar_1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 'XPATH_DO_PRIMEIRO_BOTAO_ENVIAR'))
        )
        botao_enviar_1.click()
        time.sleep(random.uniform(2, 3))

        # 7. Confirmar o envio clicando no segundo botão de "Enviar" (inspencionar no segundo botão de envio)
        # 🔧 Segundo botão geralmente aparece para confirmação de envio do contato
        botao_enviar_2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 'XPATH_DO_SEGUNDO_BOTAO_ENVIAR'))
        )
        botao_enviar_2.click()
        time.sleep(random.uniform(2, 3))

        # ✅ Atualiza o log
        atualizar_relatorio(f"✅ Contato '{nome_do_contato}' enviado com sucesso!")

    except Exception as e:
        atualizar_relatorio(f"❌ Erro ao enviar o contato '{nome_do_contato}': {e}")


    # Inicializa os contadores
contatos_enviados = 0
contatos_nao_enviados = 0
contatos_erro = 0
contador_mensagens = 0 

# Inicializa o contador de erros consecutivos
erros_consecutivos = 0

# Loop principal para envio de mensagens
for index, row in df.iterrows():
    numero_destino = str(row['Tel_1']).strip()
    if pd.isna(numero_destino) or numero_destino == "nan":
        continue

    mensagem = random.choice(mensagens)
    link_chat = f"https://web.whatsapp.com/send?phone={numero_destino}"
    driver.get(link_chat)

    try:
        mover_mouse(driver)  # Movimento antes de digitar
        # Aguarda até que o campo de mensagem esteja disponível
        caixa_de_texto = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )

        # Simula a digitação da mensagem letra por letra
        for char in mensagem:
            caixa_de_texto.send_keys(char)
            time.sleep(random.uniform(0.1, 0.2))  # Pequeno atraso para parecer natural
        
        time.sleep(random.uniform(0.5, 1.0))  # Pequena pausa antes de enviar
        caixa_de_texto.send_keys(Keys.ENTER)  # Envia a mensagem

        atualizar_relatorio(f"📩 Mensagem enviada para {numero_destino}")

        contatos_enviados += 1  # ✅ Atualiza o contador de mensagens enviadas

        time.sleep(random.uniform(3, 6))  # Tempo antes de enviar o contato
        enviar_contato_(nome_do_contato)(driver)  # Passando o driver como argumento

        contador_mensagens += 1
        erros_consecutivos = 0  # Reseta o contador de erros consecutivos

        time.sleep(random.randint(30, 40))  # Tempo entre os envios de mensagens

        # Pausa após 50 envios bem-sucedidos
        if contador_mensagens % 50 == 0:
            atualizar_relatorio("⏳ Pausando por 1-2 minutos após 50 envios bem-sucedidos...")
            time.sleep(random.randint(60, 120))

    except Exception as e:
        atualizar_relatorio(f"❌ Erro ao enviar mensagem para {numero_destino}: {e}")
        contatos_erro += 1
        erros_consecutivos += 1  # Aumenta o contador de erros consecutivos
        time.sleep(10)

        if erros_consecutivos >= 5:
            atualizar_relatorio("⛔ ALERTA: Muitos erros consecutivos! Possível bloqueio do WhatsApp.")
            break  # Sai do loop principal

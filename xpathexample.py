# Função para enviar o contato "Contato"
def enviar_contato_contato(driver):
    try:
        mover_mouse(driver)  # Movimento antes de clicar no anexo
        # Clicar no botão de anexar (ícone de clipe)
        botao_anexo = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button/span'))
        )
        botao_anexo.click()
        time.sleep(random.uniform(3, 6))

        # Clicar na opção "Contato"
        opcao_contato = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/div/div[4]/li/div/span'))
        )
        opcao_contato.click()
        time.sleep(random.uniform(3, 6))

        # Localizar e preencher o campo de pesquisa pelo contato "contato"
        campo_pesquisa = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/p'))
        )
        campo_pesquisa.click()
        campo_pesquisa.clear()
        campo_pesquisa.send_keys("Paradise Castle")
        time.sleep(random.uniform(3, 6))

        # Selecionar o contato encontrado
        enviar_contato_contato = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div'))
        )
        contato_paradise_castle.click()
        time.sleep(random.uniform(3, 6))

        # Clicar no primeiro botão de envio
        botao_enviar_1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div/span'))
        )
        botao_enviar_1.click()
        time.sleep(random.uniform(3, 6))

        # Confirmar o envio clicando no segundo botão de envio
        botao_enviar_2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/span'))
        )
        botao_enviar_2.click()
        time.sleep(random.uniform(3, 6))

        # Atualizar o relatório com o sucesso
        atualizar_relatorio("Contato enviado com sucesso!")

    except Exception as e:
        # Atualizar o relatório com o erro
        atualizar_relatorio(f"Erro ao enviar o contato: {e}")
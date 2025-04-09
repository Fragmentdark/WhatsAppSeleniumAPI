# 💬 Projeto de Disparo em Massa no WhatsApp com Selenium + Undetected ChromeDriver

Automatize o envio de mensagens, contatos, imagens ou outros anexos via WhatsApp Web utilizando **Python**, **Selenium** e **Undetected ChromeDriver**. Este projeto foi desenvolvido com foco em testes, estudo e possíveis usos em serviços sob responsabilidade do programador.

---

## ⚠️ Avisos Importantes

> **Use com responsabilidade.**  
> Este projeto pode gerar **banimento da conta do WhatsApp** caso as boas práticas de envio não sejam seguidas.  
> A automação é de **total responsabilidade do usuário**.

---

## 📌 Sobre o Projeto

Este repositório contém dois códigos distintos:

- **Script com envio simples**: Envia apenas mensagens para os contatos.
- **Script com anexos** (como contatos, imagens, vídeos): Utiliza XPath customizável para anexar arquivos ou informações.

O projeto simula comportamentos humanos para reduzir as chances de detecção pelo WhatsApp:

- ⏱️ Intervalos aleatórios entre envios (30 a 40 segundos)
- ⏸️ Pausa a cada 50 envios (1 a 2 minutos)
- 👁️ Digitação simulada (sem uso de `.send_keys(Keys.ENTER)` diretamente)
- 🛑 Parada automática após 5 erros consecutivos (proteção contra ban)

> ▶️ **Execução do script:**  
> Após rodar o código no terminal e pressionar `Enter`, o navegador Google Chrome será aberto automaticamente.  
> Basta escanear o **QR Code do WhatsApp Web** com o celular.  
> Assim que o WhatsApp conectar, pressione `Enter` novamente no terminal para iniciar o disparo das mensagens.


---

## 🧰 Requisitos Técnicos (WINDOWS 10 ou 11 64bits)

| Item                   | Recomendado                          |
|------------------------|--------------------------------------|
| Processador            | Intel Core i3 (3ª geração ou superior) |
| Memória RAM            | 12 GB DDR4                           |
| Armazenamento          | SSD com sistema operacional Windows 10|
| Navegador              | Google Chrome (versão compatível)    |
| Planilha Excel         | `.xlsx` com os contatos              |
| Editor de código       | Visual Studio Code                   |

5 GB de Armazenamento no diretório

---

## 🧪 Instalações Necessárias

# Instale o Python

Acesse: [Python](https://www.python.org/downloads/windows/)

Baixe a versão mais recente.

Na instalação, marque a opção “Add Python to PATH”.

Depois de instalar, abra o CMD e digite:

python --version

Se retornar algo como Python 3.x.x, está tudo certo.


# Instale bibliotecas utilizadas (Terminal do VS Code)

pip install pandas

pip install selenium

pip install undetected-chromedriver

pip install openpyxl


## 📎 Links Úteis e Contato

⚙️ WebDriver



🔗 Baixe o ChromeDriver compatível com a sua versão do Google Chrome:

👉 [Acessar ChromeDriver](https://chromedriver.chromium.org/downloads)

Após o download, extraia o executável no diretório do seu código
ou especifique o caminho diretamente no script.



## 📄 Estrutura da Planilha

A planilha deve conter pelo menos as seguintes colunas:

| Nome        | Tel_1          |
|-------------|----------------|
| João Silva  | 5511999999999  |
| Maria Luz   | 5599999999999  |

> O número deve estar no formato internacional: 55 (Brasil) + DDD + número.




## 🚀 Funcionalidades do Script

- ✅ Envio automático de mensagens personalizadas  
- ✅ Suporte a anexos (como contatos, imagens e vídeos)  
- ✅ Geração de relatório `.txt` com status de envio  
- ✅ Simulação de digitação humana  
- ✅ Pausas estratégicas para evitar banimentos  
- ✅ Contador de erros com encerramento automático após 5 falhas seguidas





## 📎 Sobre os Anexos

📎 O envio de contatos está implementado como exemplo.  
Você pode modificar o código para enviar imagens, vídeos ou outros arquivos, alterando os XPaths conforme o tipo de anexo desejado.

> 🔧 No arquivo `disparador_xpath.py`, os campos de XPath estão abertos e organizados para fácil modificação.  
> 📄 No arquivo `xpathexample.py`, você encontra exemplos reais dos XPaths utilizados e como eles aparecem nos elementos do navegador.

### Como encontrar o XPath de um elemento:

1. Acesse o [WhatsApp Web](https://web.whatsapp.com)  
2. Com o Whats App aberto, pressione `F12` para abrir o DevTools  
3. Use o cursor de inspeção e clique no elemento desejado  
4. Clique com o botão direito no HTML → **Copy → Copy XPath**

### Exemplo de uso de XPath no envio de contatos (6 etapas):

1. **Clique no ícone de clipe/anexo**  
2. **Clique na opção de envio de contato**  
3. **Clique na caixa de busca para encontrar o contato desejado**  
4. **Digite o nome do contato**  
5. **Clique na caixa de envio do contato (primeiro botão de enviar)**  
6. **Clique no segundo botão de envio (confirmação)**  

🔁 Esse processo pode ser adaptado para **qualquer ação com elementos no navegador**, como:

- Inserção de **emojis**
- Envio de **imagens**
- Envio de **vídeos**
- Outras opções do menu do WhatsApp Web

🛠️ Basta substituir os XPaths conforme o elemento desejado.







## 🧠 Boas Práticas Anti-Banimento

| Estratégia               | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| ⏱️ Delay entre envios     | Pausa aleatória de 30 a 40 segundos entre cada mensagem                  |
| ⏸️ Pausa entre lotes      | Pausa de 1 a 2 minutos a cada 50 envios bem-sucedidos                    |
| 👁️ Simulação de digitação | O texto é digitado letra por letra, imitando comportamento humano         |
| 🚫 Evite links            | Mensagens com links aumentam o risco de SPAM                             |
| ☎️ Use chip já utilizado  | Números novos são mais vulneráveis a bloqueios                           |
| 🛑 Tolerância de erros     | O script é interrompido automaticamente após 5 falhas consecutivas        |





## 📊 Relatório de Envio

Ao final do processo, um arquivo `.txt` será gerado com:

- ✅ Lista de contatos enviados com sucesso  
- ❌ Lista de falhas  
- 📤 Mensagens/script enviados  

Esse relatório pode ser utilizado para controle interno ou estatísticas.

---

## 👨‍💻 Responsabilidade

Este projeto é fornecido somente para fins educacionais e testes.  
**Não nos responsabilizamos por banimentos ou mau uso da ferramenta.**

---

## 🤝 Contribuição

Use, estude, melhore e compartilhe este projeto com a comunidade.






Para sugestões, melhorias ou bugs, sinta-se à vontade para abrir uma Issue.




## 📬 Entre em contato

- 📧 **Email:** [contato@jenovatech.com.br](mailto:contato@jenovatech.com.br)  
- 🔗 **LinkedIn:** [linkedin.com/in/reinaldosilveiratech](https://www.linkedin.com/in/reinaldosilveiratech)  
- 📷 **Instagram:** [@jenovatech](https://www.instagram.com/jenovatech/?igsh=MW9zaGsyNGMzazgycA%3D%3D)



---

⭐ Se você gostou do projeto, deixe uma estrela no repositório e compartilhe com a comunidade!


# 💬 Projeto de Disparo em Massa no WhatsApp com Selenium + Undetected ChromeDriver

Automatize o envio de mensagens, contatos, imagens ou outros anexos via WhatsApp Web utilizando **Python**, **Selenium** e **Undetected ChromeDriver**. Este projeto foi desenvolvido com foco em testes, estudo e possíveis usos em serviços sob responsabilidade do programador.

---

## ⚠️ Avisos Importantes

> **Use com responsabilidade.**  
> Este projeto pode gerar **banimento da conta do WhatsApp** caso as boas práticas de envio não sejam seguidas.  
> A automação é de **total responsabilidade do usuário**.

---

## 📌 Sobre o Projeto

- Este repositório contém **dois códigos** distintos:
  1. **Script com envio simples**: Envia apenas mensagens para os contatos.
  2. **Script com anexos (como contatos, imagens, vídeos)**: Utiliza `XPath` customizável para anexar arquivos ou informações.

- O projeto simula comportamentos humanos para reduzir as chances de detecção pelo WhatsApp:
  - Intervalos aleatórios entre envios (30 a 40 segundos)
  - Pausa a cada 50 envios (1 a 2 minutos)
  - Digitação simulada (sem uso de `.send_keys(Keys.ENTER)` diretamente)
  - Parada automática após 5 erros consecutivos (proteção contra ban)

---

## 🧰 Requisitos Técnicos

| Item                   | Recomendado                          |
|------------------------|--------------------------------------|
| Processador            | Intel Core i3 (3ª geração ou superior) |
| Memória RAM            | 12 GB DDR4                           |
| Armazenamento          | SSD com sistema operacional          |
| Navegador              | Google Chrome (versão compatível)    |
| Planilha Excel         | `.xlsx` com os contatos              |
| Editor de código       | Visual Studio Code                   |

---

## 🧪 Instalações Necessárias

```bash
# Instale o Python
sudo apt install python3

# Instale o gerenciador de pacotes pip
sudo apt install python3-pip

# Instale bibliotecas utilizadas
pip install pandas
pip install selenium
pip install undetected-chromedriver
pip install openpyxl

## ⚙️ WebDriver

Baixe o ChromeDriver compatível com sua versão do Google Chrome: 👉 [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

Extraia o arquivo no diretório do seu código ou especifique o caminho no script.

## 📄 Estrutura da Planilha

A planilha deve conter pelo menos:

| Nome       | Tel_1         |
|------------|---------------|
| João Silva | 5511999999999 |
| Maria Luz  | 5599999999999 |

O número deve estar no formato internacional: **55** (Brasil) + DDD + número.

## 🚀 Funcionalidades do Script

- ✅ Envio automático de mensagens personalizadas
- ✅ Suporte a anexos (como contatos, imagens e vídeos)
- ✅ Geração de relatório `.txt` com status de envio
- ✅ Simulação de digitação humana
- ✅ Pausas estratégicas para evitar banimentos
- ✅ Contador de erros com encerramento automático após 5 falhas seguidas

## 📎 Sobre os Anexos

O envio de contatos está implementado como exemplo.

Você pode modificar o código para enviar imagens, vídeos ou outros anexos, alterando os XPaths conforme o item que deseja anexar.

Para encontrar o XPath de qualquer elemento:
- Acesse o WhatsApp Web
- Pressione `F12` para abrir o DevTools
- Use o cursor de inspeção e clique no elemento desejado
- Clique com o botão direito no HTML e selecione: **Copy → Copy XPath**

## 🧠 Boas Práticas Anti-Banimento

| Estratégia               | Descrição                                                                   |
|--------------------------|-----------------------------------------------------------------------------|
| ⏱️ Delay entre envios      | Pausa aleatória de 30 a 40 segundos entre cada mensagem                      |
| ⏸️ Pausa entre lotes       | Pausa de 1 a 2 minutos a cada 50 envios bem-sucedidos                         |
| 👁️ Simulação de digitação   | O texto é digitado letra por letra (não colado), imitando comportamento humano  |
| 🚫 Evite links              | Mensagens com links aumentam o risco de SPAM                                  |
| ☎️ Use chip já utilizado   | Números novos são mais vulneráveis a bloqueios                              |
| 🛑 Tolerância de erros      | O script é interrompido após 5 falhas consecutivas                            |

## 📊 Relatório de Envio

Ao final do processo, um arquivo `.txt` será gerado contendo:
- Lista de contatos enviados com sucesso ✅
- Lista de falhas ❌
- Mensagens/script enviados 📤

Esse relatório pode ser utilizado para fins estatísticos ou controle de campanhas.

## 👨‍💻 Responsabilidade

> Este código foi feito com fins educacionais e de testes.  
> Não nos responsabilizamos pelo uso indevido da automação ou banimentos decorrentes.

🤝 Contribuição
Fique à vontade para usar, estudar, melhorar e compartilhar este projeto com outros desenvolvedores ou pessoas interessadas em automação.

⭐ Se você gostou do projeto, deixe uma estrela e compartilhe com a comunidade!


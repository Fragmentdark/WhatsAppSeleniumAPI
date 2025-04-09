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

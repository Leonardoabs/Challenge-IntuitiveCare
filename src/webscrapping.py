from auxiliares import aguardar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import zipfile
import logging
import os
import pdfplumber
import pandas as pd


def pdf1(driver):
    url = ('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-'
           'sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I'
           '_Rol_2021RN_465.2021_RN627L.2024.pdf')

    logging.info("Url do PDF 1.")
    driver.execute_script(f"window.open('{url}', '_blank');")


def pdf2(driver):
    url = ('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-'
           'sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II'
           '_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf')

    logging.info("Url do PDF 2.")
    driver.execute_script(f"window.open('{url}', '_blank');")


def zip_pdf(diretorio_download):
    try:
        pdfs = [
            f for f in os.listdir(
                diretorio_download) if f.lower().endswith(".pdf")]

        pdfs.sort(
            key=lambda f: os.path.getmtime(
                os.path.join(diretorio_download, f)), reverse=True)

        with zipfile.ZipFile(
            os.path.join(diretorio_download,
                         "PDFS_Challenge.zip"), "w") as zipf:

            for pdf in pdfs[:2]:
                zipf.write(os.path.join(diretorio_download, pdf), pdf)
        logging.info("PDFs compactados com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao compactar PDFs: {e}")


def extrair_anexo1(caminho_pdf, nome_csv):
    try:
        dfs = []
        with pdfplumber.open(caminho_pdf) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                if tables:
                    for table in tables:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        dfs.append(df)
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(nome_csv, index=False)
    except Exception as e:
        logging.error(f"Erro ao extrair tabela do PDF: {e}")


def substituir_abreviacoes(nome_csv):
    try:
        df = pd.read_csv(nome_csv)
        df.rename(
            columns={'OD': 'Outras Despesas',
                     'AMB': 'Atendimento Ambulatorial'}, inplace=True)

        df.to_csv(nome_csv, index=False)
        logging.info("Abreviações substituídas.")
    except Exception as e:
        logging.error(f"Erro nas abreviações: {e}")


def zip_csv(caminho_csv, nome_zip):
    try:
        with zipfile.ZipFile(nome_zip, 'w') as zipf:
            zipf.write(caminho_csv, os.path.basename(caminho_csv))
        logging.info(f"CSV zipado eM: {nome_zip}")
    except Exception as e:
        logging.error(f"Erro no CSV: {e}")


# Configuração do logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    chrome_options = Options()
    donwload = os.path.join(os.path.expanduser("~"), "Downloads")

    # Donwload Automático
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": donwload,
        "plugins.always_open_pdf_externally": True
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao'
        '-da-sociedade/atualizacao-do-rol-de-procedimentos')

    logging.info("Página carregada com sucesso.")

    # Recusando Cookies
    aguardar(
        driver,
        By.XPATH,
        '/html/body/div[5]/div/div/div/div/div[2]/button[2]').click()

    pdf1(driver)
    logging.info("Função PDF 1.")
    pdf2(driver)
    logging.info("Função PDF 2.")

    diretorio_download = os.path.join(os.path.expanduser("~"), "Downloads")
    zip_pdf(diretorio_download)
    logging.info("Função Zip PDFS")

    # Extração e processamento do Anexo I
    caminho_pdf_anexo1 = os.path.join(
        diretorio_download, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')

    nome_csv = os.path.join(diretorio_download, 'tabela_anexo1.csv')
    nome_zip_csv = os.path.join(diretorio_download, 'Teste_Leonardo_Alves.zip')

    extrair_anexo1(caminho_pdf_anexo1, nome_csv)
    logging.info("Função Extração dados PDF")
    substituir_abreviacoes(nome_csv)
    logging.info("Função Abreviações")
    zip_csv(nome_csv, nome_zip_csv)
    logging.info("Função Zip CSV")

except Exception as e:
    logging.error(f"Erro no Código: {e}")

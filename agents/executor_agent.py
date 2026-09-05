from tools.web_search import search_web
from tools.pdf_downloader import download_pdfs

def execute_plan(topic, folder):
    results = search_web(topic)

    pdfs = download_pdfs(results, folder)

    return results, pdfs

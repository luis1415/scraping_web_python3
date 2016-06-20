# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import wget

'''
Scraping web - Python 3
'''


def scraping_web(url, patron_link):
    """
    Esta funcion me pide una url y me devuelve un lista con los links
    :param url: pide una url como http://www.google.com con http
    :param patron_link: es un patron que aparece en el link <a href=>
    :return: devuelve una lista con los links de la pagina, que son de tipo excel xls
    """

    page = urlopen(url)

    bs = BeautifulSoup(page.read(), 'lxml')
    a = bs.find_all("a")

    # crea listas vacias para guardar los links
    links = []
    archivos_excel = []

    for link in a:
        links.append(link.get('href'))

    for link in links:
        if patron_link in str(link):
            print(link)
            archivos_excel.append(link)

    return archivos_excel


def descargar(links, patron_error, url_base):
    """
    descarga todos los links de excel
    :param links: es una lista con los links de excel
    :param patron_error: es un patron que se encuentra en los links que no queremos
    :return: solo descarga en la carpeta datos
    """

    links_buenos = []
    for link in links:
        if patron_error not in link:
            links_buenos.append(link)

    for link in links_buenos:
        if 'xls' in link:
            link = link.replace(" ", "%20")
            wget.download(url_base + link)

'''
Ejecucion de funciones
'''

# url de ejemplo con muchos archivos para descargar
url = 'https://www.superfinanciera.gov.co/jsp/loader.jsf?lServicio=Publicaciones&lTipo=publicaciones&lFuncion=loadContenidoPublicacion&id=10427'

# patron que aparece en los links que me interesan
patron = 'xls'

lista_links = scraping_web(url, patron)

print(lista_links, len(lista_links))

# para descargar necesitamos la url_base
url_base = 'https://www.superfinanciera.gov.co'

# la funcion descargar descarga toda la lista de links
descargar(lista_links, 'http', url_base)

#listo
print('listo...')

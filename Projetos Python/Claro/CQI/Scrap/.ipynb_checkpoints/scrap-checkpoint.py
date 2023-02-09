from gettext import install
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options

import gomracess
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import selenium

from time import sleep


#acesando wpage

options=Options()
options.headless= False #executar de forma visivel ou não
navegador=webdriver.Firefox(options=options)

link="http://10.119.231.252/apex/f?p=101:LOGIN::NOVOACESSO"
navegador.get(url=link)
sleep(1)
import requests
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup


source = requests.get('https://www.nytimes.com/topic/destination/brazil').text

web = BeautifulSoup(source, 'lxml')
#Criando arquivo csv
csv_file = open('dados.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titulo','Descricao'])

for article in web.find_all('article',{'itemtype': 'http://schema.org/NewsArticle'}):
    titulo = article.find('h2', {'class': 'headline'}).text
    print("Titulo: " + titulo + "\n")
    descricao = article.find('p', {'itemprop': 'description'}).text
    print("Descricao: " + descricao + "\n") 
    print "--------------------------------------------------------------------------\n"
    csv_writer.writerow([titulo,descricao])

csv_file.close()

# coding: utf8
import urllib
import csv

srcurl = 'http://www.ccomptes.fr/content/download/66943/1841804/version/1/file/Cartographie_des_taxes_affectees_2007-2013.csv'
archive_path = 'archive/Cartographie_des_taxes_affectees_2007-2013.csv'
out_path = 'data/taxes.csv'

def download():
    urllib.urlretrieve(srcurl, archive_path)

def clean():
    # Input fields
    # Identifiant de la taxe pour le rapport particulier;Nom de la taxe;Article;Corpus;Organisme affectataire;Classification du Conseil des pr�l�vements obligatoires;2007;2008;2009;2010;2011;2012 (p);2013 (p)
    reader = csv.reader(open(archive_path), delimiter=';')
    fields = [
        'uid', 
        'tax-identifier',
        'tax-name',
        'article',
        'corpus',
        'organisme-affectataire',
        'classification',
        'year',
        'montant'
        ]
    writer = csv.DictWriter(open(out_path, 'w'), lineterminator='\n',
            fieldnames=fields)
    writer.writeheader()
    # skip header
    reader.next()
    count = -1
    for row in reader:
        for yearidx in range(7):
            amount = row[6+yearidx].strip()
            if amount:
                count += 1
                amount = float(amount.replace(',', '.'))
                out = {
                    'uid': count,
                    'tax-identifier': row[0],
                    'tax-name': row[1],
                    'article': row[2],
                    'corpus': row[3],
                    'organisme-affectataire': row[4],
                    'classification': row[5],
                    'year': 2007 + yearidx,
                    'montant': amount
                    }
                writer.writerow(out)

if __name__ == '__main__':
    download()
    clean()


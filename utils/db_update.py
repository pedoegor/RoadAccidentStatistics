from lxml.html import parse

from urllib import urlretrieve

from RoadAccidentStatistics.models import DownloadFile

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))







#WARNING NEEDS PARSING
def update_data_with(file_path):

    #here you should use your parser to parse file and fill database
    pass









def load_open_data():

    page = parse('http://www.gibdd.ru/stat/').getroot()

    hrefs = page.cssselect("a")

    for row in hrefs:

        if 'xls' in row.get("href").split('.'):

            is_downloaded = fasle

            new_name = row.get("href").split('/')[-1]

            files = DownloadFile.objects.all()

            for file in files:
                if file.name == new_name:
                    is_downloaded = true
                    break

            if is_downloaded:
                continue

            f = DownloadFile(name=new_name)

            f.save()

            url = 'http://www.gibdd.ru/stat/' + row.get("href")

            destination = os.path.join(BASE_DIR, 'tables/' + new_name)
            urlretrieve(url, destination)


            update_data_with(destination)










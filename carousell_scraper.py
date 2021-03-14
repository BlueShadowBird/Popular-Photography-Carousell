import csv
import requests
from bs4 import BeautifulSoup


class CarousellScraper:
    def __init__(self):
        self.session = requests.session()
        self.result = []

    def scrape(self):
        url = 'https://id.carousell.com/categories/photography-6/'
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'D_mT M_bX D_S'})

        divs = main_div.find_all('div', attrs={'class', 'D_pR M_eE D_pO D_mQ'})

        for div in divs:
            title = div.find('p', attrs={'class':
                                         'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text
            price = div.find('p', attrs={'class':
                                         'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_a_'}).text
            desc = div.find('p', attrs={'class':
                                        'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_aA'}).text
            condition = div.find('p', attrs={'class':
                                             'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_aA'}).text
            pic = div.find('div', attrs={'class': 'D_qe'}).find('img')['src']
            url = 'https://id.carousell.com{}'.format(div.find('a', attrs={'class': 'D_ft M_bh'})['href'])

            shop = div.find('a', attrs={'class': 'D_pY M_eL D_ft M_bh'})
            shop_url = 'https://id.carousell.com{}'.format(shop['href'])
            shop_name = shop.find('p', attrs={'class': 'D_aZ M_bz D_bk M_bJ D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text

            camera = {'title': title, 'price': price, 'desc': desc, 'condition': condition, 'url': url, 'pic': pic, 'shop_url': shop_url, 'shop_name': shop_name}

            self.result.append(camera)

    def get(self):
        return self.result

    def generate_cvs(self):
        csv_writer = csv.writer(open('result.csv', 'w+', encoding='utf8', newline=''))
        csv_writer.writerow(['title', 'price', 'desc', 'condition', 'url', 'picture'])
        for camera in self.result:
            csv_writer.writerow([camera['title'], camera['price'], camera['desc'], camera['condition'], camera['url'], camera['pic'], camera['shop_url'], camera['shop_name']])

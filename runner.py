from flask import Flask, render_template,redirect

from carousell_scraper import CarousellScraper

scraper = CarousellScraper()
scraper.scrape()
scraper.generate_cvs()

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/kamera_popular', code=302)


@app.route('/kamera_popular')
def camera_popular():
    return render_template('result.html', cameras=scraper.get())


if __name__ == '__main__':
    app.run(debug=True)

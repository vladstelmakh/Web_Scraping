import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request, redirect, url_for, send_file
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
app = Flask(__name__)


app.config['BOOTSTRAP_SERVE_LOCAL'] = True


data = []

def scrape_data(query):
    global data
    url = f"https://flagma.pl/products/q={query}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('div', class_='page-list-item')
    scraped_data = []

    for product in products:
        title = product.find('h2').text.strip() if product.find('h2') else ""
        price = product.find('div', class_='price').find('span').text.strip() if product.find('div',
                                                                                              class_='price') else ""
        description = product.find('div', class_='text').text.strip() if product.find('div', class_='text') else ""
        company_name = product.find('span', style="font-weight: 500;").text.strip() if product.find('span',
                                                                                                    style="font-weight: 500;") else ""
        date = product.find('div', class_='date').text.strip() if product.find('div', class_='date') else ""
        link = product.find('a', class_='photo')['href'] if product.find('a', class_='photo') else ""
        image_url = product.find('div', class_='img-container').find('img')['src'] if product.find('div',
                                                                                                   class_='img-container') else ""

        if any([title, price, description, company_name, date, link, image_url]):
            scraped_data.append({
                'Title': title,
                'Price': price,
                'Description': description,
                'Company': company_name,
                'Date': date,
                'Link': link,
                'Image URL': image_url
            })

    data = scraped_data


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        scrape_data(query)
        return redirect(url_for('results'))
    return render_template('index.html')


@app.route('/results')
def results():
    return render_template('results.html', data=data)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    global data
    if request.method == 'POST':
        data[index]['Title'] = request.form['Title']
        data[index]['Price'] = request.form['Price']
        data[index]['Description'] = request.form['Description']
        data[index]['Company'] = request.form['Company']
        data[index]['Date'] = request.form['Date']
        data[index]['Link'] = request.form['Link']
        data[index]['Image URL'] = request.form['Image URL']
        return redirect(url_for('results'))
    return render_template('edit.html', product=data[index], index=index)


@app.route('/delete/<int:index>')
def delete(index):
    global data
    data.pop(index)
    return redirect(url_for('results'))


@app.route('/plots')
def plots():
    df = pd.DataFrame(data)
    df['Price'] = df['Price'].str.replace(' zł/szt', '').str.replace(' ', '').astype(float)

    plt.figure(figsize=(10, 6))
    plt.bar(df['Title'], df['Price'], color='blue')
    plt.xticks(rotation=90)
    plt.xlabel('Title')
    plt.ylabel('Price (zł)')
    plt.title('Prices of Products')
    price_plot = save_plot_to_base64(plt)

    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=10, color='green')
    plt.xlabel('Price (zł)')
    plt.ylabel('Number of Products')
    plt.title('Price Distribution')
    hist_plot = save_plot_to_base64(plt)

    company_counts = df['Company'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(company_counts, labels=company_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Company Distribution')
    pie_plot = save_plot_to_base64(plt)

    return render_template('plot.html', price_plot=price_plot, hist_plot=hist_plot, pie_plot=pie_plot)


def save_plot_to_base64(plt):
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url

@app.route('/download')
def download():
    si = io.StringIO()
    cw = csv.DictWriter(si, fieldnames=['Title', 'Price', 'Description', 'Company', 'Date', 'Link', 'Image URL'])
    cw.writeheader()
    cw.writerows(data)
    output = io.BytesIO()
    output.write(si.getvalue().encode('utf-8'))
    output.seek(0)

    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='products_data.csv')
if __name__ == '__main__':
    app.run(debug=True,port=5002)

from flask import Flask
import random
app = Flask(__name__)
import requests

@app.route("/")
def hello_world():

    return '<h1>Hello, World!</h1><a href="/1">Rastgele bir gerçeği görüntüle!</a><br><a href="/y_t">Yazı tura at.</a><br><a href="/r_s">Rastgele sayı.</a><br><a href="/r_p">Şifre oluşturucu.</a><br><a href="/t_d">Tilki resmi gönder.</a><br><a href="/g_o_r">Ördek resmi gönder.</a><br><a href="/k_r_g">Köpek resmi gönder.</a>'
liste=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
       "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
       "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
       "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]


@app.route("/1")
def r_i():
    return f'<p>{random.choice(liste)}</p><a href="/">Geri dön.</a>'


@app.route("/y_t")
def y_t():
    if random.randint(1,2)==1:
        x="Yazı"
    else:
        x="Tura"
    return f'<p>{x}</p>'

@app.route("/r_s")
def r_s():
    return  f'<p>{random.randint(1,1000)}</p><a href="/">Geri dön.</a>'

@app.route("/r_p")
def r_p(uzunluk=10):
    sifre=""
    harfler="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sayilar="1234567890"
    isaretler="+-/*!&$#?=@"
    a=[harfler,sayilar,isaretler]

    for i in range(uzunluk):
        x=random.choice(a)
        sifre+=random.choice(x)
    return f"<p>{sifre}</p><a href='/''>Geri dön.</a>"

@app.route("/t_d")
def t_d():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return f'<div><iframe src="{data["image"]} "frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 1000px; height: 1000px"></iframe></div><a href="/"">Geri dön.</a>'


@app.route("/g_o_r")
def g_o_r():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return f'<div><iframe src="{data["url"]} "frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 1000px; height: 1000px"></iframe></div><a href="/"">Geri dön.</a>'

@app.route("/k_r_g")
def k_r_g():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return f'<div><iframe src="{data["url"]} "frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 1000px; height: 1000px"></iframe></div><a href="/"">Geri dön.</a>'

if __name__=="__main__":

    app.run(debug=True)

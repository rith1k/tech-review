from datetime import date
from flask import Flask, redirect, request, url_for, render_template,session
import  sys 
from bs4 import BeautifulSoup
import requests
import sqlite3
import os
app = Flask(__name__)       # our Flask app
app.secret_key = os.urandom(24)

DB_FILE = 'laptop.db'    		# file for our Database 
# insert function for register


class addTable:
    def addWeather(temp):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select * from weather")
        rv= cursor.fetchall()
        name="Dubai"
        id=1
        if len(rv)==0:
            params = {'id': id, 'name': name , 'temp':temp}
            cursor.execute("insert into weather VALUES (:id, :name, :temp)", params)
        else:
            cursor.execute("update weather set temp = ? where id = ? ", (temp, id))
        connection.commit()
        cursor.close()
    def addTip(title, en3, img, meta, para):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select * from tips")
        rv= cursor.fetchall()
        params = {'title': title, 'en3': en3 , 'img':img , 'meta':meta}
        cursor.execute("insert into tips VALUES ( :title, :en3,:img, :meta)", params)
        connection.commit()
        cursor.close()
    def addNews(title, pic, caption, time,author, link):

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:        
            params = {'title':title , 'caption':caption, 'pic' :pic, 'author':author, 'link': link, 'time': time}
            cursor.execute("insert into news VALUES (:title, :caption, :pic, :author, :link, :time)", params)
        except:
            print("aready exists!")    
        connection.commit()
        cursor.close()
    def addCoin(temp):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select * from price")
        rv= cursor.fetchall()
        name="Bitcoin"
        id=1
        if len(rv)==0:
            params = {'id': id, 'name': name , 'price':temp}
            cursor.execute("insert into price VALUES (:id, :name, :price)", params)
        else:
            cursor.execute("update price set price = ? where id = ? ", (temp, id))
        
        connection.commit()
        cursor.close()
    def addTime(temp):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select * from time")
        rv= cursor.fetchall()
        name="Dubai"
        id=1
        params = {'id': id, 'name': name , 'time':temp}
        cursor.execute("insert into time VALUES (:id, :name, :time)", params)
        connection.commit()
        cursor.close()
 

def coin():
    url = "https://cryptowat.ch/assets/btc"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    today2 = soup.find('div', class_= 'flex items-center')
    today3= today2.findNext('span', class_="woobJfK-Xb2EM1W1o8yoE")
    today4= today3.findNext('span', class_="price").text
    A=addTable
    A.addCoin(today4)


    return today4
def weather():
    url1 = "https://www.bbc.co.uk/weather/292223"
   
    data1 = requests.get(url1).text
    soup1 = BeautifulSoup(data1, 'html.parser')
    today1 = soup1.find('div', {'data-component-id': 'forecast'})
    temp = today1.find(class_='wr-value--temperature--c').get_text()
    A=addTable
    A.addWeather(temp)

    
    return temp
def local_time():
    try:
        url = "https://www.timeanddate.com/worldclock/united-arab-emirates"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find(id="tz-legend-1").get_text()
        A=addTable
        A.addTime(today)

    except: 
        today ="Not avaliable try again later"
    return today



def _insert(username, password, email):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'password': password, 'email':email}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into user VALUES (:username, :password, :email)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# redirecting to razer.html
@app.route('/razer', methods=['POST', 'GET'])
def razer():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
        url = "https://www.laptopmag.com/razer-blade-15-studio-edition"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM razer")
        rv = cursor.fetchall()
        cursor.close()
        return render_template('/razer.html',  review=temp, today_weather=today_weather, local_time=current_time,coin=coin1,entries=rv)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# insert function for razer reviews
def _newcomment1(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into razer VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# redirecting to guestbook
@app.route('/comment10', methods=['POST'])
def comment10():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        _newcomment10(request.form['name'], request.form['comment'])
        return redirect(url_for('guestbook'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# Retrieve guestbook reviews
@app.route('/guestbook', methods=['POST', 'GET'])
def guestbook():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guestbook")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/guestbook.html',  today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# insert function for guestbook
def _newcomment10(name, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'name': name, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into guestbook VALUES (:name, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

@app.route('/l')
def l():
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        return render_template('l.html',  today_weather=today_weather, local_time=current_time,coin=coin1)
# redirecting to razer
@app.route('/comment1', methods=['POST'])
def comment1():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        _newcomment1(session['username'], request.form['comment'])
        return redirect(url_for('razer'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# retrive comments for asus
@app.route('/asus', methods=['POST', 'GET'])
def asus():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        url = "https://www.laptopmag.com/reviews/asus-rog-strix-scar-iii"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM asus")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/asus.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# insert function for asus
def _newcomment2(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into asus VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# redirect for asus
@app.route('/comment2', methods=['POST'])
def comment2():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        _newcomment2(session['username'], request.form['comment'])
        return redirect(url_for('asus'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# retrive comment for acer
@app.route('/acer', methods=['POST', 'GET'])
def acer():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
        url = "https://www.laptopmag.com/reviews/acer-chromebook-715"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
               
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM acer")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/acer.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# insert function for acer
def _newcomment3(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into acer VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# redirect for acer
@app.route('/comment3', methods=['POST'])
def comment3():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        _newcomment3(session['username'], request.form['comment'])
        return redirect(url_for('acer'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# retrive for msi
@app.route('/msi', methods=['POST', 'GET'])
def msi():
    try:
        url = "https://www.laptopmag.com/reviews/msi-prestige-15"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM msi")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/msi.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# insert function for msi
def _newcomment4(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into msi VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# redirect for msi
@app.route('/comment4', methods=['POST'])
def comment4():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        _newcomment4(session['username'], request.form['comment'])
        return redirect(url_for('msi'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# retrieve comments for macbook
@app.route('/macbook', methods=['POST', 'GET'])
def macbook():
    try:
        url = "https://www.laptopmag.com/reviews/laptops/apple-macbook-air-2019"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM macbook")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/macbook.html',  review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# insert function for macbook
def _newcomment5(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into macbook VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# redirect for macbook
@app.route('/comment5', methods=['POST'])
def comment5():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _newcomment5(session['username'], request.form['comment'])
        return redirect(url_for('macbook'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# retrieve comment for surface
@app.route('/surface', methods=['POST', 'GET'])
def surface():
    try:
        url = "https://www.laptopmag.com/reviews/microsoft-surface-laptop-3-13-inch"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM surface")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/surface.html', review=temp,  today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# insert function for surface
def _newcomment6(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into surface VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

#redirect for surface
@app.route('/comment6', methods=['POST'])
def comment6():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _newcomment6(session['username'], request.form['comment'])
        return redirect(url_for('surface'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
  
# retrive comments for yoga

@app.route('/yoga', methods=['POST', 'GET'])
def yoga():
    try:
        url = "https://www.laptopmag.com/reviews/lenovo-yoga-c940-15-inch"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM yoga")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/yoga.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())


# insert function for yoga
def _newcomment7(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into yoga VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# redirect function for yoga
@app.route('/comment7', methods=['POST'])
def comment7():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _newcomment7(session['username'], request.form['comment'])
        return redirect(url_for('yoga'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# retrieve comments for lg

    


@app.route('/lg', methods=['POST', 'GET'])
def lg():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
        url = "https://www.laptopmag.com/reviews/laptops/lg-gram-17"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM lg")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/lg.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# insert function for lg
def _newcomment8(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into lg VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# redirect function for lg
@app.route('/comment8', methods=['POST'])
def comment8():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _newcomment8(session['username'], request.form['comment'])
        return redirect(url_for('lg'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# retrieve comments for thinkpad
@app.route('/thinkpad', methods=['POST', 'GET'])
def thinkpad():
    try:
        url = "https://www.laptopmag.com/reviews/lenovo-thinkpad-x1-extreme-gen-2"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('div', id= 'article-body')
        temp = today.find('p').get_text()
        
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM thinkpad")
        rv1 = cursor.fetchall()
        cursor.close()
        return render_template('/thinkpad.html', review=temp, today_weather=today_weather, local_time=current_time,coin=coin1, entries=rv1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# insert function for thinkpad
def _newcomment9(username, comment):
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        params = {'username': username, 'comment': comment}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into thinkpad VALUES (:username, :comment)", params)
        connection.commit()
        cursor.close()
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# redirect for thinkpad
@app.route('/comment9', methods=['POST'])
def comment9():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _newcomment9(session['username'], request.form['comment'])
        return redirect(url_for('thinkpad'))
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# render template for home
@app.route('/')
def index():
    try:
        url = "https://www.ricksdailytips.com/"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('article', class_= 'post-43597 post type-post status-publish format-standard has-post-thumbnail sticky category-computer-tips tag-daily-deal tag-daily-pick entry')
        title=today.find('h2', class_="entry-title").text
        meta=today.find('p', class_="entry-meta").text
        en1=today.find("div", class_="entry-content")
        en2=en1.findNext('p')
        en3=en2.findNext('p').text
        en=en2.find('a', {"rel":"nofollow sponsored"})
        img=en.find("img").attrs['src']
        para=en.get_text
        coin1=coin()      
        current_time = local_time()
        
        A=addTable
        A.addTip(title, en3, img, meta, para)
        temp=weather()
        
        return render_template('index.html', title=title, en3=en3, img=img, meta=meta, para=para, today_weather=temp, local_time=current_time,coin=coin1)
    except:
        return render_template('error.html',  today_weather=temp, local_time=current_time,coin=coin1, msg=sys.exc_info())


@app.route('/news')
def news():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        url = ("https://www.laptopmag.com/laptops")
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        news = dict()
        allNews = dict()
        counter = 1
        for news in soup.findAll('div', class_="listingResult"):
            news1=news.findNext('a')
            news3=news1.find('article')
            news2=news3.find('div', class_="image")
            news4=news3.find('div', class_="content")
            news5=news4.find("p", class_="byline")  
            news = {'pic': news2.find("div", class_="image-remove-reflow-container landscape").attrs['data-original'], 'link': news1['href'] ,'author': news5.find("span").text,
            'time':news5.find( class_="published-date relative-date").attrs['data-published-date'][0:10], 'title': news4.find('h3').text,  'caption': news4.find('p', class_="synopsis").text}
            allNews[counter] = news
            A=addTable
            A.addNews(news['title'],news['pic'], news['caption'], news['time'], news['author'],news['link'])
            counter += 1
           
        return render_template('news.html',  today_weather=today_weather, local_time=current_time,coin=coin1, allNews=allNews, counter=counter)

    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

# insert function for signup
@app.route('/sign', methods=['POST'])
def sign():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        _insert(request.form['username'], request.form['password'], request.form['email'])
        return render_template('login.html',  today_weather=today_weather, local_time=current_time,coin=coin1, register_success="You've been successfully registered please log in")
    
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# function for login


@app.route('/login', methods=['POST','GET'])
def login():
    try:
        url = "https://www.ricksdailytips.com/"
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        today = soup.find('article', class_= 'post-43597 post type-post status-publish format-standard has-post-thumbnail sticky category-computer-tips tag-daily-deal entry')
        title=today.find('h2', class_="entry-title").text
        meta=today.find('p', class_="entry-meta").text
        en1=today.find("div", class_="entry-content")
        en2=en1.findNext('p')
        en3=en2.findNext('p').text
        en=en2.find('a', {"rel":"nofollow sponsored"})
        img=en.find("img").attrs['src']
        para=en.get_text
        coin1=coin()      
        current_time = local_time()
        temp=weather()
        
        
 
        if request.method == 'POST':
            query = "select * from user where username = '" + request.form['username']
            query = query + "' and password = '" + request.form['password'] + "';"
            connection = sqlite3.connect(DB_FILE)
            cur = connection.execute(query)
            rv = cur.fetchall()
            cur.close()
            if len(rv) == 1:
                session['username'] = request.form['username']
                session['logged in'] = True

                return render_template('index.html', title=title, en3=en3, img=img, meta=meta, para=para, today_weather=temp, local_time=current_time,coin=coin1)
            else:
                return render_template('login.html',  today_weather=temp, local_time=current_time,  coin=coin1)
        else:
            return render_template('login.html',  today_weather=temp, local_time=current_time,  coin=coin1)  
    except:
        return render_template('error.html',  today_weather=temp, local_time=current_time,   coin=coin1, msg=sys.exc_info())
# function for logout
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        session.pop("logged in",None)
        session.pop("username",None)
        return render_template("index.html", logout_msg="Successfully Logged out")
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# function for contactus
@app.route('/aboutus')
def aboutus():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        return render_template('aboutus.html',  today_weather=today_weather, local_time=current_time,coin=coin1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())
# function for search
@app.route('/search')

def search():
    try:
        coin1=coin()
      
        
        today_weather = weather()
        current_time = local_time()
 
        return render_template('search.html',  today_weather=today_weather, local_time=current_time,coin=coin1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())


# function for reviews
@app.route('/reviews')

def reviews():
    try:
        coin1=coin()        
        today_weather = weather()
        current_time = local_time()
        return render_template('reviews.html',  today_weather=today_weather, local_time=current_time,coin=coin1)
    except:
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1, msg=sys.exc_info())

@app.route('/<url>')
def get_page(url):
    try:
        coin1=coin()
        today_weather = weather()
        current_time = local_time()
        return render_template('{}.html'.format(url),  today_weather=today_weather, local_time=current_time,coin=coin1)
    except:
        
        return render_template('error.html',  today_weather=today_weather, local_time=current_time,coin=coin1)

if __name__ == '__main__':
    app.run(debug = True)
			
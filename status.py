import sqlite3
import time
import requests
import datetime
import matplotlib.pyplot as plt

db_name = 'status.db'
table_name = 'task'


def update_status(url, status, dt):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        '''create table if not exists task ([url] text, [status] integer, [dt] date) ''')
    c.execute(
        f""" INSERT or IGNORE into task (url, status, dt) VALUES('{url}', '{status}', '{dt}') ; """)
    conn.commit()
    conn.close()


def get_graph():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('SELECT url, status, dt FROM  task')
    data = c.fetchall()

    url = []
    status = []
    date = []

    for row in data:
        url.append(row[0])
        status.append(row[1])
        date.append(row[2])

    plt.plot(date, status)
    plt.xlabel('time')
    plt.ylabel('status')
    plt.title('Website status')
    plt.show()


def getUrlStatus(url):
    try:
        response = requests.get(url)
        status = response.status_code
        update_status(url, status, datetime.datetime.now())
        print(url, status, datetime.datetime.now())

    except print(0):
        pass


def executeSomething():
  # here goes the url
    getUrlStatus('http://youtube.com')
    # graph
    get_graph()
    # timer
    time.sleep(60)


while True:
    executeSomething()

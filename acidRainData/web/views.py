from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import socket

def index(request):
    return render(request, "base.html", locals())

# Create your views here.
def rainfall(request):
    conn = None
    try:
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "ph_rain")
        c = conn.cursor()
        conn.set_character_set('utf8')
        c.execute("SELECT * FROM hourly_data WHERE ItemName='雨量'") #ORDER BY SiteId
        r = c.fetchall()
        conn.close()
    except socket.error as serror:
        if conn is not None:
            conn.close()
    return render(request, "display.html", locals())

def ph_rain(request):
    conn = None
    try:
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "ph_rain")
        c = conn.cursor()
        conn.set_character_set('utf8')
        c.execute("SELECT * FROM hourly_data WHERE ItemName='酸雨'") #ORDER BY SiteId
        r = c.fetchall()
        conn.close()
    except socket.error as serror:
        if conn is not None:
            conn.close()
    return render(request, "display.html", locals())

def rain_cond(request):
    conn = None
    try:
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "ph_rain")
        c = conn.cursor()
        conn.set_character_set('utf8')
        c.execute("SELECT * FROM hourly_data WHERE ItemName='導電度'") #ORDER BY SiteId
        r = c.fetchall()
        conn.close()
    except socket.error as serror:
        if conn is not None:
            conn.close()
    return render(request, "display.html", locals())
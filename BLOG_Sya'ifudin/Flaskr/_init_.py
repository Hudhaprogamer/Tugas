# import aplikasi flask untuk di pakai di web kita
from flask import Flask


#mengatur nama aplikasi 
app = Flask(_name_)


#mengatur URI (universal resource indentifier),dan apa yang di tampilkan jika URI tersebut di akses
@app.route('/')# ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi fungsi hello()
def hello():#function dengan nama hello
  return 'Hello, World!'
  
#mengatur URI ke http://127.0.0.1.5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URL http://127.0.0.1.5000/login
@app.route("/login")
def login():
  return 'halaman login'
  
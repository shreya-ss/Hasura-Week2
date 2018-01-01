from src import app


from flask import Flask, render_template, make_response, request, redirect
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World-Shreya'



@app.route('/authors')
def authors():
	url1 = 'https://jsonplaceholder.typicode.com/users'
	url2 = 'https://jsonplaceholder.typicode.com/posts'
	r1 = requests.get(url1)
	r2 = requests.get(url2)
	data1 = r1.json()
	data2 = r2.json()
	return render_template('authors.html', data1=data1, data2=data2)


@app.route('/setcookie')
def set_cookie():
	resp=make_response("Cookies are set!")
	resp.set_cookie("name","Shreya")
	resp.set_cookie("age","20")
	return resp


@app.route("/getcookies")
def get_cookies():
	name=request.cookies.get('name')
	age=request.cookies.get('age')
	return "Name: "+name+" "+" Age: "+age


@app.route('/robots.txt')
def deny_request():
	return redirect('http://httpbin.org/deny')



@app.route('/html')
def send_html():
	return render_template('home.html')



@app.route('/input')
def input():
	return render_template('input.html')


@app.route('/welcome', methods=['POST'])
def welcome():
	if request.method == 'POST':
		result = request.form
		name=result.get('nm')
		print(name)
	return render_template("welcome.html",result = result)

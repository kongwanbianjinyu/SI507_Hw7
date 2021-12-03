from flask import Flask, render_template, request
import secrets
import json
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<nm>')
def show_name(nm):
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(secrets.api_key)
    requestHeaders = {
        "Accept": "application/json"
    }

    response = requests.get(requestUrl, headers=requestHeaders).json()

    # print(response)
    result_list = [result["title"] for result in response["results"]]

    result_list = enumerate(result_list[:5])
    return render_template('name.html',name = nm,result_list = result_list)

@app.route('/links/<nm>')
def show_name_links(nm):
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(secrets.api_key)
    requestHeaders = {
        "Accept": "application/json"
    }

    response = requests.get(requestUrl, headers=requestHeaders).json()

    # print(response)
    title_list = [result["title"] for result in response["results"]]
    url_list = [result["url"] for result in response["results"]]

    title_list = enumerate(title_list[:5])
    url_list = url_list[:5]
    return render_template('name_url.html',name = nm,title_list = title_list, url_list = url_list)


@app.route('/images/<nm>')
def show_image_links(nm):
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}".format(secrets.api_key)
    requestHeaders = {
        "Accept": "application/json"
    }

    response = requests.get(requestUrl, headers=requestHeaders).json()

    # print(response)
    title_list = [result["title"] for result in response["results"]]
    url_list = [result["url"] for result in response["results"]]
    image_list = [result["multimedia"][0]["url"] for result in response["results"]]

    title_list = enumerate(title_list[:5])
    url_list = url_list[:5]
    image_list = image_list[:5]
    print(image_list)
    return render_template('image.html',name = nm,title_list = title_list, url_list = url_list, image_list = image_list)


if __name__ == '__main__':
    app.run(debug=True)

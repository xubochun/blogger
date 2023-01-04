# My Google Blogger 
This is the example that I use to write my Blogger articles.

please feel free to check [here](https://jacksonxu-notes.blogspot.com/)!

## 1. Selenium - Web crawler
blogger: https://jacksonxu-notes.blogspot.com/2022/12/seleium-yahoo.html

### How to use:
1. Install requirements txt file with `pip3 install -r requirements.txt`
2. Run python script `python3 example_1_yahoo_stock.py`

## 2. Docker 
blogger: https://jacksonxu-notes.blogspot.com/2022/12/blog-post.html

### How to use:
1. Create a Dockerfile like this:
```
FROM python:3.12-rc-alpine
MAINTAINER Jackson Xu
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
```
2. Build a docker image via `docker build -t python-docker . --no-cache`
3. Start and run a container in docker via `docker run --name flask-app -p 5000:5000 -d python-docker`

## 3. Selenium - UI testing
blogger: https://jacksonxu-notes.blogspot.com/2023/01/python-selenium-pytest-ui-google.html

### How to use:
1. Install python package
```
pip3 install webdriver-manager
pip3 install pytest
```
2. Run pytest
```
cd selemium_test_ui
python3 -m pytest
```

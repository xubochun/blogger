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

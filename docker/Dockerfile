FROM python:3.12-rc-alpine
MAINTAINER Jackson Xu
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
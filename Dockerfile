FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
# 安装Python依赖
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple --trusted-host=pypi.douban.com
COPY . .
# scraping-numbers

## dockerは事前にインストールするが必要ある
- docker for Windows or docker for Mac

## docker pullでpythonイメージを取得してくる 
```
docker pull python
```

## docker runでコンテナ立ち上げて中に入る
```
# -v でマウントする場所は好きな場所を指定する
docker run -it -v hoge:/tmp python:latest /bin/bash

# get_numbers.pyで必要なライブラリをインストール
pip install beautifulsoup4
pip install html5lib

# get_numbers.pyを実行
python get_numbers3.py
python get_numbers4.py
```

## 不要になったコンテナ、イメージは削除する
```
docker ps -a
docker rm hoge

docker images
docker rmi hoge
```


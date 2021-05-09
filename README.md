# sphinxのサンプル

起動

```bash
docker-compose build
docker-compose up -d
```

sphinxの設定

```bash
docker-compose exec mypython sphinx-quickstart docs
```

sphinxのconfigファイルを編集

```bash
docker-compose exec -T mypython patch -p0 < conf.py.diff 
```

各モジュールのsphinxのrstファイルを生成

```bash
docker-compose exec mypython sphinx-apidoc -f -o docs/source ./
```

sphinxのhtmlドキュメントを作成

```bash
docker-compose exec mypython sphinx-build -b html docs/source docs/build/html/
```





停止

```bash
docker-compose down
```

または

```bash
docker-compose down --rmi all --volumes --remove-orphans
```

# duelchik

## Как запустить сервак

### Через докер
```bash
cd server
docker build -t zhc/duelchik .
docker run --rm -p8080:8080 zhc/duelchik
```

### Через путон
```bash
cd server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Дока API
Открыть ссылку http://localhost:8080/docs

## Как запустить frontend

## Через докер
```bash
cd frontend
docker build -t zhc/duelchik/frontend .
docker run --rm -p8888:80 zhc/duelchik/frontend
```

## Через жс
```bash
cd frontend
npm install
npm run serve
```
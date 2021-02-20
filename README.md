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

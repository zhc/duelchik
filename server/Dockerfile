FROM python:3.8.5
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD ./duelchik /app/duelchik
CMD ["uvicorn", "duelchik.server:app", "--host", "0.0.0.0", "--port", "8080"]

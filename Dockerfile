From python:3.9

WORKDIR /app

Copy . .

Run pip install Flask pymysql

Expose 5200

CMD ["python", "flask3.py"]



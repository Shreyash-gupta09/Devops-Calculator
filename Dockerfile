FROM python

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest

CMD ["python3", "calculator.py"]

FROM python:3.11

WORKDIR /bot

COPY . /bot

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "bot.py"]

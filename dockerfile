FROM python:3.8-alpine
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN mkdir /code
COPY main.py /code.
CMD ["python", "/code/btc_scraper.py"]


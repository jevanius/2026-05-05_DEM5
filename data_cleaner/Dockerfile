FROM python:3.12-slim
WORKDIR /cleaner
COPY . .
RUN pip install --no-cache-dir pandas
ENTRYPOINT ["python","data_cleaning.py"]
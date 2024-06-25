FROM python:3.8-slim

WORKDIR /home/jovyan

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter-lab", "--ip=0.0.0.0", "--allow-root"]

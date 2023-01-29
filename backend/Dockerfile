FROM python:3.10.3-bullseye
WORKDIR /app
COPY ./ /app
RUN pip3 install -r requirements.txt
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

CMD ["python3", "main.py"]
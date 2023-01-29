FROM python:3.10.3-bullseye
WORKDIR /app
COPY ./ /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

CMD ["python3", "main.py"]
# Detectron2 Simple User Interface
This project is a web interface to Detectron2
### Run (developer config)
Open localhost:80 in your browser 
```sh
docker-compose -f docker-compose-dev.yml up
python main.py
```
### Run (simple prod config)
Open localhost:8080 in your browser
```sh
docker build -t frontend-detectron2 ./frontend/ 
docker build -t backend-detectron2 ./backend/ 
docker-compose up
```
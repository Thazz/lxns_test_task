# Estates Scraper

This repository contains an application that:
- scrapes information about apartment offers on the real estate portal [sreality.cz](https://www.sreality.cz/en) using [Scrapy](https://scrapy.org/). By using API request it gets information about 500 appartments in all available countries. It is scheduled to run every minute.
- Data is stored in [PostgreSQL](https://www.postgresql.org/) database.
- Simple [Flask](https://flask.palletsprojects.com/) web app is served on [localhost](http://127.0.0.1:8080) to display pictures and information about scraped apartments.

## Installation

To use this application, [Docker](https://docs.docker.com/engine/install/) installation is required.
Clone this repository to your local machine
```
git clone https://github.com/Thazz/lxns_test_task.git
```
Move to the root project folder and start the application using docker-compose
```
docker-compose up -d
```
You can check the status of the started containers with 
```
docker-compose ps
```
To stop the application use 
```
docker-compose down
```
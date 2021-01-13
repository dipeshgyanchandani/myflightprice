# Flight Price Prediction
## Table of Content
* [Overview](#Overview)
* [Demo](#Demo)
* [Installation](#Installation)
* [Directory Tree](#Directory-Tree)
* [Technologies Used](#Technology-Used)
* [Bugs and Feature Request](#Bugs-and-Feature-Request)
* [Future Scope](#Future-Scope)

## Overview
[MyFlightPrice](https://myflightprice.herokuapp.com/) is a Flask web app which can predict your flight price based on the required information. Price may vary based on Source & Destination cities, Stops, Departure and Arrival Date & Time. Random Forest Regressor is implemented to predict the price of a flight.

## Demo
Link: https://myflightprice.herokuapp.com/
or Click [Here](https://myflightprice.herokuapp.com/)

![alt text](https://github.com/dipeshgyanchandani/myproject/blob/master/Screenshot%202021-01-13%20at%202.47.16%20AM.png "Logo Title Text 1")

![alt text](https://github.com/dipeshgyanchandani/myproject/blob/master/Screenshot%202021-01-13%20at%202.42.41%20AM.png "Logo Title Text 2")

## Installation
To install the required packages and libraries, run this command in the project directory after cloning the repository:

```pip install -r requirements.txt```

## Directory Tree
```
├── static 
│   ├── main.css
├── template
│   ├── about.html
│   ├── home.html
│   ├── layout.html
│   ├── predicted.html
├── Procfile
├── README.md
├── app.py
├── flight_price.ipynb
├── flight_rf.pkl
├── requirements.txt
```

## Technologies Used
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Gunicorn](https://gunicorn.org/)
* [sci-kit learn](https://scikit-learn.org/stable/)

## Bugs and Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/dipeshgyanchandani/myflightprice/issues) by including your search query and the expected result

## Future Scope
* Use Multiple Algorithms
* Front - End

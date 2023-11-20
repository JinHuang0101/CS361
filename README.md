# CS361
Communication Contract 
This project is a microservice that I wrote for my partner's weather app with a Command Line Interface. 

A. Request. My microservice will make an HTTP request to the REST API on weatherapi.com. 
Following is an example of how to request data from the microservice: My partner's main program will prompt the user to input a location in, for example, 'Portland'. The string 'Portland' will be passed as a string parameter in my microservice which will make an HTTP request to the weather API
using the current weather endpoint to retrieve the current weather info of 'Portland'.

B. Receive. My microservice will retrieve the current weather data of Portland from the weather API in a json file. The microservice will save the returned json file as current_weather_data and 
return it to my partner's main program. The main program will access current_weather_data and interpret/display some of the data to users on the Command Line Interface. 

C. UML sequence diagram

<img width="1437" alt="Screenshot 2023-11-20 at 11 27 48 AM" src="https://github.com/JinHuang0101/CS361/assets/54080607/e9432217-093d-4d9a-9bbb-cd6e09c70845">

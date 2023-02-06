# README

## Challenge for Voxy - Back-end Engineer Position

## Building and Running Docker Container in Windows
1. Install Docker for Windows from https://www.docker.com/products/docker-desktop
2. Open Command Prompt or PowerShell and navigate to the project directory
3. Build the Docker image using the command: 

```cmd
    docker build -t <image-name> .
```

4. Run the Docker container using the command: 
```cmd
    docker run -p 5000:5000 <image-name>
```

## Building and Running Docker Container in Linux
1. Install Docker for Linux from https://www.docker.com/products/docker-desktop
2. Open Terminal and navigate to the project directory
3. Build the Docker image using the command: 
```cmd
    docker build -t <image-name> .
```
4. Run the Docker container using the command: 
```cmd
    docker run -p 5000:5000 <image-name>
```

## Running Flask Application using venv
1. Install Python3 and venv from https://www.python.org/
2. Open Command Prompt or Terminal and navigate to the project directory
3. Create a virtual environment using the command: 
```cmd
    python3 -m venv <env-name>
```
4. Activate the virtual environment using the command: 
on Linux
```cmd
    source <env-name>/bin/activate
``` 
on Windows
```cmd
    <env-name>\Scripts\activate
```
5. Install the required packages using the command: 
```cmd
    pip install -r requirements.txt
```
6. Set the environment variables using the command: 
on Linux
```cmd
    export FLASK_APP=app.py
```
on Windows

```cmd
    set FLASK_APP=app.py
```
7. Run the application using the command: 
```cmd
    flask run
```

## Testing
1. To test the application run:
```cmd
    pytest
```


## Application Behavior
The application is a simple Flask application that displays a form containing a text box to enter a body of text. When the form is submitted with some text, the result will display the number of words in the text box. If the form is submitted with an empty text, a form error will be displayed telling the user that some text input is required.

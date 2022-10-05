# FakeNameGenerator

Generates fake profile names that can be used when needing to simulate realistic usage of an app.
I needed this to simulate somewhat realistic chat activity.

The tool contains two apps: 

 * a command-line tool
 * a Flask-based webapp

The tool generates the fake profile names by selecting random names from a pool of available first, middle and last names.

See the text around data files below.

## Command-line usage

Generate a fake name by running:

    $ ./cli.py

The output will be something like this:


    Full name: John Smith
    Username: jsmith53

## Web App

As a prerequisite, you will need to build and activate a virtual environment. 
This is done using the Makefile:

    $ make venv

When the venv is built, activate it by running:

    $ . venv/bin/activate

Now start the web application by running:

    (venv) ~/FakeNameGenerator $ python app.py
     * Serving Flask app 'app'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit


Now point a browser to one of the following addresses:

 * <http://127.0.0.1:5000> : this will give you a single user.
 * <http://127.0.0.1:5000/many> : this will give you many profiles



## Data files

For this to work, you need three data files: 

    first_names.txt
    last_names.txt
    middle_names.txt

The names are self explanatory.
The files should respectively contain a list of first names, last names and middle names. 
One name per line.

You will need to get the data files somewhere else or make your own.


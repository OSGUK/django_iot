# Samsung Open Source Group Web Portal
This is a web portal for Samsung Open Source Group. It demonstrates some clever IoT technology and eCommerce platform capability with QR code generation and tracking built out the box. It's used to allow IoT devices to register themselves using HTTP Rest interface.
To use a specific device local to the user - the user access's the registration server to discover it. The user is then redirected to this device.

The platofm is based on python django. It uses all the common django libs to develop a CMS type portal.
Added to this it also uses QR-Codes for generating QR code enabled sku's. 
The message bus (AMQP) is Celery. This is used for queuing messages to and from the client/server interfaces so that a QR code 
can dynamically route to a URI.

## Software You Need
You will need to install or have on your system:
python3, virtualenv, virtualenvwrapper, sqlite

## Installation
Steps to install locally.
* Create a virtual environment
  /> mkvirtualenve --python=/usr/bin/python3 <name of your project>

* Activate the virtual environemnet
  /> workon <name of your project>
  
* Clone the github repo of this project
  /> git clone https://github.com/OSGUK/Django_IOT.git

## First Time Setup
Steps to setup your django web server before running. You must first activte your virtual environment before doing this.
See 'Installation' for details.
* First get all the python packages you need to run your server. This is stored in the requirements.txt file for the project
  /> pip install -r requirements.txt
  
* Upon starting the django web server will try and start as a production server. You need to change the settings.py file and add your computer name to the list of development machines. Hence open settings.py and update line 18 'DEVELOPER_MACHINES' to have your local machine ID e.g.

DEVELOPER_MACHINES = ['Zenbook-UX32A', 'kieran', 'dilmac-VB', 'dilmac', 'my-mac-machine', 'my-linux-machine', 'nb-909' ]

Save this. Now when the server runs it will use an SQLite DB. You can configure the server to use any DB you like, but this is the fastest way to get it up and running.

* Migrate Your Tables. Django uses an ORM, so we need to migrate new Django objets to your SQL database.
  /> python manage.py migrate
  
## Start Your Server
Now run the django server in a development mode way - i.e. no requirement for nginx, apache, gunicorn etc.. This is not a production system!

  /> python manage.py runserver
  
  Output.....
  January 26, 2018 - 11:52:41
  Django version 1.10.5, using settings 'config.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C
  
  
Now navigate to your localhost interface on port 8000 on your browser.





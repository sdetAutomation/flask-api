```                                                                      
#             .___      __     _____          __                         __  .__               
#    ______ __| _/_____/  |_  /  _  \  __ ___/  |_  ____   _____ _____ _/  |_|__| ____   ____  
#   /  ___// __ |/ __ \   __\/  /_\  \|  |  \   __\/  _ \ /     \\__  \\   __\  |/  _ \ /    \ 
#   \___ \/ /_/ \  ___/|  | /    |    \  |  /|  | (  <_> )  Y Y  \/ __ \|  | |  (  <_> )   |  \
#  /____  >____ |\___  >__| \____|__  /____/ |__|  \____/|__|_|  (____  /__| |__|\____/|___|  /
#       \/     \/    \/             \/                         \/     \/                    \/ 
```
# flask-api
sample project building an api using flask and python


Introduction
------------
This project is made for anyone who is looking for an example of how to create a rest endpoint using Python and Flask.

This service calls a local sqlite database. Please see databases directory for more details. 

This projet was written using PyCharm Community Edition.   


Installing Project Dependencies
-----
[This project uses Pipenv for virtual environment management.](https://pipenv.readthedocs.io)

If you are on MacOS you can install the dependency using homebrew:

`brew install pipenv`


Next run the following command to install the dependencies on your local computer:

`pipenv install`


Running the application
-----
After you have performed all the dependency installations from above, you can run the following command on your terminal
to start this app.

From the root of this project enter the following terminal command:

`pipenv run python app.py`


Or you can also start the application using PyCharm.  



Project Database
-----
This project uses local sqlite for a repository.  


Swagger
-----
This project contains a swagger ui.  (For more information regarding swagger)[https://swagger.io/]

To view this api's swagger ui, run this application, then navigate to [http://localhost:5000/ui/]

You can test out this api entirely from the swagger ui page. 


Rest Api 
-----

GET - getAll : localhost:5000/users/v1/

GET - getByUsername: http://localhost:5000/users/v1/darth

PUT - updateUserEmail: http://localhost:5000/users/v1/darth + include a json body with new email.

DELETE - deleteUsername: http://localhost:5000/users/v1/darth



TDD - Integration Tests
-----
This api is fully tested with Unit Tests and Integration tests.  Please see tests directory for examples.

    
Flask Project
-----
This project is a Flask project. (For more information)[http://flask.pocoo.org/]
    
   
Continuous Integration(CI)
------------
A web hook has been setup with Travis CI for all Push and Pull Requests.
 

Questions / Contact / Contribute
------------
Feel free to fork this repo, add to it, and create a pull request if you like to contribute.  

If you have any questions, you can contact me via email: `sdet.testautomation@gmail.com`
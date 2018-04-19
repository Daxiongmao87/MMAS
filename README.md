
# Movie Meta-Analytics and Statistics (MMAS)

A webpage that analyzes interesting and most probably useless info from Rotten Tomatoes and IMDB.

mmas.py is the main application script, this is where most of the code will be.

**INSTRUCTIONS**
1. Install python 2.7 (https://www.python.org/)
2. Open command promprt (or terminal) and install virtualenv from pip: 'python -m pip install virtualenv'
3. Navigate to your project folder and create a virtual environment: 'virtualenv'
4. Next you'll want to be in the python virtual environment, so navigate to venv/Scripts/activate.bat (or if iin linux, ./venv/Scripts/activate
5. Type 'python -m pip install -r requirements.txt in the root folder
6. You now have all the requirements to launch the webserver, and would probably be best working on the project at this step.
	
	
**TO RUN**
1. While in the virtual environment, type 'set FLASK_APP=mmas' (or if in linux: 'export FLASK_APP=mmas')
2. To run the server at the root directory, you should be able to type 'flask run'

**TODO**

 - Webserver  :heavy_check_mark:
 - Database schema once we figured out how we will be organizing the data :construction:
 - Backend calculations for desired analytics and statistics :construction:
 - Webpage to display analytics and statistics :construction:

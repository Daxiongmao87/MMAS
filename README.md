
# Sabermetrics Major League Basebball Analysis
(Formerly) Movie Meta-Analytics and Statistics (MMAS)

mmas.py is the main application script, this is where most of the code will be.

**INSTRUCTIONS**
1. Install python 2.7 (https://www.python.org/).  After installation on Windows, you may need to set your environment variables.  To do this:
	a. type "Environment Variables" in your search bar and select "Edit environment variables for your account" (Windows 10)
	b. Select the variable "Path" and click "Edit"
	c. Click "New" and add the path to your python folder (default: "C:\Python27\")
	d. Click on "New" again, and add the path to your pyhon scripts folder (default: "C:\Python27\Scripts\")
	e. Then click "OK" and "OK" to apply your changes and exit out.
2. Open command prompt (or terminal) and install virtualenv from pip: 'python -m pip install virtualenv'
3. Navigate to your project folder and create a virtual environment: 'virtualenv'
4. Next you'll want to be in the python virtual environment, so navigate to venv/Scripts/activate.bat (or if iin linux, ./venv/Scripts/activate
5. In the root directory, type 'pip install --editable .'
6. You now have all the requirements to launch the webserver, and would probably be best working on the project at this step.
	
	
**TO RUN**
1. While in the virtual environment, type 'set FLASK_APP=mmas' (or if in linux: 'export FLASK_APP=mmas')
2. To run the server at the root directory, you should be able to type 'flask run'

**TODO**

 - Webserver  :heavy_check_mark:
 - Database schema once we figured out how we will be organizing the data :heavy_check_mark:
 - Backend calculations for desired analytics and statistics :heavy_check_mark:
 - Webpage to display analytics and statistics :heavy_check_mark:

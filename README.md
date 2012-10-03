------------------------------------ Setup -------------------------------------------

Should run on a virtual environment to make sure it works the same on everyones machines
To install virtualenv:

pip install virtualenv

To set up virtualenv and install necessary components:

virtualenv-2.7 env
source ./env/bin/activate
pip install django
pip install south

You can stop using virtualenv by using the command:

deactivate

-------------------------------------------------------------------------------------------

pip install pil
pip install django_facebook

------------ FOR FACEBOOK -------------

sudo nano /private/etc/hosts
     * In that file add the line "127.0.0.1       hackbyrd.com" at the bottom
dscacheutil -flushcache

/* Now navigate to "http://hackbyrd.com:8000/facebook/connect/" to ensure that it worked */


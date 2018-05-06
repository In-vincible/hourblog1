# hOUR BLOG 

* Hosted on: http://devohack.tk/
* Development server on heroku: https://techwana.herokuapp.com/
* Runtime: Python 3.6
## How to install:
```
git clone https://github.com/In-vincible/hourblog1/
```
### Create virtualenv using venv(new for python 3.6):
```
python3.6 -m venv hourblog
cd hourblog/bin
source activate
```

## or 

### Create virtualenv using virtualenvwrapper
```
mkvirtualenv hourblog --python=python3.6
workon hourblog 
```

### Enter Blog directory after activating the venv as described above:
```
pip install -r requirements.txt
pip freeze #to check the installed modules
```

### Migrate and Run:
```
python manage.py migrate
python manage.py runserver
```

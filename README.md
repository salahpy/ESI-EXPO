# ESI-expo :

##  Running The API

Clone the Repo then :


```python
python3 -m venv env
source env/bin/activate  
# On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb 

#Run the server 

python manage.py runserver
```
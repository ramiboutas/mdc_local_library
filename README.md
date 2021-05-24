# mdc_local_library

This is just a tutorial from the [MDN](https://developer.mozilla.org/)


[Django Tutorial: The Local Library website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)


#### 1. Create a virtual enviorement 

` python3 -m venv venv `

#### 2. Activate it (linux)
` source venv/bin/activate `

#### 3. Install the requirements once inside the venv

`pip install -r requirements.txt`

#### 4. make migrations & migrate

` python manage.py makemigrations`

` python manage.py migrate`

#### 5. Run the server


` python manage.py runserver`

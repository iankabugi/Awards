# Awards
This an awards web app
## Getting Started

git clone : https://github.com/iankabugi/Awards.git

### Prerequisites

astroid==2.1.0
autopep8==1.4.3
confusable-homoglyphs==3.2.0
dj-database-url==0.5.0
Django==1.11
django-bootstrap3==11.0.0
django-heroku==0.3.1
django-registration==2.4.1
django-tinymce==2.8.0
gunicorn==19.9.0
isort==4.3.7
lazy-object-proxy==1.3.1
mccabe==0.6.1
mypy==0.670
mypy-extensions==0.4.1
Pillow==5.4.1
psycopg2==2.7.7
psycopg2-binary==2.7.7
pycodestyle==2.5.0
pylint==2.2.2
pyperclip==1.7.0
python-decouple==3.1
pytz==2018.9
six==1.12.0
typed-ast==1.3.1
whitenoise==3.3.1
wrapt==1.11.1
yapf==0.26.0


### Installing

After cloneing,run this command:

```
pip install -r requirements.txt
```


## Running the tests

run this in your terminal: python manage.py tests

### Break down into end to end tests

The test are doen to affirm app functionality
### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Create User | Enter credenetialss | they are saved in the background and redirected to the landing page |
| Sign In | Click on the Sign In and enter your credentials | Loads the landing page. |


## Deployment

The app was deployed to heroku:

https://bugiawards.herokuapp.com/

## Built With

* python-django
* git
* postgresql

## Contributing

* **Ian Kabugi**

## Versioning

I used git versioning ,[instaclone](https://github.com/iankabugi/Awards/tags)

## Authors

* **Ian Kabugi** - *Initial work* - [iankabugi](https://github.com/iankabugi/awards)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
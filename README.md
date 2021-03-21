# newsfeed
personalized newsfeed portal


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ejaj/newsfeed.git
$ cd newsfeed
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
To get initial data browse `http://127.0.0.1:8000/initial_news_api`

## Dependencies

```sh
- Database: PostgreSQL
- Redis as a Message Broker
```
Change the database namd name and password from settings.py

### Phase 1 location
```sh
- newsfeed/newsupdateApi
```
### Phase 2 location
```sh
- newsfeed/accounts
```
### Phase 3 location
```sh
- newsfeed/news
```
### Phase 4 location
```sh
- newsfeed/accounts
```
### Phase 5 location
```sh
- newsfeed/accounts
```

### Run Task scheduler 
```sh
Run these commad in separate terminal. 
$ celery -A newsfeed worker -l info
$ celery -A newsfeed beat -l info

```
## API Token
User token generated while user registration/sign up. To get this token. Open postman and put username and password below url. it is POST request
```sh
http://127.0.0.1:8000/api/v1/get_api_token
```
To get personalized newsfeed for a specific user curl this url with token
```sh
$ curl http://127.0.0.1:8000/api/v1/user_news_feed/1 -H 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'
```

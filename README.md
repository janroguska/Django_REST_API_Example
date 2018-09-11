# Django_REST_API_Example

## Setup
* Ensure Python is installed globally.
* ```bash
  $ pip install virtualenv
  ```
* cd into the 'src' directory
* ```bash
  $ virtualenv --python=python3 env
  ```
* ```bash
  $ source env/bin/activate
  ```
* ```bash
  $ pip install -r requirements.txt
  ```
* ```bash
  $ python3 manage.py makemigrations user_auth users_api
  ```
* ```bash
  $ python3 manage.py migrate
  ```
## Running the Server
* ```bash
  $ python3 manage.py runserver
  ```
* setup a user at:
  ```
  http://http://127.0.0.1:8000/api/v1/rest-auth/registration/
  ```
* access the database entries at:
  ```
  http://http://127.0.0.1:8000/api/v1/users/
  ```
  ```
  http://http://127.0.0.1:8000/api/v1/users/[id]
  ```
  ## Methods:
  `GET`|`PUT`|`POST`|DELETE`
  ## Parameters:
  *uid(required): Positive integer from 0-999
  *name(required): String
  *age: Positive integer from 0-999
  *image: JPEG file. limit: 150kb
  
  


# Task Management App

Objective: To design and implement a simple Task Management Web Application using Django and React.

Frontend Link : https://github.com/ProgrammingWithSid/task-management-frontend

## Technologies Used
Framework : Django
REST API

## Languages Used
Python

# Build Setup

git clone https://github.com/ProgrammingWithSid/task-management-backend.git

cd auth/
# Install Dependencies
pip install -r requirements.txt
# Server at localhost:8000
python manage.py createsuperuser       
python manage.py runserver

API Endpoints

* GET /tasks: Fetch all tasks.
* GET /tasks/:id: Fetch a single task by ID.
* POST /tasks: Add a new task.
* PUT /tasks/:id: Update a task by ID.
* DELETE /tasks/:id: Delete a task by ID.

## API References

#### Get all items

Fetch all tasks.

```http
  GET /tasks
```

Header : 
```
  Authorization: JWT <token>
```


#### Get item

```http
  GET /tasks/${uuid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uuid`      | `uuid` | **Required**. Id of item to fetch |

**Header :** 
```
  Authorization: JWT <token>
```

#### Add a new task

```http
  POST /tasks/${uuid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uuid`      | `uuid` | **Required**. Id of item to fetch |

**Header :** 
```
  Authorization: JWT <token>
```

**Body :**
```
{
    "taskName": "Testing Add View",
    "description": "Now testing add view"
}
```
    


#### Update a task

```http
  PUT /tasks/${uuid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uuid`      | `uuid` | **Required**. |


**Header :** 
```
  Authorization: JWT <token>
```

**Body :**
```
{
    "taskName": "Testing Add View",
    "description": "Now testing add view"
}
```


#### Delete a task

```http
  DELETE /tasks/${uuid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uuid`      | `uuid` | **Required**. |

**Header :** 
```
  Authorization: JWT <token>
```

#### Create a user

```http
  POST /auth/users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**.  |
| `name`      | `string` | **Required**.  |
| `password`      | `string` | **Required**. |
| `re_password`      | `string` | **Required**.  |


**Body :**
```
{
    "email": "",
    "name": "",
    "password" : "",
    "re_password" : ""
}
```

#### Login a user


```http
  POST /auth/jwt/create/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. |
| `password`      | `string` | **Required**. |


**Body:** 
```
{
    "email":"satender@gmail.com",
    "password":"Sid@1234"
}
```

#### Generate refresh token

```http
  POST /auth/jwt/refresh/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `refresh`      | `string` | **Required**. |

```
{
    "refresh":"<token_value>"
}
```


# Connect @
* LinkedIn: https://www.linkedin.com/in/satender-kumar-600bb3179/
* Leetcode: https://leetcode.com/satenderk8700
* Email: satenderk8700@gmail.com   

# Personal
Name: Satender Kumar  

# Gratitude
Thank You

# cosmoquizz-api

API built with python and FastAPI library for the cosmoquizz app. Connects with Firebase realtime database storage to store and manipulate the data required for the cosmoquizz.

 
### Deployed Website
https://cosmoquizz-api.herokuapp.com/
API Documentation (Swagger UI): https://cosmoquizz-api.herokuapp.com/docs

Known Issues:
1. Since Heroku set a limit on free access, pages that require API connections will load more slowly. Please wait patiently.

## Endpoints

### GET /students
#### Description:
Get all data of all students

#### Sample Request Body:
None

#### Sample Response Body:
{
  "students": [
    {
      "birthday": "01/01/1999",
      "email": "bobbob@gmail.com",
      "emergencyContact": "111-111-1111",
      "firstName": "bob",
      "grade": 10,
      "lastName": "bob",
      "school": "Hunter",
      "username": "bobbob"
    },
    {
      "birthday": "2010-05-31",
      "email": "joejoe@gmail.com",
      "emergencyContact": "999-999-9999",
      "firstName": "joe",
      "grade": 5,
      "lastName": "joe",
      "school": "Baruch College",
      "username": "joejoe"
    }
  ]
}

### GET /students/{username}
#### Description:
Get data of student with corresponding username

#### Sample Request Body:
None

#### Sample Response Body:
{
  "data": {
    "birthday": "01/01/1999",
    "email": "bobbob@gmail.com",
    "emergencyContact": "111-111-1111",
    "firstName": "bob",
    "grade": 10,
    "lastName": "bob",
    "school": "Hunter",
    "username": "bobbob"
  }
}

### POST /students
#### Description:
Create new student

#### Sample Request Body:
{
  "birthday": "string",
  "emergencyContact": "string",
  "firstName": "string",
  "grade": 0,
  "lastName": "string",
  "school": "string",
  "username": "string",
  "email": "string"
}

#### Sample Response Body:
If username doesn't exist
{
  "username": "inputted_username"
}

If username does exist
{
  "message": "username already exists"
}


### PUT /students/{username}
#### Description:
Update existing student's info

#### Sample Request Body:
{
  "birthday": "string",
  "emergencyContact": "string",
  "firstName": "string",
  "grade": 0,
  "lastName": "string",
  "school": "string",
  "username": "string",
  "email": "string"
}

#### Sample Response Body:
If username doesn't exist
{
  "message": "username not found"
}

If username does exist (returns inputted data)
{
  "birthday": "string",
  "school": "string",
  "email": "string",
  "username": "string",
  "emergencyContact": "string",
  "lastName": "string",
  "firstName": "string",
  "grade": 0
}

### DELETE /students/{username}
#### Description:
Delete a student from the database

#### Sample Request Body:
None

#### Sample Response Body:
If username doesn't exist
{
  "message": "username not found"
}

If username does exist 
{
  "message": "successfully removed"
}



### GET /teachers
### GET /teachers/{username}
### POST /teachers
### PUT /teachers/{username}
### DELETE /teachers/{username}



### GET /teachers/{username}/students
### PUT /teachers/{teacher_username}/students/{student_username}
### DELETE /teachers/{teacher_username}/students/{student_username}
### GET /students/{username}/teachers



### GET /tests
### GET /tests/{testName}
### GET /tests/submissions/{testName}
### POST /tests/{createdBy}
### DELETE /tests/{testName}

### GET /submissions/{username}
### GET /submissions/{username}/{testName}
### POST /submissions/{username}
### DELETE /submissions/{username}/{testName}
### GET /submissions/all/{username}

### GET /grades/{username}
### POST /grades/{username}/{testName}
### DELETE /grades/{username}/{testName}






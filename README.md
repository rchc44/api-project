# cosmoquizz-api

API built with python and FastAPI library for the cosmoquizz app. Connects with Firebase realtime database storage to store and manipulate the data required for the cosmoquizz.

 
### Deployed Website
https://cosmoquizz-api.herokuapp.com/
API Documentation (Swagger UI): https://cosmoquizz-api.herokuapp.com/docs

### Endpoints

#### GET /students
Description:
Get all data of student with corresponding studentId

Sample Request Body:
None

Sample Response Body:
Student Found

#### GET /students/{username}
Description:
Get all data of student with corresponding studentId

Sample Request Body:
None

Sample Response Body:
Student Found


#### POST /students
#### PUT /students/{username}
##### DELETE /students/{username}

#### GET /teachers
#### GET /teachers/{username}
#### POST /teachers
#### PUT /teachers/{username}
#### DELETE /teachers/{username}

#### GET /teachers/{username}/students
#### PUT /teachers/{teacher_username}/students/{student_username}
#### DELETE /teachers/{teacher_username}/students/{student_username}
#### GET /students/{username}/teachers



#### GET /tests
#### GET /tests/{testName}
#### GET /tests/submissions/{testName}
#### POST /tests/{createdBy}
#### DELETE /tests/{testName}

#### GET /submissions/{username}
#### GET /submissions/{username}/{testName}
#### POST /submissions/{username}
#### DELETE /submissions/{username}/{testName}
#### GET /submissions/all/{username}

#### GET /grades/{username}
#### POST /grades/{username}/{testName}
#### DELETE /grades/{username}/{testName}




Known Issues:
1. Since Heroku set a limit on free access, pages that require API connections will load more slowly. Please wait patiently.

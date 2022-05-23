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
  
  "students": 
  
[
    
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
  
  "data": 
  
  {
    
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
	"emergencyContact": "string",
	"firstName": "string",
	"grade": 0,
	"lastName": "string",
	"school": "string",
	"username": "string",
	"email": "string"

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

#### Description:
Get all data of all teachers

#### Sample Request Body:
None

#### Sample Response Body:

{

  "teachers": [
  
    {
      "bio": "string",
      "birthday": "string",
      "email": "string",
      "firstName": "string",
      "lastName": "string",
      "phone": "string",
      "school": "string",
      "students": [
        "joejoe"
      ],
      "subject": "string",
      "username": "string"
    },
    {
      "bio": "Hi, I am pro professor",
      "birthday": "4/12/1987",
      "email": "proprof@gmail.com",
      "firstName": "prof",
      "lastName": "pro",
      "phone": "123-432-3254",
      "school": "Hunter",
      "subject": "CS",
      "username": "proprof",
      "students": []
    }
	
  ]
  
}

### GET /teachers/{username}

#### Description:
Get data of teacher with corresponding username

#### Sample Request Body:
None

#### Sample Response Body:

{

  "data": {
  
    "bio": "Hi, I am pro professor",
    "birthday": "4/12/1987",
    "email": "proprof@gmail.com",
    "firstName": "prof",
    "lastName": "pro",
    "phone": "123-432-3254",
    "school": "Hunter",
    "subject": "CS",
    "username": "proprof",
    "students": []
	
  }
  
}

### POST /teachers


#### Description:
Create new teacher

#### Sample Request Body:

{

	"bio": "string",
	"birthday": "string",
	"firstName": "string",
	"lastName": "string",
	"phone": "string",
	"subject": "string",
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


### PUT /teachers/{username

#### Description:
Update existing teacher's info

#### Sample Request Body:
{

	"bio": "string",
	"birthday": "string",
	"firstName": "string",
	"lastName": "string",
	"phone": "string",
	"subject": "string",
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

	"bio": "string",
	"birthday": "string",
	"firstName": "string",
	"lastName": "string",
	"phone": "string",
	"subject": "string",
	"school": "string",
	"username": "string",
	"email": "string"

}




### DELETE /teachers/{username}
#### Description:
Delete a teacher from the database

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





### GET /teachers/{username}/students
#### Description:
Get all the students in a teacher's class

#### Sample Request Body:
None

#### Sample Response Body:

If username doesn't exist
{
  "message": "teacher's username not found"
}

If username does exist 
{
  
  "data": [  ]
  
}


### PUT /teachers/{teacher_username}/students/{student_username}
#### Description:
Add a student to a teacher's class

#### Sample Request Body:
None

#### Sample Response Body:

If username doesn't exist

{
  "message": "student's username not found"
}

{
  "message": "teacher's username not found"
}


If username does exist 

{
  "student": "inputted_student_username"
}


### DELETE /teachers/{teacher_username}/students/{student_username}
#### Description:
Delete a student from a teacher's class

#### Sample Request Body:
None

#### Sample Response Body:

If username doesn't exist

{
  "message": "student's username not found"
}

{
  "message": "teacher's username not found"
}


If username does exist 

{
  "student": "inputted_student_username"
}


### GET /students/{username}/teachers
#### Description:
Get the teachers of a student

#### Sample Request Body:
None

#### Sample Response Body:

If username doesn't exist

{
  "message": "username not found"
}

If username does exist 

{
  "teachers": []
}





### GET /tests
#### Description:
Get the names of all the tests

#### Sample Request Body:

None

#### Sample Response Body:

{

  "tests": [
  
    "samplequestions2",
    "samplequestions3",
    "samplequestions"
	
  ]

}


### GET /tests/{testName}
#### Description:
Get the questions of a test

#### Sample Request Body:
None

#### Sample Response Body:

{

  "data": {
  
    "createdBy": "john",
    "questions": [
	
      {
        "answer": " D",
        "description": "All of the girls hid themselves.\n\nWhich word is the pronoun in the above sentence?",
        "number": "1",
        "options": "A: of;B: hid;C: the;D: themselves;",
        "type": "multiple-choice"
      },
      {
        "answer": "A",
        "description": "Did you enjoy this quiz?\n\nIs there a noun in the above sentence?",
        "number": "10",
        "options": " A: Yes;B: No;",
        "type": "multiple-choice"
      },
      {
        "answer": "A",
        "description": "He returned after a year.\n\nWhich word is the preposition in the above sentence?",
        "number": "2",
        "options": "A: after;B: a;C: He;D: returned;",
        "type": "multiple-choice"
      },
      {
        "answer": " A",
        "description": "One and three make four.\n\nWhich word is the conjunction in the above sentence?",
        "number": "3",
        "options": "A: and;B: make;C: three;D: four;",
        "type": "multiple-choice"
      },
      {
        "answer": " A",
        "description": "She showed much patience.\n\nWhich word is the adjective in the above sentence?",
        "number": "4",
        "options": "A: much;B: showed;C: She;D: patience;",
        "type": "multiple-choice"
      },
      {
        "answer": " D ",
        "description": "Never tell a fib.\n\nWhich word is the noun in the above sentence?",
        "number": "5",
        "options": "A: Never;B: a;C: tell;D: fib;",
        "type": "multiple-choice"
      },
      {
        "answer": "  C",
        "description": "Hurray! we won the contest.\n\nWhich word is the interjection in the above sentence?",
        "number": "6",
        "options": "A: the;B: we;C: Hurray;D:  won;",
        "type": "multiple-choice"
      },
      {
        "answer": " C",
        "description": "John ran a short distance.\n\nWhich word is the verb in the above sentence?",
        "number": "7",
        "options": "A: distance;B: John;C: ran;D: short;",
        "type": "multiple-choice"
      },
      {
        "answer": "A",
        "description": "Sam runs quickly to the store.\n\nWhich word is the adverb in the above sentence?",
        "number": "8",
        "options": "A: quickly;B: to;C: runs;D: store;",
        "type": "multiple-choice"
      },
      {
        "answer": "A",
        "description": "There are many different parts of speech.\n\nDoes the above sentence contain an adjective?",
        "number": "9",
        "options": "A: Yes;B: No;",
        "type": "multiple-choice"
      }
    ],
    "testName": "t5"
  }
}



### GET /tests/submissions/{testName}
#### Description:
Get all submissions of a test

#### Sample Request Body:

None


#### Sample Response Body:

{

  "data": [
  
    {
      "createdBy": "bobbob",
      "submission": [
        {
          "answer": "4",
          "description": "What is 2+2?",
          "number": "1",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "D",
          "description": "The remainder of 21 divided 7 is?",
          "number": "10",
          "options": "A: 7;B: 21;C: 3;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "Lorem Ipsum",
          "description": "What is lorem ipsum?",
          "number": "11",
          "options": "",
          "providedAnswer": "115",
          "type": "essay"
        },
        {
          "answer": "22",
          "description": "How much is 65-43?",
          "number": "2",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "12",
          "description": "The square root of 144?",
          "number": "3",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "9",
          "description": "How many sides does Nonagon contain?",
          "number": "4",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "90",
          "description": "Total degrees in the right angle?",
          "number": "5",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "84.9",
          "description": "How much is 849 divided by 10?",
          "number": "6",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "",
          "description": "How many days and hours are equal to 200 hours?",
          "number": "7",
          "options": "A: 8 days and 8 hours;B: 9 days and 10 hours;C: 20 days and 20 hours;D: 10 days and 20 hours;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "A",
          "description": "In 25,600, the place value of 6 is?",
          "number": "8",
          "options": "A: 600;B: 6;C: 6000;D: 60;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "C",
          "description": "The least number of two digits is?",
          "number": "9",
          "options": "A: 99;B: 88;C: 11;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        }
      ],
      "testName": "samplequestions",
      "username": "joejoe"
    }

]



### POST /tests/{createdBy}
#### Description:
Create a test

#### Sample Request Body:

Csv file with test questions, with each question of format:


          "answer": "D",
          "description": "The remainder of 21 divided 7 is?",
          "number": "10",
          "options": "A: 7;B: 21;C: 3;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"


#### Sample Response Body:

{
  "testName": "inputted_name"
}


### DELETE /tests/{testName}
#### Description:
Delete a test

#### Sample Request Body:
None

#### Sample Response Body:

If testName doesn't exist

{
  "message": "testName not found"
}

If testName does exist 

{
  "message": "successfully removed"
}


### GET /submissions/{username}
#### Description:
Get all submissions of a student

#### Sample Request Body:
None

#### Sample Response Body:

{
  "message": "no submissions found"
}


{
  "data": [
  
    {
	
      "createdBy": "bobbob",
      "submission": [
        {
          "answer": "4",
          "description": "What is 2+2?",
          "number": "1",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "D",
          "description": "The remainder of 21 divided 7 is?",
          "number": "10",
          "options": "A: 7;B: 21;C: 3;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "Lorem Ipsum",
          "description": "What is lorem ipsum?",
          "number": "11",
          "options": "",
          "providedAnswer": "115",
          "type": "essay"
        },
        {
          "answer": "22",
          "description": "How much is 65-43?",
          "number": "2",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "12",
          "description": "The square root of 144?",
          "number": "3",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "9",
          "description": "How many sides does Nonagon contain?",
          "number": "4",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "90",
          "description": "Total degrees in the right angle?",
          "number": "5",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "84.9",
          "description": "How much is 849 divided by 10?",
          "number": "6",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "",
          "description": "How many days and hours are equal to 200 hours?",
          "number": "7",
          "options": "A: 8 days and 8 hours;B: 9 days and 10 hours;C: 20 days and 20 hours;D: 10 days and 20 hours;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "A",
          "description": "In 25,600, the place value of 6 is?",
          "number": "8",
          "options": "A: 600;B: 6;C: 6000;D: 60;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "C",
          "description": "The least number of two digits is?",
          "number": "9",
          "options": "A: 99;B: 88;C: 11;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        }
      ],
      "testName": "samplequestions",
      "username": "joejoe"
    }
  ]
}


### GET /submissions/{username}/{testName}
#### Description:
Get a submission of a student on a specific test

#### Sample Request Body:
None

#### Sample Response Body:



{
  "data": [
  
    {
	
      "createdBy": "bobbob",
      "submission": [
        {
          "answer": "4",
          "description": "What is 2+2?",
          "number": "1",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "D",
          "description": "The remainder of 21 divided 7 is?",
          "number": "10",
          "options": "A: 7;B: 21;C: 3;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "Lorem Ipsum",
          "description": "What is lorem ipsum?",
          "number": "11",
          "options": "",
          "providedAnswer": "115",
          "type": "essay"
        },
        {
          "answer": "22",
          "description": "How much is 65-43?",
          "number": "2",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "12",
          "description": "The square root of 144?",
          "number": "3",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "9",
          "description": "How many sides does Nonagon contain?",
          "number": "4",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "90",
          "description": "Total degrees in the right angle?",
          "number": "5",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "84.9",
          "description": "How much is 849 divided by 10?",
          "number": "6",
          "options": "",
          "providedAnswer": "115",
          "type": "open"
        },
        {
          "answer": "",
          "description": "How many days and hours are equal to 200 hours?",
          "number": "7",
          "options": "A: 8 days and 8 hours;B: 9 days and 10 hours;C: 20 days and 20 hours;D: 10 days and 20 hours;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "A",
          "description": "In 25,600, the place value of 6 is?",
          "number": "8",
          "options": "A: 600;B: 6;C: 6000;D: 60;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        },
        {
          "answer": "C",
          "description": "The least number of two digits is?",
          "number": "9",
          "options": "A: 99;B: 88;C: 11;D: None of these;",
          "providedAnswer": "115",
          "type": "multiple-choice"
        }
      ],
      "testName": "samplequestions",
      "username": "joejoe"
    }
  ]
}


### POST /submissions/{username}
#### Description:
Create a submission for a student

#### Sample Request Body:

{

  "submission": [{"providedAnswer": ""}], // number of objects must match number of questions in test
  "testName": "string"

}

#### Sample Response Body:

{
	
"message":"successfully added submission"

}

### DELETE /submissions/{username}/{testName}
#### Description:
Delete a submission of a student for  atest

#### Sample Request Body:
None

#### Sample Response Body:

If testName doesn't exist

{
  "message": "testName not found"
}

If testName does exist 

{
  "message": "successfully removed"
}



### GET /grades/{username}
#### Description:
Get all the grades of a student

#### Sample Request Body:
None

#### Sample Response Body:

{

  "message": "No grades found"

}

If testName does exist 

{

  "grades": {
  
	"samplequestions": 80,
	"samplequestions2": 90
  }

}



### POST /grades/{username}/{testName}
#### Description:
Create a grade for a submission

#### Sample Request Body:

{

  "grade": 0

}



#### Sample Response Body:

{

	"message": "username or test not found"
	
}

{

	"message":"successfully created Grade"

} 

### DELETE /grades/{username}/{testName}
#### Description:
Delete a grade of a student for a specific test

#### Sample Request Body:
None

#### Sample Response Body:


{
  "message": "successfully removed"
}






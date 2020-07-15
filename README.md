# TextUtiltiy
A Text editing Rest API
TextUtiltiy
A Text Editing Utility Rest API

Example Returns json data about a single user.

URL

/employe

Method:

GET

Data Params

None

Success Response: Content-Type: application/json Vary: Accept Data : { "id": 2, "username": "Aditya", "email_id": "123@gmail.com" } Error Response:

Code: 404 NOT FOUND Content: { error : "User doesn't exist" } OR

Code: 401 UNAUTHORIZED Content: { error : "You are unauthorized to make this request." }

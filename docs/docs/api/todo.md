# Todo
CRUD endpoints for Todo owned by User

## Get List of Todos

**Request**:

`GET` `/api/v1/todo/<user_id>/`

Parameters:

**Response**:

```json
Content-Type application/json
200 Ok

[
  {
        "id": 6,
        "name": "some tasks",
        "todo_status": "nc",
        "active_status": true,
        "date_added": "2020-08-26T10:17:05.097054Z",
        "date_updated": "2020-08-26T10:20:34.845735Z"
    },
]
```

## Add Task

**Request**:

`POST` `/api/v1/todo/<user_id>/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
name          | string | Yes      | What's the task?
todo_status   | enum | Yes      | Completed or Not Completed?
active_status | boolean| Yes      | If True, then it's marked as deleted


**Response**:

```json
Content-Type application/json
201 Created

{
    "id": 7,
    "name": "some tasks",
    "todo_status": "nc",
    "active_status": true,
    "date_added": "2020-08-26T10:17:05.097054Z",
    "date_updated": "2020-08-26T10:20:34.845735Z"
}
```


## Retrive Todo Data

**Request**:

`GET` `/api/v1/todo/<user_id>/<todo_id>/`

Parameters:


**Response**:

```json
Content-Type application/json
200 Ok

{
    "id": 7,
    "name": "some tasks",
    "todo_status": "nc",
    "active_status": true,
    "date_added": "2020-08-26T10:17:05.097054Z",
    "date_updated": "2020-08-26T10:20:34.845735Z"
}
```


## Update Todo

**Request**:

`PUT` `/api/v1/todo/<user_id>/<todo_id>/`

Parameters:

Name          | Type   | Required | Description
--------------|--------|----------|------------
name          | string | Yes      | What's the task?
todo_status   | enum   | Yes      | Completed or Not Completed?
active_status | boolean| Yes      | If True, then it's marked as deleted


**Response**:

```json
Content-Type application/json
200 Ok

{
    "id": 7,
    "name": "updated tasks",
    "todo_status": "nc",
    "active_status": true,
    "date_added": "2020-08-26T10:17:05.097054Z",
    "date_updated": "2020-08-26T10:20:34.845735Z"
}
```
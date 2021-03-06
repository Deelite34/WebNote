# Get all available notes.

**URL** : `/auth/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : valid token within header

## Success Response

**Code** : `200 OK`

**Content examples**

Returns available notes, for example:

```json
[
    {
        "id": 1,
        "content": "base post note",
        "views_count": 1
    },
    {
        "id": 2,
        "content": "another note",
        "views_count": 1
    }
]
```
# Add a note

**URL** : `/auth/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : valid token within header

## Success Response

**Code** : `200 OK`

**Content examples**
Sending request:
```json
{
    "content": "third note"
}
```

Will create a new Note and result in response::

```json
{
    "id": 3,
    "content": "third note",
    "views_count": 0
}
```
# Get specific note

**URL** : `/auth/:pk/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : valid token within header

## Success Response

**Code** : `200 OK`

**Content examples**

Requesting only second note trough POST request in `/auth/2/` results in incrementation of views_count for that note, and response:

```json
{
        "id": 2,
        "content": "another note",
        "views_count": 1
}
```

# Modify specific note

**URL** : `/auth/:pk/`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : valid token within header

## Success Response

**Code** : `201 Created`

**Content examples**
Sending request:
```json
{
    "content": "second note edited"
}
```
Editing second note results in:

```json
{
    "id": 2,
    "content": "second note edited",
    "views_count": 0
}
```

# Delete specific note

**URL** : `/auth/:pk/`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : valid token within header

## Success Response

**Code** : `204 No Content`

**Content examples**

Sending DELETE request at `/auth/2/`, and then sending GET request at `/auth/` shows, that secondnote is gone:

```json
[
    {
        "id": 1,
        "content": "base post note",
        "views_count": 1
    },
    {
        "id": 3,
        "content": "second note edited",
        "views_count": 0
    }
]
```

# Get all available notes.

**URL** : `/api/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

With 2 notes being present in the database, with first having id=1 and second having id=2, 
the first GET request would result with response:

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

# Get specific note

**URL** : `/api/:pk/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

Requesting only second note results in response:

```json
{
        "id": 2,
        "content": "another note",
        "views_count": 1
}
```

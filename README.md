# Mozio Technical Test 

Functionality API:
- **Complete CRUD (GET/POST/PATCH/DELETE) for Provider model**
- **Complete CRUD (GET/POST/PATCH/DELETE) for Area (Polygon) model** 
- **Filter area by provider ID**
- **Filter area by coordinates (lat/long)**

## Stack

 - Django 4.0.4
 - Python 3.8.10
 - PostgreSql 13

## Endpoints 

### Provider

> Get providers saved in the database

```plaintext
GET /apis/provider
```

Request example:

```shell
curl -X GET "http://localhost:8001/apis/provider" -H  "accept: application/json" -H  "Authorization: Token KeyToken"
```

> Save provider in the database

```plaintext
POST /apis/provider
```

Request example:

```shell
curl -X POST "http://localhost:8001/apis/provider" -H  "accept: application/json" -H  "Authorization: Token KeyToken -H  "Content-Type: application/json" -H -d {data}
```

> Update provider in the database

```plaintext
PATCH /apis/provider/{id}
```

Request example:

```shell
curl -X PATCH "http://localhost:8001/apis/provider/1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H  "Content-Type: application/json" -H -d {data}
```

> Delete provider in the database

```plaintext
DELETE /apis/provider/{id}
```

Request example:

```shell
curl -X DELETE "http://localhost:8001/apis/provider/1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H
```

### Area

> Get areas saved in the database

```plaintext
GET /apis/area
```

Request example:

```shell
curl -X GET "http://localhost:8001/apis/area" -H  "accept: application/json" -H  "Authorization: Token KeyToken"
```

> Save area in the database

```plaintext
POST /apis/area
```

Request example:

```shell
curl -X POST "http://localhost:8001/apis/area" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H  "Content-Type: application/json" -d {data}
```

> Update area in the database

```plaintext
PATCH /apis/area/{id}
```

Request example:

```shell
curl -X PATCH "http://localhost:8001/apis/area/1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H  "Content-Type: application/json" -H -d {data}
```

> Delete area in the database

```plaintext
DELETE /apis/area/{id}
```

Request example:

```shell
curl -X DELETE "http://localhost:8001/apis/area/1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H
```

> Get areas in database filtering by provider ID.

```plaintext
GET /area/filter/provider?provider_id={ID Provedor}
```

Request example:

```shell
curl -X GET "http://localhost:8001/apis/area/filter/provider?provider_id=1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H
```

> Get areas in database filtering by lat/long.

```plaintext
GET /area/filter/coordinate?lat={lat}&long={long}
```

Request example:

```shell
curl -X GET "http://localhost:8001/apis/area/filter/coordinate?lat=0.1&long=1" -H  "accept: application/json" -H  "Authorization: Token 01869aae3dff9217a13007ce6fe0d222c27fb860" -H 
```

## Deploy Information

## Docs Information

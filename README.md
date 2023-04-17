## Configuration

admin: root <br>
password: root


# How to use API

## Задачи
#### Получить все задачи
> **GET** http://localhost:8000/api/tasks/
#### Получить только одну задачу
> **GET** http://localhost:8000/api/task/<int:pk>/
#### Изменить задачу
> **PUT** http://localhost:8000/api/task/<int:pk>/
> 
> Чтобы изменить нужно в запросе отправить **body** в виде **JSON**
> 
```javascript
// Json
{
    "short_description": "some description",
    "full_description": "some description"    
}
```
#### Удалить задачу
> **DELETE** http://localhost:8000/api/task/<int:pk>/


## Проекты
#### Получить все проекты
> **GET** http://localhost:8000/api/projects/
#### Получить только один проект
> **GET** http://localhost:8000/api/project/<int:pk>/
#### Изменить проект
> **PUT** http://localhost:8000/api/project/<int:pk>/
> 
> Чтобы изменить нужно в запросе отправить **body** в виде **JSON**
> 
```javascript
// Json
{
    // required fields
    "start_date": "some date",
    "end_date": "some date",
    "name": "some name",
    "description": "some description"
}
```

#### Удалить проект
> **DELETE** http://localhost:8000/api/project/<int:pk>/
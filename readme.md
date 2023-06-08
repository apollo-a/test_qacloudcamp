## Автоматизация тестирования API.

Проект с автотестами, которые будут проверять работу всех API-эндпоинтов, описанных ниже:
- API url https://jsonplaceholder.typicode.com/
- Методы, требующие проверки: GET /posts, POST /posts, DELETE /posts
- Методы могут принимать параметры userId, id, title, body
- В качестве языка программирования используется python
- Используются библиотеки requests, а также pytest.

### Как поднять проект

1. Склонировать репозиторий в локальную директорию:
```
git clone https://github.com/your-username/your-repo.git
```
2. Перейти в директорию проекта:
```
cd your-repo
```
3. Установить зависимости:
```
pip install -r requirements.txt
```
4. Запустить приложение:
```
pytest qacloud_autotest.py
```

### Запуск контейнера Docker
```
docker-compose up --build
```

# DRF Social Network

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

DRF Social Network — это социальная сеть, разработанная с использованием Django Rest Framework (DRF). Проект предоставляет API для создания пользователей, публикации постов.

## 🚀 Технологии

- Django 5.1
- Django REST Framework 3.15
- JWT аутентификация (djangorestframework-simplejwt)
- PostgreSQL
- Docker + Docker Compose
- Nginx
- DRF Spectacular (документация API)

## Основные функции

- **Регистрация и аутентификация пользователей**: Поддержка JWT-аутентификации.
- **Публикация постов**: Пользователи могут создавать, редактировать и удалять свои посты.

## Установка и настройка

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/UsmanA07/drf-social-network.git
   cd drf-social-network
   ```
2. **Запустите проект**

   ```bash
   docker-compose up --build
   ```

## 📚 Документация API
   Доступна через Swagger/Redoc после запуска:

 - Swagger UI: http://localhost/api/schema/swagger-ui/

 - Redoc: http://localhost/api/schema/redoc/

## Эндпоинты

- POST /auth/register/ - Регистрация
- POST /auth/token/ - Получение токена
- POST /auth/token/refresh - Обновление токена

- GET /api/v1/posts/ - Список постов
- POST /api/v1/posts/ - Создание поста (требуется аутентификация)

- PATCH /api/v1/post-detail/<int:post_id> - Редактирование поста
- GET /api/v1/post-detail/<int:post_id> - Просмотр поста
- DELETE /api/v1/post-detail/<int:post_id> - Удаление поста

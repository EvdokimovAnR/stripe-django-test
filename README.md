# Django Stripe Integration

Тестовое задание: Полная интеграция Django с платежной системой Stripe

## 🚀 Быстрый старт

### Вариант 1: Docker (рекомендуется)
```bash
# 1. Клонировать репозиторий
git clone https://github.com/EvdokimovAnR/stripe-django-test
cd stripe-django-test

# 2. Создать файл с переменными окружения
cp .env.example .env
# Отредактируйте .env файл, добавьте свои ключи Stripe

# 3. Запустить контейнеры
docker-compose up --build

# 4. Создать администратора для доступа к админ-панели
# Откройте новый терминал в той же папке и выполните:
docker-compose exec web python manage.py createsuperuser
# Следуйте инструкциям в терминале:
# Username: admin (или любой другой)
# Email: ваш_email@example.com
# Password: ваш_пароль

# 5. Открыть в браузере
#    - Приложение: http://localhost:8000
#    - Админка: http://localhost:8000/admin
```
### Локальный запуск
```bash
# 1. Создать виртуальное окружение
python -m venv venv
# 2. Активировать окружение
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
# 3. Установить зависимости
pip install -r requirements.txt
# 4. Создать файл с переменными окружения
cp .env.example .env
# 5. Настроить базу данных
python manage.py migrate
# 6. Создать администратора (опционально)
python manage.py createsuperuser
# 7. Запустить сервер
python manage.py runserver
```
### Приложение доступно: http://localhost:8000
### Админка: http://localhost:8000/admin

### Функционал:
✅ **Каталог товаров** - Просмотр товаров с ценами и описаниями  
✅ **Создание заказов** - Выбор нескольких товаров в один заказ  
✅ **Stripe Checkout** - Безопасная оплата через Stripe  
✅ **Панель администратора** - Управление товарами и заказами  
✅ **Модульные тесты** - Полное покрытие кода тестами  
✅ **Docker контейнеризация** - Готовый Docker Compose  

### Тестовые платежи:
**Номер карты:** `4242 4242 4242 4242`  
**Дата:** Любая будущая дата  
**CVC:** Любые 3 цифры

### Технологии:
- **Python 3.11 + Django 4.2** - Backend
- **Stripe API** - Платежная система
- **Tailwind CSS** - Современный дизайн
- **SQLite** - База данных
- **Pytest** - Тестирование
- **Docker** - Контейнеризация

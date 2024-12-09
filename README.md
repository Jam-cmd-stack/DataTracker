# 📈 DataTracker

## Описание
**DataTracker** — это инструмент для отслеживания и анализа данных. Он позволяет пользователям добавлять, обновлять, удалять и просматривать данные через командную строку.

## Особенности
- Легкая настройка с использованием Docker.
- Хранение данных в PostgreSQL.
- Командный интерфейс для взаимодействия с данными.
- Анализ данных: возможность выполнять простые статистические вычисления (например, среднее, медиана) на основе значений в базе данных.

## Установка

### 1. Установка необходимых инструментов
Перед началом убедитесь, что у вас установлены:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Клонирование репозитория
Склонируйте проект на свой компьютер:
```bash
git clone https://github.com/Jam-cmd-stack/DataTracker/
cd DataTracker
```

## Запуск проекта

### Сборка проекта
Соберите Docker-образ:
```bash
docker-compose build
```

### Запуск приложения
Запустите проект:
```bash
docker-compose up
```
Для запуска в фоновом режиме:
```bash
docker-compose up -d
```

## Взаимодействие с приложением

### Команды
- **Добавить запись**:
  ```bash
  docker-compose run app --action add --name "Имя" --date "2024-01-01" --value 100
  ```

- **Просмотреть записи**:
  ```bash
  docker-compose run app --action view
  ```

- **Обновить запись**:
  ```bash
  docker-compose run app --action update --id 1 --name "Новое Имя" --date "2024-01-02" --value 150
  ```

- **Удалить запись**:
  ```bash
  docker-compose run app --action delete --id 1
  ```

- **Выполнить анализ данных (среднее и медиана)**:
  ```bash
  docker-compose run app --action analyze --metric average
  ```
  ```bash
  docker-compose run app --action analyze --metric median
  ```

## Остановка проекта
Чтобы остановить запущенные контейнеры:
```bash
docker-compose down
```

## Логи
Чтобы просмотреть логи приложения:
```bash
docker-compose logs
```


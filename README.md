[README.md](https://github.com/user-attachments/files/24234860/README.md)
# 3 Практическая работа: Docker + PostgreSQL

## Описание
В рамках практической работы реализовано веб-приложение с использованием Docker.
Приложение работает с базой данных PostgreSQL и может быть запущено локально через
Docker Compose, а также автоматически проверяется с помощью CI/CD в GitHub Actions.

---

## Стек технологий

- Docker — упаковка приложения и зависимостей в контейнеры  
- Docker Compose — оркестрация сервисов (web + database)  
- Python 3 — язык реализации серверной логики  
- Flask — веб-фреймворк для обработки HTTP-запросов  
- PostgreSQL — система управления реляционной базой данных  
- GitHub — система контроля версий и хранения кода  
- GitHub Actions — CI/CD pipeline для автоматической сборки, запуска и тестирования  
- Self-hosted GitHub Runner — выполнение CI/CD pipeline на локальном хосте  

Данный стек позволяет запускать приложение как локально через Docker Compose,
так и автоматически проверять его работоспособность с помощью CI/CD в GitHub Actions.

---

## CI/CD и автоматическая проверка

Для проекта настроен CI/CD pipeline с использованием GitHub Actions.

- Репозиторий: https://github.com/OvsAV/DevOps-OvsAV--22-24-3-
- Workflow: Docker app CI
- Runner: self-hosted

В ходе выполнения pipeline:
- создаётся файл окружения `.env` из GitHub Secrets;
- запускаются контейнеры с помощью Docker Compose;
- выполняются проверки доступности приложения и согласованности данных;
- формируются артефакты (логи, отчёт, замаскированный `.env`).

Артефакты доступны во вкладке **Actions**

---

## Запуск проекта (Windows)

1) Запустить:
docker compose up -d --build

2) Открыть в браузере:
http://localhost:8000 

## Остановка
docker compose down

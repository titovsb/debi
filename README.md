---
author: Sergei Titov
title: DEBI
status: Beta
version: 1.0b
---
# Развертывание приложения debi

## Подготовка
### 1. Установка pithon, pip, git
Выполните команды и убедитесь, что у вас установлены python и pip.

    $ python --version
    Python 3.9.2
    $ pip --version
    pip 21.3 from /home/...
    $git --version
    git version 2.30.2

При необходимости выполните их установку самостоятельно для python https://python-scripts.com/install-python, для pip (https://pythonru.com/baza-znanij/ustanovka-pip-dlja-python-i-bazovye-komandy).

### 2. Установка виртуального окружения

Для создания виртуального окружения создайте папку проекта и выполните следующие команды:

    $mkdir DEBI
    $cd DEBI
    $python -m venv venv
    $source venv/bin/activate

### 3. Клонирование репозитория
Для совместной работы проведите инициализацию локального репозитория и склонируйте репозиторий:

    (venv) $git config --global user.name 'debi'
    (venv) $git config --global user.email your@email
    (venv) $git init
    (venv) $git clone https://github.com/titovsb/debi
    (venv) $git pull            # здесь команды уточнить

### 4. Установка зависимостей
Установите зависимости интерпретатора:

    (venv) $python install -r site/requirements.txt

## Запуск приложения
### 1. Запуск сервера
Перейдите в папку сайта и запустите сервер

    (venv) $cd site
    (venv) $django-admin runserver

После запуска сервера в адресной строке браузера наберите адрес http://localhost:8000.

Работайте с программой согласно инструкции пользователя.



Задача сервиса ДЕБИТОРОВ.NET
--------------
Сервис предназначен для автоматического направления уведомлений пользователям о имеющейся дебиторской задолженности. База данных обеспечивает хранение информации по дебиторам, направленным уведомлениям, текущем статусе отправления. Обеспечивает получение списка пользователей надлежащим образом уведомленных, для цели передачи специалистам для формирования искового заявления.


Описание БД
-----------

1. Первичная сущность - пользователь
2. Текущая сущность - список дебиторских задолженностей. Текущаяя задолженность ОДНА, остальные неактивные (для справки)
3. отдельными полями учитываются: дата создания, дата направления уведомления, дата последнего полученного статуса.

updated: 01/09/2021
- создана структура таблиц.


# Авторизация через бота Discord

### Логика:
Если у пользователя две роли Holder и Member - авторизация проходит
Если у потзователя одна из ролей Team или Founder - авторизация проходит
Во всех остальных случаях отказ в авторизации


### Для работы:
* в config/token.py внести переменную TOKEN = 'токен_бота' (формат str)
* config/config.py - в словарь ROLES нужно внести актуальные id для ролей
* если роль отсутствует, не удаляйте ее из словаря, просто поставьте сначение None
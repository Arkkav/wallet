## REST сервис кошелька

### Техническое задание
Пишем простой REST сервис (на Django).<br/>
Подразумевается, что под ваш REST сервис будет написано отдельное приложение (SPA или мобильное).
 
Сервис по управлению финансами, функционал следующий:
- Пользователь хранит данные о своем "кошельке", произвольное название + баланс в рублях.
- В рамках кошелька ведется история транзакций (как списание, так и пополнение).
- Кошельков может быть больше чем 1, но сам пользователь один (это его персональный веб сервис).
 
API сервиса должен позволять:
1. Создавать, редактировать и удалять кошелек.
2. Создавать и удалять транзакции в рамках кошелька (при этом напрямую редактировать баланс кошелька пользователь не может).
Транзакции могут быть как +, так и -. то есть транзакции по зачислению денег и списанию. 
У каждой транзакции должна быть дата, сумма, произвольный комментарий от пользователя.
3. Просматривать список своих кошельков.
4. Просматривать список своих транзакций как в рамках одного кошелька, так и общий, всех кошельков сразу.

### Имплементация
Приложение реализовано на фреймворке Django.
 
#### Основные модули 
- wallet/apps/wallet_app/views.py - модуль логики приложения
- wallet/apps/wallet_app/models.py - описание моделей базы данных
- wallet/urls.py, wallet/apps/wallet_app/urls.py - URL-структура приложения

#### Примеры URL запросов
- просмотр кошельков (метод GET):<br/>
    http://127.0.0.1:8000/wallet_app/wallets/5/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/ <br/>

- просмотр транзакций (метод GET): <br/>
    http://127.0.0.1:8000/wallet_app/txs/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/3/txs/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/3/txs/3/ <br/>
    http://127.0.0.1:8000/wallet_app/txs/3/ <br/>

- создание кошелька (метод POST): <br/>
    http://127.0.0.1:8000/wallet_app/wallets/create/ <br/>
    body: {"name": "wal5"} <br/>

- редактирование кошелька (метод PUT): <br/>
    http://127.0.0.1:8000/wallet_app/wallets/1/update/ <br/>
    body: {"name": "my_wal2134297"} <br/>

- создание транзакции (метод POST): <br/>
    http://127.0.0.1:8000/wallet_app/txs/create/ <br/>
    body: {"wallet_id": 2, "tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} <br/>
    http://127.0.0.1:8000/wallet_app/wallets/3/txs/create/ <br/>
    body: {"tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} <br/>

- редактирование транзакции (метод PUT): <br/>
    http://127.0.0.1:8000/wallet_app/txs/2/update/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/3/txs/2/udpate/ <br/>
    body: {"wallet_id": 2, "tx_comment": "ergergweg", "tx_date": "2020-04-20 07:26:33", "tx_sum": 800} <br/>

- удаление кошельков или транзакций (метод DELETE): <br/>
    http://127.0.0.1:8000/wallet_app/txs/3/delete/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/2/delete/ <br/>
    http://127.0.0.1:8000/wallet_app/wallets/2/txs/3/delete/ <br/>

### Установка приложения 
git clone git@github.com:Arkkav/wallet.git<br/>
cd ./wallet<br/>
python3 -m venv env<br/>
./env/bin/activate<br/>
pip3 install -r requirements.txt<br/>
python3 manage.py runserver 


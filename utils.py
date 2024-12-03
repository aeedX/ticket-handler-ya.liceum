from transliterate import translit
import sqlite3
import shutil
import datetime as dt
import main


user = -1
default_image = 'data/img-placeholder.png'
edit_connection = None

def upload(file, public_id):
    file_name = public_id + file[file.rfind('.'):]
    shutil.copy2(file, f'data\\{file_name}')
    return f'data\\{file_name}'

def login(username, password):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT password, user_id FROM users WHERE username = ?""",
                            (username,)).fetchall()

    connection.close()

    if result:
        if password == result[0][0]:
            global user
            user = result[0][1]
            return 0
        return 1
    return 2

def register(username, password):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT username FROM users WHERE username = ?""",
                            (username,)).fetchall()

    if not result:
        result = cursor.execute("""SELECT user_id FROM users""").fetchall()
        user_id = result[-1][0] + 1

        cursor.execute("""INSERT INTO users VALUES (?, ?, ?, ?)""",
                       (user_id, username, password, 0))
        connection.commit()
        connection.close()
        global user
        user = user_id
        return 0
    connection.close()
    return 1

def is_user_admin():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT admin_access FROM users WHERE user_id = ?""",
                            (user,)).fetchall()

    connection.close()
    if result[-1][0]:
        return True
    return False

def get_categories(get_id = False, get_all = False):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    if get_id:
        result = cursor.execute("""SELECT category_id FROM categories""").fetchall()
    elif get_all:
        result = cursor.execute("""SELECT * FROM categories""").fetchall()
        connection.close()
        return result
    else:
        result = cursor.execute("""SELECT category_name FROM categories""").fetchall()

    connection.close()
    result = [data[0] for data in result]
    return result

def ticket_create(heading, description, category, image):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT ticket_id FROM tickets""").fetchall()
    ticket_id = result[-1][0] + 1

    category = cursor.execute("""SELECT category_id FROM categories WHERE category_name = ?""",
                              (category,)).fetchall()[0][0]

    date = dt.datetime.now().strftime('%d.%m.%Y %H:%M')

    if image != default_image:
        image = upload(image, f'{user}_{ticket_id}_{date.replace(" ", "-")}')

    cursor.execute("""INSERT INTO tickets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (ticket_id, heading, description,
                    category, 0, user, image, date, 'ожидание ответа'))
    main.printt(123)

    connection.commit()
    connection.close()

def user_tickets():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT ticket_id, heading, category, status, image
    FROM tickets WHERE user = ?""",
                            (user,)).fetchall()
    tickets = []
    categories_id = get_categories(get_id=True)
    for ticket_id, heading, category, status, image in result:
        if category in categories_id:
            category = cursor.execute("""SELECT category_name FROM categories
            WHERE category_id = ?""",
                                      (category,)).fetchall()[0][0]
            if category == 'deleted':
                category = 'другое'
        else:
            category = 'другое'
        status = cursor.execute("""SELECT status FROM statuses WHERE status_id = ?""",
                                  (status,)).fetchall()[0][0]
        tickets.append([str(ticket_id), heading, category, status, image])
    connection.close()
    return tickets

def all_tickets():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT ticket_id, heading, category, status, user, image
    FROM tickets""").fetchall()
    tickets = []
    categories_id = get_categories(get_id=True)
    for ticket_id, heading, category, status, user, image in result:
        if category in categories_id:
            category = cursor.execute("""SELECT category_name FROM categories
            WHERE category_id = ?""",
                                      (category,)).fetchall()[0][0]
        else:
            category = 'deleted'
        status = cursor.execute("""SELECT status FROM statuses WHERE status_id = ?""",
                                (status,)).fetchall()[0][0]

        user = cursor.execute("""SELECT username FROM users WHERE user_id = ?""",
                                      (user,)).fetchall()[0][0]
        tickets.append([str(ticket_id), heading, category, status, user, image])
    connection.close()
    return tickets

def create_connection():
    global edit_connection
    edit_connection = sqlite3.connect('data/data.db')

def add_category(category_name):
    cursor = edit_connection.cursor()

    result = cursor.execute("""SELECT category_id FROM categories""").fetchall()
    category_id = result[-1][0] + 1
    cursor.execute("""INSERT INTO categories VALUES (?, ?)""",
                   (category_id, category_name))
    result = cursor.execute("""SELECT * FROM categories WHERE category_id = ?""",
                            (category_id,)).fetchall()
    return result[0]

def delete_category(category_name):
    cursor = edit_connection.cursor()

    cursor.execute("""UPDATE categories SET category_name = 'deleted' WHERE category_name = ?""",
                   (category_name,))

def get_users(get_id = False):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

def get_admins():
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT user_id, username FROM users
    WHERE admin_access = 1""").fetchall()

    connection.close()
    return result

def add_admin(username):
    cursor = edit_connection.cursor()

    cursor.execute("""UPDATE users SET admin_access = 1 WHERE username = ?""", (username,))
    result = cursor.execute("""SELECT user_id, username FROM users WHERE username = ?""",
                            (username,)).fetchall()
    return result[0]

def delete_admin(username):
    cursor = edit_connection.cursor()

    cursor.execute("""UPDATE users SET admin_access = 0 WHERE username = ?""", (username,))
    result = cursor.execute("""SELECT user_id, username FROM users WHERE username = ?""",
                            (username,)).fetchall()
    return result[0]

def cancel_connection():
    edit_connection.close()

def commit_connection():
    edit_connection.commit()
    edit_connection.close()

def get_ticket(ticket_id):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    result = cursor.execute("""SELECT * FROM tickets WHERE ticket_id = ?""",
                            (ticket_id,)).fetchall()
    category = get_categories()[get_categories(get_id=True).index(result[0][3])]
    username = cursor.execute("""SELECT username FROM users WHERE user_id = ?""",
                          (result[0][5],)).fetchall()[0][0]

    connection.close()
    return [ticket_id, result[0][1], result[0][2], category, result[0][4],
            username, result[0][6],result[0][7], result[0][8]]

def manage_ticket(ticket_id, delete_ticket):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    if delete_ticket:
        cursor.execute("""DELETE FROM tickets WHERE ticket_id = ?""",
                       (ticket_id,))
    else:
        cursor.execute("""UPDATE tickets SET status = 2 WHERE ticket_id = ?""",
                       (ticket_id,))

    connection.commit()
    connection.close()

def update_ticket(ticket_id, status, answer, date):
    connection = sqlite3.connect('data/data.db')
    cursor = connection.cursor()

    if status == 1:
        cursor.execute("""UPDATE tickets SET status = ?, answer = ?, date = ?
        WHERE ticket_id = ?""",
                       (status, answer,
                        date + dt.datetime.now().strftime('%d.%m.%Y %H:%M'), ticket_id))
    else:
        cursor.execute("""UPDATE tickets SET status = ?, answer = ? WHERE ticket_id = ?""",
                       (status, answer, ticket_id))

    connection.commit()
    connection.close()

def get_timedelta(date):
    main.printt(date)
    if len(date) > 16:
        delay = dt.datetime.strptime(date[16:],
                                     '%d.%m.%Y %H:%M') - dt.datetime.strptime(date[:16],
                                                                              '%d.%m.%Y %H:%M')
        date = date[:16]
        main.printt(123)
    else:
        delay = dt.datetime.now() - dt.datetime.strptime(date, '%d.%m.%Y %H:%M')
    if delay.total_seconds() // 60 < 60:
        delta = int(delay.total_seconds() // 60)
        if delta % 10 == 1:
            delta = f'{delta} минута'
        elif 2 <= delta % 10 <= 4:
            delta = f'{delta} минуты'
        else:
            delta = f'{delta} минут'
    elif delay.total_seconds() < 86399:
        delta = int(delay // 60)
        if delta % 10 == 1:
            delta = f'{delta} час'
        elif 2 <= delta % 10 <= 4:
            delta = f'{delta} часа'
        else:
            delta = f'{delta} часов'
    elif delay < dt.timedelta(days=7):
        delta = int(delay.days)
        if delta % 10 == 1:
            delta = f'{delta} день'
        elif 2 <= delta % 10 <= 4:
            delta = f'{delta} дня'
        else:
            delta = f'{delta} дней'
    else:
        delta = int(delay.days // 7)
        if delta % 10 == 1:
            delta = f'{delta} неделя'
        elif 2 <= delta % 10 <= 4:
            delta = f'{delta} недели'
        else:
            delta = f'{delta} недель'

    main.printt(123)
    return date, delta

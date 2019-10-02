import random


class UserModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_id VARCHAR(50),
                             name VARCHAR(100),
                             image_id VARCHAR(100),
                             ratio VARCHAR(50),
                             step VARCHAR(2)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_id, name, image_id, ratio):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                                  (user_id, name, image_id, ratio, step) 
                                  VALUES (?,?,?,?,?)''', (str(user_id) ,name, image_id, str(ratio), '0'))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id = {str(user_id)}")
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def get_all_rated(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT user_id FROM users")
        rows = cursor.fetchall()
        return sorted(rows, key=lambda x: int(x[4]))

    def exists(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id = {str(user_id)} ")
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return True

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (str(user_id),))
        cursor.close()
        self.connection.commit()

    def get_length(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users')
        row = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return len(row)

    def add_ratio(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT ratio FROM users WHERE user_id = {str(user_id)}')
        current = cursor.fetchone()
        new_ratio = int(current[0]) + 1
        cursor.execute('UPDATE users SET ratio = ? WHERE user_id = ?', (new_ratio, str(user_id)))
        cursor.close()
        self.connection.commit()

    def get_two_random(self, current_user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT user_id FROM users")
        try:
            all_user_id = [i[0] for i in cursor.fetchall()]
        except ValueError:
            all_user_id = cursor.fetchall()
        first_choice = random.choice(all_user_id)
        all_user_id.remove(first_choice)
        second_choice = random.choice(all_user_id)
        return (self.get(first_choice), self.get(second_choice))

    def get_step(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE user_id={str(user_id)}")
        step = cursor.fetchone()
        return int(step[5])

    def set_step(self, user_id, new_step):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT step FROM users WHERE user_id={str(user_id)}")
        step = cursor.fetchone()
        print('pm setstep', step)
        cursor.execute('UPDATE users SET step = ? WHERE user_id = ?', (str(new_step), str(user_id)))
        cursor.close()
        print(self.get(user_id))
        self.connection.commit()

    def update_user(self,user_id, name, image_id):
        cursor = self.connection.cursor()
        cursor.execute('''UPDATE users SET
                          (name, image_id) = (?,?) WHERE user_id=?''', (name, image_id,str(user_id)))
        cursor.close()
        self.connection.commit()

    def clear_db(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM users')
        cursor.close()
        self.connection.commit()
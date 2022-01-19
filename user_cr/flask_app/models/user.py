from flask_app.config.mysqlconnection import connectToMySQL

class usercls:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)
        # print(results)
        userlist = []
        for user in results:
            userlist.append(cls(user))
        return userlist

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first)s, %(last)s, %(email)s)"
        result = connectToMySQL("users_schema").query_db(query,data)
        return result

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,id)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query ="UPDATE users SET first_name= %(first)s , last_name=%(last)s , email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query= "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)
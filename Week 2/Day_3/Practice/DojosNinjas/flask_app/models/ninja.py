from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return data['dojo_id']
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """
            SELECT dojos.*, ninjas.id as ninja_id, ninjas.first_name, 
            ninjas.last_name, ninjas.age
            FROM dojos
            LEFT JOIN ninjas ON ninjas.dojo_id = dojo.id
            WHERE dojo.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if not results:
            return None
        
        dojo = cls(results[0])
        for row in results:
            if row['ninja_id']:
                ninja_data = {
                    'id': row['ninja_id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
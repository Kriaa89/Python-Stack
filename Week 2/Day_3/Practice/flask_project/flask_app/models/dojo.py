from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
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
        return [cls(row) for row in results]
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_with_ninjas(cls, data):
        query = """SELECT * FROM dojos
                LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id
                WHERE dojos.id = %(id)s;"""
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        
        if not results or len(results) == 0:
            return None
            
        dojo = cls(results[0])
        for row in results:
            if row['ninjas.id'] is not None:  # Check if there are any ninjas
                ninja_data = {
                    "id": row['ninjas.id'], 
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "dojos_id": row['dojos_id'],  # Changed from dojo_id
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                }
                dojo.ninjas.append(Ninja(ninja_data))
        return dojo
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results


    @classmethod 
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        show = cls(results[0])
        new_ninja_data = {
            'id' : results[0]['id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'age' : results[0]['age'],
            'created_at' : results[0]['created_at'],
            'updated_at' : results[0]['updated_at'],
            'dojo_id' : results[0]['dojo_id']
        }
        ninja = Ninja(new_ninja_data)
        return results[0]



    
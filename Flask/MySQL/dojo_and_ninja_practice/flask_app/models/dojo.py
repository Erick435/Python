from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninja = {}

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojo_name)s, NOW(), NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results

    @classmethod 
    def get_all_dojos(cls):
        query ="SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for one_dojo in results:
            dojos.append(cls(one_dojo))
        return dojos

    

    # @classmethod
    # def ninjas_in_dojo(cls):
    #     query = "SELECT ninjas.first_name, ninjas.last_name, ninjas.age FROM dojos LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    #     dojos = []
    #     for row in results:
    #         dojo = cls(row)
    #         ninja_data = {
    #             'id' : row['ninjas.id'],
    #             'first_name' : row['first_name'],
    #             'last_name' : row['last_name'],
    #             'age' : row['age'],
    #             'created_at' : row['ninjas.created_at'],
    #             'updated_at' : row['ninjas.updated_at'],
    #             'dojos_id' : row['ninjas.dojos_id']
    #         }
    #         dojo.ninja = ninja.Ninja(ninja_data)
    #         dojos.append(cls(row))
    #     return dojos


from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.db).query_db(query)
        allDojos = []
        for row in results:
            dojo = cls(row)
            allDojos.append(dojo)
        return allDojos

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
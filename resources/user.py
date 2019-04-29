from flask_restful import Resource
class User(Resource):
    def __init__(self,users):
       self.users = users

    def get(self, id):
        for user in self.users:
            if(user["id"] == id):
                return user, 200
        return "User not found", 404
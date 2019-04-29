from flask_restful import Resource

class Account(Resource):
    def __init__(self,accounts):
       self.accounts = accounts
    def get(self, id):
        for account in self.accounts:
            if(account["id"] == id):
                return account, 200
        return "Account not found", 404
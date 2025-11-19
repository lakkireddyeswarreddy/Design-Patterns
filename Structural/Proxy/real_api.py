from api import API

class RealAPI(API):
    
    def get_user_details(self, user_id):
        print("Lazy loading the complex database operation..")
        return f"User details of the user with {user_id} are : ..."
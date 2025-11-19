from api import API
from real_api import RealAPI
import time

class ProxyAPI(API):
    
    def __init__(self, real_api : RealAPI):
        self._real_api = real_api
        self._cache = dict()
        self._request_times = list()
        self._limit = 5
        
    def get_user_details(self, user_id):
        
        current_time = time.time()
        
        self._request_times = [ request_time for request_time in self._request_times if current_time - request_time < 60]
        
        if len(self._request_times) > self._limit:
            return "API limit exceeded..."
        
        self._request_times.append(current_time)
        
        if user_id in self._cache:
            print("Returning the user details from the remote")
            return self._cache[user_id]
        
        user_details = self._real_api.get_user_details(user_id)
        
        self._cache[user_id] = user_details
        return user_details
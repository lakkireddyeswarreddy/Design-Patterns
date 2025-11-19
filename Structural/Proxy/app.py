
"""
Proxy pattern is used to create an surrogate or placeholder for another object for controlling access to it.
We have different types of proxies:

1. Virtual proxies : Creates objects on demand (Lazy loading).
2. Remote proxies : Uses the cached object from different adress space.
3. Protection proxies : Controls direct access to the original object.
4. Smart Reference : Performs additional operations when an object is accessed.
"""
from proxy_api import ProxyAPI
from real_api import RealAPI
import random

if __name__ == "__main__":
    
    proxy_api = ProxyAPI(RealAPI())
    
    # print(proxy_api.get_user_details(random.choice[1,2,3]))
    
    for i in range(10):
        print(proxy_api.get_user_details(random.choice([1,2,3])))
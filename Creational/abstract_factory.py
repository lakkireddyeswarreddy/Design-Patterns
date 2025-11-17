from abc import ABC, abstractmethod

class Server(ABC):
    
    @abstractmethod
    def get_instance(self):
        pass
    
class EC2Server(Server):
    
    def get_instance(self):
        return "EC2 server instance from AWS."
    
class VMServer(Server):
    def get_instance(self):
        return "VM server instance from Azure."
    
    
class Storage(ABC):
    
    @abstractmethod
    def get_storage(self):
        pass
    
class S3Storage(Storage):
    
    def get_storage(self):
        return "S3 storage from AWS."
    
class BlobStorage(Storage):
    
    def get_storage(self):
        return "blob storage from Azure."
    
    
class CloudFactory(ABC):
    
    @abstractmethod
    def get_server(self):
        pass
    

    @abstractmethod
    def get_storage(self):
        pass
    
    
class AWSCloudFactory(CloudFactory):
    
    def get_server(self):
        return EC2Server().get_instance()
    
    def get_storage(self):
        return S3Storage().get_storage()
    
class AzureCloudFactory(CloudFactory):
    
    def get_server(self):
        return VMServer().get_instance()
    
    def get_storage(self):
        return BlobStorage().get_storage()
    
    
if __name__ == "__main__":
    
    aws_obj = AWSCloudFactory()
    print(aws_obj.get_server())
    print(aws_obj.get_storage())
    
    azure_obj = AzureCloudFactory()
    print(azure_obj.get_server())
    print(azure_obj.get_storage())
    
    
        
        
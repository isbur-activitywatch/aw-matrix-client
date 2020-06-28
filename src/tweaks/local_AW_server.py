import requests 
from urllib.parse import urljoin


class AW_server(requests.Session):

    def __init__(self, url):
        requests.Session.__init__(self)
        self.base_url = url
    
    def get(self, appendix = "", **kwargs):        
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.get(self, my_url, **kwargs)
    
    def post(self, appendix = "", **kwargs):
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.post(self, my_url, **kwargs)
    
    def get_event_count_from_(self, bucket_id):
        if type(bucket_id) != type(""):
            raise TypeError("must be str")

        return self.get(
        "/api/0/buckets/"   +
                    bucket_id  +
                    "/events/count"
        )


local_AW_server = AW_server("http://localhost:5600")


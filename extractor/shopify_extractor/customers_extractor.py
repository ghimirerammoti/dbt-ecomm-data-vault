from api_client import get_json
from utils.base_extractor import BaseExtractor

class CustomersExtractor(BaseExtractor):
    def extract(self):
        return get_json("customers.json")
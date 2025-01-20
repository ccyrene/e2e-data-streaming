import uuid

from typing import Dict

def format_data(data: Dict) -> Dict:
    data_with_format = {}
    
    location = data['location']
    data_with_format['id'] = str(uuid.uuid4())
    data_with_format['first_name'] = data['name']['first']
    data_with_format['last_name'] = data['name']['last']
    data_with_format['gender'] = data['gender']
    data_with_format['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data_with_format['post_code'] = location['postcode']
    data_with_format['email'] = data['email']
    data_with_format['username'] = data['login']['username']
    data_with_format['dob'] = data['dob']['date']
    data_with_format['registered_date'] = data['registered']['date']
    data_with_format['phone'] = data['phone']
    data_with_format['picture'] = data['picture']['medium']

    return data_with_format
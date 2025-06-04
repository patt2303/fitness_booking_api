import json
import pytz
from datetime import datetime

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, default=str)

def convert_to_timezone(dt_str, target_tz='UTC'):
    ist = pytz.timezone('Asia/Kolkata')
    target = pytz.timezone(target_tz)
    dt = ist.localize(datetime.fromisoformat(dt_str))
    return dt.astimezone(target).isoformat()
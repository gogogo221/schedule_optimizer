import json
from json import JSONEncoder
    
class ComplexEncoder(JSONEncoder):
    def default(self, schedule):
        if hasattr(schedule,'reprJSON'):
            return schedule.reprJSON()
        else:
            return json.JSONEncoder.default(self, schedule)
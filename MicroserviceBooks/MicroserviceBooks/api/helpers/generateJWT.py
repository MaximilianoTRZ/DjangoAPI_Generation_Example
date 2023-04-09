from django.utils import timezone
from MicroserviceBooks.settings import env
import datetime
import json 
import jwt


def getTime(sec):
    expiresIn = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=sec)
    expiresInAsInt = expiresIn.year*10000000000 + expiresIn.month * 100000000 + expiresIn.day * 1000000 + (expiresIn.hour)*10000 + expiresIn.minute*100 + expiresIn.second
    return expiresInAsInt

def generateJWT(finalToken):
    finalToken = json.dumps(finalToken)
    time = getTime(1800) #Time in seconds
    expiresIn = json.dumps({"exp": time})
    # expiresIn = json.dumps({"exp": 1800})
    payload = {**json.loads(finalToken), **json.loads(expiresIn)}

    try:
        jwt_token = jwt.encode(payload, env("JWT_SECRET"), algorithm="HS256")
    except:
        print("Error Generating JWT")

    return jwt_token
        

#call to functions
# parameterfinalToken = {"user_id":"31546518749"}
# jwt_encoded = generateJWT(parameterfinalToken)
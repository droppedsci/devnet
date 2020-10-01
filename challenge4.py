import requests
import json

myWebexToken = "Y2lzY29zcGFyazovL3VzL1JPT00vZTFlNzc5MTAtMDJiZC0xMWViLWE3NWUtNmRlMjNmMjlkZjRk"


room_url = "https://webexapis.com/v1/rooms"
message_url = "https://webexapis.com/v1/messages"

room_data = {
     "id": "Y2lzY29zcGFyazovL3VzL1JPT00vY2RmMTcxODAtMDQxYy0xMWViLWIwNDUtZjVjZGM0Y2JlZGFi",
     "title": "DevNet High 2020",
}

message_data = "{\n    \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vY2RmMTcxODAtMDQxYy0xMWViLWIwNDUtZjVjZGM0Y2JlZGFi\",\n    \"text\": \"TinkyWinky, Tipsy, Lala, Poe\"\n}"

header = {
     'Authorization': 'Bearer NmRhYTlmN2ItZmU2Ny00NjdiLTg4YjYtZWYyMGQwNmVmN2FiMmZjNTgwMGEtNjZl_PF84_consumer',
     'Content-Type': 'application/json'
}

def post_message():

     response = requests.request("POST",url = message_url,headers = header,data=message_data)


if __name__ == '__main__':
      response = requests.request("POST",url=room_url,headers=header, data=room_data)
      if response.request == 200:
          post_message()

      else:
          print('An error occurred')

# import urllib.request
# import json
#
# def getResponse(url):
#     operUrl = urllib.request.urlopen(url)
#     jsonData = ''
#     if(operUrl.getcode()==200):
#         data = operUrl.read()
#         jsonData = json.loads(data)
#
#     else:
#         print("Error receiving data", operUrl.getcode())
#     return jsonData
#
# def main():
#
#     urlData = "https://api.thecatapi.com/v1/images/search"
#     jsonData = getResponse(urlData)
#     # print the state id and state name corresponding
#     # for i in jsonData["states"]:
#     #     print(f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}')
#     print(jsonData[0]["url"])
#
# if __name__ == '__main__':
#     main()


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# # Assume that you have installed requests: pip install requests
# from rest_framework import request
# import json

# class GenerateCredential(APIVIew):
#     """ This view make and external api call, save the result and return
#         the data generated as json object """
#     # Only authenticated user can make request on this view
#     permission_classes = (IsAuthenticated, )
#     def get(self, request, format=None):
#         # The url is like https://localhost:8000/api/?results=40
#         results = self.request.query_params.get('type')
#         response = {}
#         # Make an external api request ( use auth if authentication is required for the external API)
#         r = requests.get('https://randomuser.me/api/?results=40', auth=('user', 'pass'))
#         r_status = r.status_code
#         # If it is a success
#         if r_status = 200:
#             # convert the json result to python object
#             data = json.loads(r.json)
#             # Loop through the credentials and save them
#             # But it is good to avoid that each user request create new
#             # credentials on top of the existing one
#             # ( you can retrieve and delete the old one and save the news credentials )
#             for c in data:
#                 credential = Credential(user = self.request.user, value=c)
#                 credential.save()
#             response['status'] = 200
#             response['message'] = 'success'
#             response['credentials'] = data
#         else:
#             response['status'] = r.status_code
#             response['message'] = 'error'
#             response['credentials'] = {}
#         return Response(response)
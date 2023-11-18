import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
import requests
from rest_framework.decorators import api_view
from .models import VMs
from rest_framework.response import Response
from .serializers import VmSerializer

# @api_view
# class AuthVMView(APIView):
#     # queryset = VMs.objects.all()
#     # serializer_class = VmSerializer
#    # logger.debug("Processing request")
#     print("Hello, this message will be printed to the terminal.")
#     def post(self, request):
#         # Deserialize the request data
#         #serializer = VmSerializer(data=request.data)
#         #if serializer.is_valid():
#             #vm_data = serializer.validated_data

#                 # Call vSphere API to create VM
#             permission_classes = [permissions.IsAuthenticated]
#             vcenter_url = 'https://2226.ciscofreak.com/api/'
#             username = 'administrator@vsphere.local'
#             password = 'Time4work!'


#             credentials = f"{username}:{password}"
#             credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

#     # Create the headers with the Authorization header
#             headers = {'Authorization': f'Basic {credentials_encoded}'}

#         #header = {'Authorization': ' Basic base64encoded(username:password)'}
#            # try:

#             print(headers)
#             response = requests.post(vcenter_url + 'session', headers=headers, verify=False)
#             print (response)
#             if response.status_code == 200:
#                      return Response({'message': 'VM created successfully'}, status=status.HTTP_201_CREATED)
#             else:
#                     # Handle other status codes accordingly
#                     return Response({'error': f'Error from vSphere API: {response.status_code}'},
#                                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         #     except Exception as e:
        #         # Handle connection or other exceptions
        #         return Response({'error': f'Exception while connecting to vSphere API: {str(e)}'},
        #                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # # else:
        #     return Response({'error': 'Invalid input data'}, status=status.HTTP_400_BAD_REQUEST)
# 


# class Vm(APIView):
#        def create():
              




# @api_view(['GET'])
# def getData(request):
#     users = MyUser.objects.all()
#     users_serializer = MyUserSerializer(users, many=True)
#     return Response(users_serializer.data)


@api_view(['POST'])    
def create_vm(request):
    if request.method=='POST':
        data=request.data
        
      
        print(data)
        serializer = VmSerializer(data=data)
        print(serializer)

        vcenter_url = 'https://2226.ciscofreak.com/api/'
        username = 'administrator@vsphere.local'
        password = 'Time4work!'
        credentials = f"{username}:{password}"
        credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

        headers = {'Authorization': f'Basic {credentials_encoded}'}
        response = requests.post(vcenter_url + 'session', verify=False)
        print(response.json())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response("Errrro")


# @api_view(['PUT'])    
# def update_user(request, id):
#     if request.method=='PUT':
#         data=request.data
#         user_obj = MyUser.objects.get(id=id)
#         serializer = MyUserSerializer(user_obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response("Errrro")

# @api_view(['DELETE'])    
# def delete_user(request, id):
#     if request.method=='DELETE':
#         data=request.data
#         user_obj = MyUser.objects.get(id=id)
#         user_obj.delete()
#         return Response("Delete succesffully")








              
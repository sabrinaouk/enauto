import base64
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

from dotenv import load_dotenv
import os

load_dotenv()

@api_view(['POST'])    
def create_vm(request):
    print('Test')
    if request.method=='POST':
        data=request.data
        
      
        print(data)
        serializer = VmSerializer(data=data)

        vm=serializer.create(data)
        print('hadi vm',vm)
        
        # username=os.environ.get('VSPHEREUSERNAME')
        # password=os.environ.get('VSPHEREPASSWORD')
        # api_host=os.environ.get('API_HOST')
       
      
        # url=f'https://{api_host}/rest/vcenter/vm'
       
        # data=request.data
        # credentials = f"{username}:{password}"
        # credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

        # headers = {'Authorization': f'Basic {credentials_encoded}'}
        # response = requests.post(url ,headers=headers,data=data, verify=False)
        # print(response.json())

        # print(response.status_code)
        if serializer.is_valid():
        #     response = requests.post(url ,headers=headers,data=data, verify=False)
        #     print(response.json())
            serializer.save()
            return Response(serializer.data)
    return Response("Errrro")


       
# # #################Create vm #################################
# # @api_view(['POST'])    
# # def create_vm(request):
# #         print('Test')
       
# #         if request.method=='POST':

# #                 username=os.environ.get('VSPHEREUSERNAME')
# #                 password=os.environ.get('VSPHEREPASSWORD')
# #                 api_host=os.environ.get('API_HOST')
# #                 data=request.data
# #                 print(data)
                 
                        
# #                 url=f'https://{api_host}/rest/vcenter/vm'
                        
# #                 credentials = f"{username}:{password}"
# #                 print(username)
# #                 credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# #                 headers = {'Authorization': f'Basic {credentials_encoded}'}
                           
# #                 serializer = VmSerializer(data=data)    
# #                 if serializer.is_valid():
#  #                        response = requests.post(url ,headers=headers,data=data, verify=False)
# #                         print(response.json())
# #                         serializer.save()
# #                         return Response(serializer.data)
# #         return Response("Errrro")

# ################Get details one VM#####################

@api_view(['GET'])
def get_Onevm(request,pk,**kargs):
        print('HELLO')
        print(kargs)
        print(pk)
      
        # try:
                # Vm=get_object_or_404(VMs, idvm=pk)
        vm = VMs.objects.get(idvm=pk)
        print(vm)
        # except VMs.DoesNotExist:
        #         return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method=='GET':
                # username=os.environ.get('VSPHEREUSERNAME')
                # password=os.environ.get('VSPHEREPASSWORD')
                # api_host=os.environ.get('API_HOST')
                # url=f'https://{api_host}/rest/vcenter/vm/{vm}'
                # credentials = f"{username}:{password}"
                # credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

                # headers = {'Authorization': f'Basic {credentials_encoded}'}
                serializer=VmSerializer(vm)
                # response = requests.delete(url ,headers=headers, verify=False)
                # print(response.json())
                # print(response.status_code)

        return Response(serializer.data)


# # ################### Delete one vm#####################

# @api_view(['DELETE'])
# def delete_Onevm(request, pk):
#         print(pk)
#         try:
#                 vm=get_object_or_404(VMs, idvm=pk)
#                 # Vm = VMs.objects.get(idvm=pk)
#                 print(vm)
#         except VMs.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         if request.method=='DELETE':
#                 username=os.environ.get('VSPHEREUSERNAME')
#                 password=os.environ.get('VSPHEREPASSWORD')
#                 api_host=os.environ.get('API_HOST')
#                 url=f'https://{api_host}/rest/vcenter/vm/{vm}'
#                 credentials = f"{username}:{password}"
#                 credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

#                 headers = {'Authorization': f'Basic {credentials_encoded}'}
#                 serializer=VmSerializer(vm)
#                 print (serializer)
              
        
                
#                 response = requests.delete(url ,headers=headers, verify=False)
#                 print(response.json())
#                 # serializer.delete()
#         return Response("Errrro")
             


# ###################Update###################



# # @api_view(['PUT'])
# # def update_vm(request, pk):
# #     if request.method=='':
# #         data=request.data
# #         username=os.environ.get('VSPHEREUSERNAME')
# #         password=os.environ.get('VSPHEREPASSWORD')
# #         api_host=os.environ.get('API_HOST')
       
# #         serializer = VmSerializer(data=data)
  
# #         url=f'https://{api_host}/rest/vcenter/vm'
       
# #         data=request.data
# #         credentials = f"{username}:{password}"
# #         credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# #         headers = {'Authorization': f'Basic {credentials_encoded}'}
        
# #         if serializer.is_valid():
# #             response = requests.post(url ,headers=headers,data=data, verify=False)
# #             print(response.json())
# #             serializer.save()
# #             return Response(serializer.data)
# #     return Response("Errrro")

























#     item = itemgetter.objects.get(pk=pk)
#     serializer = VmSerializer(instance=item, data=request.data)
 
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['DELETE'])
# def delete_items(request, pk):
#         if request.method=='DELETE':
#                 data=request.data
       
#         serializer = VmSerializer(data=data)
  
#         url=f'https://{api_host}/rest/vcenter/vm'
       
#         data=request.data
#         credentials = f"{username}:{password}"
#         credentials_encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

#         headers = {'Authorization': f'Basic {credentials_encoded}'}
        
#         if serializer.is_valid():
#             response = requests.post(url ,headers=headers,data=data, verify=False)
#             print(response.json())
#             serializer.save()
#             return Response(serializer.data)
#     return Response("Errrro")

#         item = itemgetter.objects.get(pk=pk)
#         serializer = VmSerializer(instance=item, data=request.data)
 
#         if serializer.is_valid():
#                 serializer.delete()
#                 return Response(serializer.data)
#         else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
        



        



 









              

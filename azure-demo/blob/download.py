import requests
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

url = 'http://localhost:50342/oauth2/token'
header = {'Metadata' : "true"}

r = requests.post(url, data={'resource': 'https://management.azure.com/'}, headers=header)
access_token = r.json()['access_token']

subID = "77bbb887-5daa-4b0b-acf6-46f07353c2cf"
rg = "DD"
storage_account_name = "burnignluffy1"
authToken = "Bearer %s" % (access_token)
blob_url = "https://management.azure.com/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Storage/storageAccounts/%s/listKeys?api-version=2016-12-01" % (subID, rg, storage_account_name)

header = {'Authorization' : authToken}
r = requests.post(blob_url, data={}, headers=header)
account_key = r.json()['keys'][0]['value']



block_blob_service = BlockBlobService(account_name=storage_account_name, account_key=account_key)
container_name ='images'
full_path_to_file2 = os.path.join('./', 'icon.jpg')
block_blob_service.get_blob_to_path(container_name, 'icon.jpg', full_path_to_file2)

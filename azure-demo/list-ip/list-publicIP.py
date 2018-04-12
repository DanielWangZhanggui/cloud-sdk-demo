# -*- coding: UTF-8 -*-
import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient


LOCATION = 'westus'

# Resource Group
GROUP_NAME = 'HH'
TAGs = {u'app': u'Memcached'}


def get_credentials():
    subscription_id = 'XXXX'
    credentials = ServicePrincipalCredentials(
        client_id='XXXX',
        secret='XXXX',
        tenant='XXXX'
    )
    return credentials, subscription_id


def list_vms(tags, group_name):
    credentials, subscription_id = get_credentials()
    # compute_client = ComputeManagementClient(credentials, subscription_id)
    # for vm in compute_client.virtual_machines.list_all():
    #     print("\tVM: {}".format(vm))
    network_client = NetworkManagementClient(credentials, subscription_id)
    for public_ip in network_client.public_ip_addresses.list(group_name):
        if(public_ip.tags == tags):
            print public_ip.ip_address
    # resource_client = ResourceManagementClient(credentials, subscription_id)
    # for tags in resource_client.tags.list({'app':'Memcached'}):
    #     print("\ttags: {}".format(tags.tag_name))

if __name__ == "__main__":
    list_vms(TAGs,GROUP_NAME)
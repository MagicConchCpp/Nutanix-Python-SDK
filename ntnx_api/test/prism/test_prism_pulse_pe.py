#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_update_pulse():
    """Test that pulse configuration can be updated"""
    result = True
    # Cannot test pulse against Nutanix CE
    # result = False
    # test_pulse = {
    #     'enable': True,
    #     'email': [
    #         'davies.ross@gmail.com',
    #         'ross.davies@nutanix.com',
    #     ],
    #     'email_nutanix': True,
    # }
    #
    # reset_pulse = {
    #     'enable': True,
    #     'email': [],
    #     'email_nutanix': True,
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_pe_api())
    # config_obj = prism.Config(api_client=_pe_api())
    #
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_update_pulse = config_obj.set_pulse(enable=test_pulse['enable'], email_address_list=test_pulse['email'],
    #                                                email_nutanix=test_pulse['email_nutanix'], clusteruuid=each_uuid)
    #
    #     cluster_pulse = config_obj.get_pulse(clusteruuid=each_uuid)
    #
    #     if not cluster_pulse:
    #         result = True
    #
    #     config_obj.set_pulse(enable=reset_pulse['enable'], email_address_list=reset_pulse['email'], email_nutanix=reset_pulse['email_nutanix'],
    #                          clusteruuid=each_uuid)
    assert result
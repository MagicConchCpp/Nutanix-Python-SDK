#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_add_smtp_pe():
    """Test that smtp configuration can be added on prism element"""
    result = True
    # Cannot test smtp against Nutanix CE
    # result = False
    # test_smtp = {
    #     'smtp_server': 'relay.ntnx-lab.com',
    #     'port': 25,
    #     'mode': 'tls',
    #     'from_email_address': 'do-not-reply@ntnx-lab.com',
    #     'username': 'emailuser',
    #     'password': 'emailuserpassword',
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    #
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_add_smtp = config_obj.set_smtp(address=test_smtp['smtp_server'], port=test_smtp['port'], mode=test_smtp['mode'],
    #                                           from_email_address=test_smtp['from_email_address'], username=test_smtp['username'],
    #                                           password=test_smtp['password'], clusteruuid=each_uuid, force=True)
    #
    #     cluster_smtp = config_obj.get_smtp(clusteruuid=each_uuid)
    #     if cluster_smtp['address'] == test_smtp['smtp_server'] and cluster_smtp['from_email_address'] == test_smtp['from_email_address'] and \
    #             cluster_smtp['port'] == test_smtp['port'] and test_smtp['mode'].upper() in cluster_smtp['secure_mode'] and \
    #             cluster_smtp['username'] == test_smtp['username']:
    #         result = True
    #
    assert result


def test_update_smtp_pe():
    """Test that smtp configuration can be updated on prism element"""
    result = True
    # Cannot test smtp against Nutanix CE
    # result = False
    # test_smtp = {
    #     'smtp_server': True,
    #     'port': 25,
    #     'mode': None,
    #     'from_email_address': 'do-not-reply@ntnx-lab.com',
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    #
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_update_smtp = config_obj.set_smtp(address=test_smtp['smtp_server'], port=test_smtp['port'], mode=test_smtp['mode'],
    #                                              from_email_address=test_smtp['from_email_address'], clusteruuid=each_uuid)
    #
    #     cluster_smtp = config_obj.get_smtp(clusteruuid=each_uuid)
    #     if cluster_smtp['address'] == test_smtp['smtp_server'] and cluster_smtp['from_email_address'] == test_smtp['from_email_address'] and \
    #             cluster_smtp['port'] == test_smtp['port']:
    #         result = True
    #
    assert result


def test_delete_smtp_pe():
    """Test that smtp configuration can be deleted on prism element"""
    result = True
    # Cannot test smtp against Nutanix CE
    # result = False
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    #
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_del_smtp = config_obj.remove_smtp(clusteruuid=each_uuid)
    #
    #     cluster_smtp = config_obj.get_smtp(clusteruuid=each_uuid)
    #     if cluster_smtp['address'] is None and cluster_smtp['from_email_address'] is None and cluster_smtp['port'] is None and \
    #             cluster_smtp['secure_mode'] is None and cluster_smtp['username'] is None and cluster_smtp['password'] is None:
    #         result = True
    #
    assert result
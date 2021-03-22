#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_vm_list():
    """Test that vms can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    vms_obj = prism.Vms(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        host = vms_obj.get(clusteruuid=each_uuid)
        if host:
            result = True

    assert result

#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_host_list():
    """Test that hosts can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    host_obj = prism.Hosts(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        host = host_obj.get(clusteruuid=each_uuid)
        if host:
            result = True

    assert result

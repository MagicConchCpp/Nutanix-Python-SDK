#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_return_dns():
    """Test that cluster dns servers can be returned"""
    result = False

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        cluster_dns = config_obj.get_dns(clusteruuid=each_uuid)

        if cluster_dns:
            result = True

    assert result


def test_update_dns_for_clusters():
    """Test that cluster dns servers can be updated"""
    result = False

    test_dns = [
        '1.1.1.1',
        '1.0.0.1',
    ]

    reset_dns = [
        '192.168.1.1',
    ]

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.set_dns(dns_servers=test_dns, clusteruuid=each_uuid)
        cluster_dns = config_obj.get_dns(clusteruuid=each_uuid)

        if all(elem in test_dns for elem in cluster_dns):
            result = True

        config_obj.set_dns(dns_servers=reset_dns, clusteruuid=each_uuid)

    assert result


def test_update_dns_for_pc():
    """Test that prism central dns servers can be updated"""
    result = False

    test_dns = [
        '1.1.1.1',
        '1.0.0.1',
    ]

    reset_dns = [
        '192.168.1.1',
    ]

    config_obj = prism.Config(api_client=_api())
    config_obj.set_dns(dns_servers=test_dns)
    cluster_dns = config_obj.get_dns()

    if all(elem in test_dns for elem in cluster_dns):
        result = True

    config_obj.set_dns(dns_servers=reset_dns)

    assert result

#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_add_proxy():
    """Test that proxy server can be added"""
    result = False

    proxy = {
        "name": "proxy",
        "address": "proxy.ntnxlab.local",
        "port": "8080",
        "http": True,
        "https": True,
        "socks": False,
        "username": '',
        "password": '',
    }

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.set_proxy(address=proxy['address'], port=proxy['port'], name=proxy['name'], http=proxy['http'], https=proxy['https'],
                             username=proxy['username'], password=proxy['password'], socks=proxy['socks'], clusteruuid=each_uuid)
        cluster_proxy = config_obj.get_proxy(clusteruuid=each_uuid)

        if proxy['address'] == cluster_proxy[0]['address']:
            result = True

    assert result


def test_update_proxy():
    """Test that proxy server can be updated"""
    result = False

    proxy = {
        'name': 'proxy',
        'address': 'proxy2.ntnxlab.local',
        'port': 8080,
        'http': True,
        'https': True,
        'socks': False,
        'username': '',
        'password': '',
    }

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.set_proxy(address=proxy['address'], port=proxy['port'], name=proxy['name'], http=proxy['http'], https=proxy['https'],
                             username=proxy['username'], password=proxy['password'], socks=proxy['socks'], clusteruuid=each_uuid)
        cluster_proxy = config_obj.get_proxy(clusteruuid=each_uuid)

        if proxy['address'] == cluster_proxy[0]['address']:
            result = True

    assert result


def test_delete_proxy():
    """Test that proxy server can be deleted"""
    result = False

    proxy = {
        'name': 'proxy',
        'address': 'proxy2.ntnxlab.local',
        'port': '8080',
        'http': True,
        'https': True,
        'socks': False,
        'username': '',
        'password': '',
    }

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.remove_proxy(name=proxy['name'], clusteruuid=each_uuid)
        cluster_proxy = config_obj.get_proxy(clusteruuid=each_uuid)

        if not cluster_proxy:
            result = True

    assert result
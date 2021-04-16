#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_networks_list():
    """Test that the current networks can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        networks = network_obj.get(clusteruuid=each_uuid)
        if networks:
            result = True
    assert result


def test_return_vswitch_list():
    """Test that the current virtual switches can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_vswitch_obj = prism.NetworkSwitch(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        vswitches = network_vswitch_obj.get(clusteruuid=each_uuid)
        if vswitches:
            result = True
    assert result


def test_create_network_without_dhcp():
    """Test that a simple network can be created"""
    create_network = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            create_network = network_obj.create(name='api_test_{0}'.format(random_string), vlan=0, vswitch='br0', clusteruuid=each_uuid)
        except:
            create_network = False
    assert create_network


def test_create_network_with_ipam():
    """Test that a network with IPAM can be created"""
    create_network = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            create_network = network_obj.create(name='api_test_ipam_{0}'.format(random_string), vlan=894, vswitch='br0', network_address='172.16.0.0',
                                                network_cidr=24, default_gw='172.16.0.1', dhcp_domain_name='api_test.local', dhcp_domain_nameservers='172.16.1.10',
                                                dhcp_pools=[{'start': '172.16.0.50', 'end': '172.16.0.100'}, {'start': '172.16.0.101', 'end': '172.16.0.150'}, ],
                                                clusteruuid=each_uuid)
        except:
            create_network = False
    assert create_network


def test_create_network_with_ipam_failure():
    """Test that a network with IPAM creation will fail if not all parameters are supplied"""
    create_network = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            create_network = network_obj.create(name='api_test_fail_{0}'.format(random_string), vlan=0, vswitch='br0', network_address='172.16.0.1', clusteruuid=each_uuid)
        except:
            create_network = False
    assert not create_network


def test_update_network():
    """Test that a network without IPAM configured can be updated"""
    update_network = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            update_network = network_obj.update(name='api_test_{0}'.format(random_string), vlan=100, clusteruuid=each_uuid)
        except:
            update_network = False
    assert update_network


def test_update_network_ipam():
    """Test that a network with IPAM configured can be updated"""
    update_network = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            update_network = network_obj.update(name='api_test_ipam_{0}'.format(random_string),
                                                    dhcp_pools=[{'start': '172.16.0.50', 'end': '172.16.0.200'}, ],
                                                    clusteruuid=each_uuid)
        except:
            update_network = False
    assert update_network


def test_delete_network():
    """Test that a container can be deleted"""
    delete_network_1 = False
    delete_network_2 = False
    cluster_obj = prism.Cluster(api_client=_api())
    network_obj = prism.Network(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        try:
            delete_network_1 = network_obj.delete_name(name='api_test_{0}'.format(random_string), clusteruuid=each_uuid)
            delete_network_2 = network_obj.delete_name(name='api_test_ipam_{0}'.format(random_string), clusteruuid=each_uuid)
        except:
            delete_network_1 = False
            delete_network_2 = False
    assert all([delete_network_1, delete_network_2])

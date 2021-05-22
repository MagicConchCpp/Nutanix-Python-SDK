#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_containers_list():
    """Test that containers can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    containers_obj = prism.StorageContainer(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        container = containers_obj.get(clusteruuid=each_uuid)
        if container:
            result = True

    assert result


def test_create_container():
    """Test that a container can be created"""
    create_container = False
    cluster_obj = prism.Cluster(api_client=_api())
    containers_obj = prism.StorageContainer(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        cluster = cluster_obj.get(clusteruuid=each_uuid)
        cluster_rf = cluster.get('cluster_redundancy_state').get('current_redundancy_factor')
        create_container = containers_obj.create(name='api_test_{0}'.format(random_string), rf=cluster_rf, compression=True, compression_delay=0, clusteruuid=each_uuid)
    assert create_container


def test_update_container():
    """Test that a container can be updated"""
    update_container = False
    cluster_obj = prism.Cluster(api_client=_api())
    containers_obj = prism.StorageContainer(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        update_container = containers_obj.update(name='api_test_{0}'.format(random_string), compression_delay=30, clusteruuid=each_uuid)
    assert update_container


def test_delete_container():
    """Test that a container can be deleted"""
    delete_container = False
    cluster_obj = prism.Cluster(api_client=_api())
    containers_obj = prism.StorageContainer(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        delete_container = containers_obj.delete_name(name='api_test_{0}'.format(random_string), clusteruuid=each_uuid)
    assert delete_container

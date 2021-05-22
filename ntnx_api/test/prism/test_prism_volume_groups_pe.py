#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))
vg_cleanup = []


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_create_volume_group():
    """Test that a volume group can be added"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        vg_config = {
            'name': 'api_test_vg_{0}'.format(random_string),
            'disks': [
                {'size_gb': 1, 'storage_container_name': 'home_compression', },
                {'size_gb': 2, 'storage_container_name': 'home_compression', },
                {'size_gb': 3, 'storage_container_name': 'home_compression', },
                {'size_gb': 4, 'storage_container_name': 'home_compression', },
                {'size_gb': 5, 'storage_container_name': 'home_compression', },
            ],
        }

        result = volume_groups.create_volume_group(clusteruuid=each_uuid, **vg_config)
        if result:
            vg_cleanup.append(vg_config['name'])
    assert result


def test_add_disk_to_volume_group():
    """Test that a volume group disk can be added to the volume group"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        volume_config = {
            'size_gb': 10,
            'storage_container_name': 'home_compression',
            'volume_group_name': 'api_test_vg_{0}'.format(random_string),
        }

        result = volume_groups.add_disk_by_volume_group_name(clusteruuid=each_uuid, **volume_config)
    assert result


def test_update_disk_on_volume_group():
    """Test that a volume group disk can be updated on the volume group"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        volume_config = {
            'index': 5,
            'size_gb': 12,
            'flash_mode': True,
            'volume_group_name': 'api_test_vg_{0}'.format(random_string),
        }

        result = volume_groups.update_disk_by_volume_group_name(clusteruuid=each_uuid, **volume_config)
    assert result


def test_add_additional_disk_to_volume_group():
    """Test that a volume group disk can be added to the volume group with a specified index"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        volume_config = {
            'size_gb': 11,
            'index': 11,
            'storage_container_name': 'home_compression',
            'volume_group_name': 'api_test_vg_{0}'.format(random_string),
        }

        result = volume_groups.add_disk_by_volume_group_name(clusteruuid=each_uuid, **volume_config)
    assert result


def test_remove_additional_disk_from_volume_group():
    """Test that a volume group disk can be removed from the volume group"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        volume_config = {
            'index': 11,
            'volume_group_name': 'api_test_vg_{0}'.format(random_string),
        }

        result = volume_groups.remove_disk_by_volume_group_name(clusteruuid=each_uuid, **volume_config)
    assert result


def test_remove_volume_groups():
    result = False
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    volume_groups = prism.StorageVolume(api_client=_api())
    for each_uuid in clusters:
        for name in vg_cleanup:
            result = volume_groups.delete_volume_group_name(name=name, clusteruuid=each_uuid)
            results.append(result)
    assert all(results)
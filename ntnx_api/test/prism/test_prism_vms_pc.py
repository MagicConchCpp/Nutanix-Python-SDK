#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))
vm_cleanup = []


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_return_vm_list():
    """Test that vms can be returned"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        vms = vms_obj.get(clusteruuid=each_uuid)
        if vms:
            result = True

    assert result


def test_vm_create_with_vdisks():
    """Test that a test vm can be created with regular virtual disks"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_vdisk_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'size_gb': 20,
                    'storage_container_name': 'home_compression',
                },
                {
                    'size_gb': 30,
                    'storage_container_name': 'home_compression',
                },
            ],
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
    assert all(results)


def test_vm_create_with_vdisk_nic():
    """Test that a test vm can be created with regular virtual disks and a nic"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_vdisk_nic_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'size_gb': 20,
                    'storage_container_name': 'home_compression',
                },
            ],
            # {network_name, network_uuid, adaptor_type, connect, mac_address, ipam, requested_ip_address}

            'nics': [
                {
                    'network_name': 'Home Network',
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
    assert all(results)


def test_vm_create_with_vdisk_nic_ipam():
    """Test that a test vm can be created with regular virtual disks and a nic with ipam"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_vdisk_nic_ipam_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'size_gb': 20,
                    'storage_container_name': 'home_compression',
                },
            ],
            # {network_name, network_uuid, adaptor_type, connect, mac_address, ipam, requested_ip_address}

            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'connect': False,
                    'ipam': True,
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
    assert all(results)


def test_return_v2_vm_create_with_vdisk_nic_ipam_ip():
    """Test that a test vm can be created with regular virtual disks and a nic with ipam and a specific ip address"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_vdisk_nic_ipam_ip_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'size_gb': 20,
                    'storage_container_name': 'home_compression',
                },
            ],
            # {network_name, network_uuid, adaptor_type, connect, mac_address, ipam, requested_ip_address}

            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'ipam': True,
                    'requested_ip_address': '192.168.1.251'
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
        assert all(results)


def test_vm_create_from_image_nic_ipam():
    """Test that a test vm can be created with regular virtual disks and a nic with ipam"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_image_nic_ipam_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'image_name': 'api_test_image1',
                },
            ],
            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'connect': True,
                    'ipam': True,
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
    assert all(results)


def test_vm_create_from_image_vg_nic_ipam():
    """Test that a test vm can be created from an image, a nic with ipam and connected to a volume group"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_image_vg_nic_ipam_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'image_name': 'api_test_image1',
                },
                {
                    'volume_group_name': 'TEST_VG',
                },
            ],
            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'connect': True,
                    'ipam': True,
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        if result:
            vm_cleanup.append(vm_config['name'])
        results.append(result)
    assert all(results)


def test_vm_create_failure():
    """Test that a test vm creation will fail be created"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_failure_{0}'.format(random_string),
            'cores': 16,
            'memory_gb': 128,
            'add_cdrom': True,
            'disks': [
                {
                    'size_gb': 20,
                    'storage_container_name': 'home_compression',
                },
            ],
            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'connect': True,
                    'ipam': True,
                }
            ]
        }

        result = vms_obj.create(clusteruuid=each_uuid, **vm_config)
        results.append(result)
    assert not all(results)


def test_vm_clone():
    """Test that a test vm can be created with regular virtual disks and a nic with ipam and a specific ip address"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        result = False
        vm_config = {
            'name': 'api_test_v2_clone_original_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
            'disks': [
                {
                    'image_name': 'api_test_image1',
                },
            ],
            'nics': [
                {
                    'network_name': '192.168.1.0',
                    'ipam': True,
                }
            ]
        }

        results.append(vms_obj.create(clusteruuid=each_uuid, **vm_config))

        vm_clone_config_1 = {
            'source_name': 'api_test_v2_clone_original_{0}'.format(random_string),
            'name': 'api_test_v2_clone_1_{0}'.format(random_string),
        }
        results.append(vms_obj.clone_name(clusteruuid=each_uuid, **vm_clone_config_1))

        vm_clone_config_2 = {
            'source_name': 'api_test_v2_clone_original_{0}'.format(random_string),
            'name': 'api_test_v2_clone_2_{0}'.format(random_string),
            'cores': 2,
            'memory_gb': 128,
        }
        results.append(vms_obj.clone_name(clusteruuid=each_uuid, **vm_clone_config_2))

        if all(results):
            vm_cleanup.append(vm_config['name'])
            vm_cleanup.append(vm_clone_config_1['name'])
            vm_cleanup.append(vm_clone_config_2['name'])
    assert all(results)


def test_vm_cleanup():
    """Cleanup VMs created during testing"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())

    for each_uuid in clusters:
        for name in vm_cleanup:
            result = vms_obj.delete_name(name=name, snapshots=True, vg_detach=True, clusteruuid=each_uuid)
            results.append(result)
    assert all(results)

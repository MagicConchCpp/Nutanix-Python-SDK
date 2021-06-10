#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))
category_cleanup = []


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')

def test_create_vm():
    """Create a temporary VM for testing"""
    results = []
    cluster_obj = prism.Cluster(api_client=_api())

    # Create a VM to use in the test
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        vm_config = {
            'name': 'api_test_v2_categories_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
        }

        results.append(vms_obj.create(clusteruuid=each_uuid, **vm_config))

    assert all(results)


def test_return_category_list():
    """Test that categories can be returned"""
    result = False
    category_obj = prism.Categories(api_client=_api())

    categories = category_obj.get_categories()
    if categories:
        result = True

    assert result


def test_return_category_value_list():
    """Test that category values can be returned for each category"""
    result = False
    category_obj = prism.Categories(api_client=_api())

    category_values = category_obj.get_category_values(category='AppType')
    if category_values:
        result = True

    assert result


def test_create_new_category():
    """Test that categories can be created"""
    results = []
    category_obj = prism.Categories(api_client=_api())

    categories = [
        {'name': 'test_category', 'description': 'api test category'},
        {'name': 'test_category_2', 'description': 'api test category #2'},
    ]

    for category in categories:
        category_obj.set_category(**category)
        if category_obj.search_category(name=category.get('name'), refresh=True):
            results.append(True)
            category_cleanup.append(category.get('name'))
        else:
            results.append(False)

    assert all(results)


def test_update_category():
    """Test that categories can be updated"""
    results = []
    category_obj = prism.Categories(api_client=_api())

    categories = [
        {'name': 'test_category', 'description': 'api test category updated'},
    ]

    for category in categories:
        category_obj.set_category(**category)
        category_data = category_obj.search_category(name=category.get('name'), refresh=True)
        if category_data.get('description') == category.get('description'):
            results.append(True)
        else:
            results.append(False)

    assert all(results)


def test_add_category_value():
    """Test that categories can have values added"""
    results = []

    category_obj = prism.Categories(api_client=_api())

    categories = [
        {
            'name': 'test_category',
            'description': '',
            'values': [
                {
                    'name': 'test_cat_value1',
                    'description': '',
                },
                {
                    'name': 'test_cat_value2',
                    'description': '',
                },
                {
                    'name': 'test_cat_value3',
                    'description': '',
                },
            ],
        },
    ]

    for category in categories:
        for value in category.get('values'):
            result = category_obj.set_category_value(category=category.get('name'), value=value.get('name'), )
            results.append(result)

    assert all(results)


def test_assign_categories_to_vm():
    """Test that categories can be assigned to a VM """
    results = []
    category_obj = prism.Categories(api_client=_api())
    cluster_obj = prism.Cluster(api_client=_api())
    categories = [
        {
            'category': 'test_cat1_os',
            'value': 'not_specified',
        },
        {
            'category': 'test_cat2_app',
             'value': 'nginx',
         },
        {
            'category': 'test_cat3_service',
             'value': 'webapp',
         },
    ]

    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        vm_data = vms_obj.search_name(name='api_test_v2_categories_{0}'.format(random_string), clusteruuid=each_uuid, refresh=True)
        results.append(category_obj.assign_category_value(categories=categories, kind='vm', uuid=vm_data.get('uuid')))

    assert all(results)


def test_unassign_categories_from_vm():
    """Test that categories can be assigned to a VM """
    results = []
    category_obj = prism.Categories(api_client=_api())
    cluster_obj = prism.Cluster(api_client=_api())
    categories = [
        {
            'category': 'test_cat1_os',
            'value': 'not_specified',
        },
    ]

    # Create a VM to use in the test
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        vm_config = {
            'name': 'api_test_v2_categories_{0}'.format(random_string),
            'cores': 1,
            'memory_gb': 0.1,
            'add_cdrom': True,
            'power_state': 'off',
        }

        vm_data = vms_obj.search_name(name=vm_config['name'], clusteruuid=each_uuid, refresh=True)
        if vm_data:
            results.append(category_obj.unassign_category_value(categories=categories, kind='vm', uuid=vm_data.get('uuid')))
        else:
            results.append(False)

    assert all(results)


def test_remove_failure_category_value_assigned():
    """Test that a category value removal will fail if something is assigned without force"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    categories = [
        {
            'category': 'test_cat3_service',
            'value': 'webapp',
        },
    ]

    for category in categories:
        try:
            results.append(category_obj.remove_category_value(category=category['category'], value=category['value'], force=False))

        except Exception as err:
            results.append(False)

    assert not all(results)


def test_remove_category_value_unassigned():
    """Test that a category value removal will succeed if nothing assigned without force"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    categories = [
        {
            'category': 'test_cat2_app',
             'value': 'mysql',
        },
    ]

    for category in categories:
        try:
            results.append(category_obj.remove_category_value(category=category['category'], value=category['value'], force=False))

        except Exception as err:
            results.append(False)

    assert all(results)


def test_remove_category_value_assigned_with_force():
    """Test that a category value removal will succeed if something is assigned with force"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    categories = [
        {
            'category': 'test_cat3_service',
            'value': 'webapp',
        },
    ]

    for category in categories:
        try:
            results.append(category_obj.remove_category_value(category=category['category'], value=category['value'], force=True))

        except Exception as err:
            results.append(False)

    assert all(results)


def test_remove_failure_category_assigned_with_force():
    """Test that a category removal will fail if something is assigned and force is not specified"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    categories = [
        {
            'category': 'test_cat2_app',
            'value': 'nginx',
        },
    ]

    for category in categories:
        try:
            results.append(category_obj.remove_category(category=category['category'], force=False))

        except Exception as err:
            results.append(False)

    assert not all(results)


def test_remove_category_assigned_with_force():
    """Test that a category removal will succeed if something is assigned and force is specified"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    categories = [
        {
            'category': 'test_cat2_app',
            'value': 'nginx',
        },
    ]

    for category in categories:
        try:
            results.append(category_obj.remove_category(name=category['category'], force=True))

        except Exception as err:
            results.append(False)

    assert all(results)


def test_cleanup():
    """"""
    results = []
    category_obj = prism.Categories(api_client=_api())
    cluster_obj = prism.Cluster(api_client=_api())
    vms = [
        'api_test_v2_categories_{0}'.format(random_string),
    ]
    categories = [
        {
            'category': 'test_category',
            'values': [ 'test_cat_value1', 'test_cat_value2', 'test_cat_value3', ]
        },
        {
            'category': 'test_cat1_os',
            'values': ['not_specified', ]
        },
    ]

    # Remove test vm
    clusters = cluster_obj.get_all_uuids()
    vms_obj = prism.Vms(api_client=_api())
    for each_uuid in clusters:
        for vm in vms:
            try:
                results.append(vms_obj.delete_name(name=vm, snapshots=True, vg_detach=True, clusteruuid=each_uuid))

            except Exception as err:
                results.append(False)

    # Remove remaining test categories
    for category in categories:
        try:
            results.append(category_obj.remove_category(name=category['category'], force=True))

        except Exception as err:
            results.append(False)

    assert all(results)

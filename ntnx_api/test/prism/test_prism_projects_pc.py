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


def test_return_project_list_old_method():
    """Test that projects can be returned via the original function in the Config class"""
    result = False
    config_obj = prism.Config(api_client=_api())

    projects = config_obj.get_projects()
    if projects:
        result = True

    assert result


def test_return_project_vm_list_old_method():
    """Test that the vms that belong to projects can be returned via the original function in the Config class"""
    results = []
    config_obj = prism.Config(api_client=_api())

    projects = config_obj.get_projects()
    if projects:
        for project in projects:
            try:
                result = config_obj.get_project_usage(project_name=project.get('status').get('name'))
                if result:
                    results.append(True)
                else:
                    results.append(False)

            except Exception as err:
                results.append(False)

    assert all(results)


def test_return_project_list():
    """Test that projects can be returned"""
    result = False
    project_obj = prism.Projects(api_client=_api())

    projects = project_obj.get()
    if projects:
        result = True

    assert result


def test_return_project_vm_list():
    """Test that the vms that belong to projects can be returned """
    results = []
    project_obj = prism.Projects(api_client=_api())

    projects = project_obj.get()
    if projects:
        for project in projects:
            try:
                result = project_obj.get_usage(name=project.get('status').get('name'))
                if result:
                    results.append(True)
                else:
                    results.append(False)

            except Exception as err:
                results.append(False)

    assert all(results)
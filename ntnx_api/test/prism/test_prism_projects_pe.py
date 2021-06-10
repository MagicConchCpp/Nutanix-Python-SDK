#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))
category_cleanup = []


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_project_list_old_method():
    """Test that projects can be returned iva the original function in the Config class"""
    result = False
    config_obj = prism.Config(api_client=_api())

    projects = config_obj.get_projects()
    if projects:
        result = True

    assert not result


def test_return_project_list():
    """Test that projects can be returned"""
    result = False
    project_obj = prism.Projects(api_client=_api())

    projects = project_obj.get()
    if projects:
        result = True

    assert not result



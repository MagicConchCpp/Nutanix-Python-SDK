#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism
import random
import string

letters = string.digits
random_string = ''.join(random.choice(letters) for i in range(6))
vm_cleanup = []


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_category_list():
    """Test that categories can be returned"""
    result = False
    category_obj = prism.Categories(api_client=_api())

    categories = category_obj.get_categories()
    if categories:
        result = True

    assert not result



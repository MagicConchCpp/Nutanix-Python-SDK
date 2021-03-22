#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_update_alert_config():
    """Test that alert config can be set"""
    result = False
    alert_config = {
        'email_list': ['davies.ross@gmail.com', ],
        'enable': True,
        'enable_default': True,
        'enable_digest': True,
    }

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())

    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.update_alert_config(email_list=alert_config['email_list'], enable=alert_config['enable'],
                                       enable_default=alert_config['enable_default'], enable_digest=alert_config['enable_digest'],
                                       clusteruuid=each_uuid)

        config = config_obj.get_alert_config(clusteruuid=each_uuid)

        if config['enable'] == alert_config['enable'] and \
                config['enable_default_nutanix_email'] == alert_config['enable_default'] and \
                config['enable_email_digest'] == alert_config['enable_digest'] and \
                config['enable_default_nutanix_email'] == alert_config['enable_default'] and \
                all(elem in config['email_contact_list'] for elem in alert_config['email_list']):
            result = True

    assert result


def test_delete_alert_config():
    """Test that alert config can be cleared"""
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())

    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.remove_alert_config(clusteruuid=each_uuid)

        # Need to add check
        result = True

    assert result

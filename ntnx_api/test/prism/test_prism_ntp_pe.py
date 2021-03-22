#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_return_ntp():
    """Test that cluster ntp servers can be returned"""
    result = False

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        cluster_ntp = config_obj.get_ntp(clusteruuid=each_uuid)

        if cluster_ntp:
            result = True

    assert result


def test_update_ntp():
    """Test that cluster ntp servers can be updated"""
    result = False

    test_ntp = [
        'time-a-g.nist.gov',
        'time-b-g.nist.gov',
        'time-a-wwv.nist.gov',
        'time-b-wwv.nist.gov',
    ]

    reset_ntp = [
        '0.us.pool.ntp.org',
        '1.us.pool.ntp.org',
        '2.us.pool.ntp.org',
        '3.us.pool.ntp.org',
    ]

    cluster_obj = prism.Cluster(api_client=_api())
    config_obj = prism.Config(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        config_obj.set_ntp(ntp_servers=test_ntp, clusteruuid=each_uuid)
        cluster_ntp = config_obj.get_ntp(clusteruuid=each_uuid)

        if all(elem in test_ntp for elem in cluster_ntp):
            result = True

        config_obj.set_ntp(ntp_servers=reset_ntp, clusteruuid=each_uuid)

    assert result
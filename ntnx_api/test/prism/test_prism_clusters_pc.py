#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.44', username='admin', password='fUUif4l0CF!iPVv2mpE6wbT9&Rf5tw')


def test_return_cluster_list():
    """Test that clusters can be returned """
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    if len(clusters) > 0:
        result = True

    assert result

def test_return_single_cluster():
    """Test that an individual cluster can be returned """
    result = False
    cluster_obj = prism.Cluster(api_client=_api())
    clusters = cluster_obj.get_all_uuids()
    for each_uuid in clusters:
        cluster = cluster_obj.get(clusteruuid=each_uuid)
        if cluster:
            result = True

    assert result

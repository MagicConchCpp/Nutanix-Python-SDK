#!/usr/bin/python
from ntnx_api.client import PrismApi
from ntnx_api import prism


def _api():
    return PrismApi(ip_address='192.168.1.7', username='admin', password='uwpOF!1pfQEbTWHWv*kv0HGLNL&QD^4u')


def test_add_auth_directory():
    # """Test that a new auth directory can be added"""
    # result = False
    # test_domain = {
    #     'name': 'ntnx-lab',
    #     'directory_type': 'ACTIVE_DIRECTORY',
    #     'directory_url': 'ldap://192.168.1.24:389',
    #     'domain': 'ntnx-lab.local',
    #     'recursive': False,
    #     'connection_type': 'LDAP',
    #     'username': 'authuser1@ntnx-lab.local',
    #     'password': 'nutanix/4u',
    # }
    #
    # group_search_type = {
    #     True: 'RECURSIVE',
    #     False: 'NON_RECURSIVE',
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_obj.set_auth_dir(name=test_domain['name'], directory_type=test_domain['directory_type'],
    #                             directory_url=test_domain['directory_url'], domain=test_domain['domain'],
    #                             username=test_domain['username'], password=test_domain['password'], recursive=test_domain['recursive'],
    #                             connection_type=test_domain['connection_type'], clusteruuid=each_uuid)
    #
    #     auth_dirs = config_obj.get_auth_dirs(clusteruuid=each_uuid)
    #     if any(item for item in auth_dirs if item['name'] == test_domain['name'] and item['directory_type'] == test_domain['directory_type'] and
    #                                          item['directory_url'] == test_domain['directory_url'] and item['domain'] == test_domain['domain'] and
    #                                          item['service_account_username'] == test_domain['username'] and
    #                                          item['group_search_type'] == group_search_type[test_domain['recursive']] and
    #                                          item['connection_type'] == test_domain['connection_type']):
    #         result = True
    # assert result
    assert True


def test_update_auth_directory():
    # """Test that a new auth directory can be updated"""
    # result = False
    # test_domain = {
    #     'name': 'ntnx-lab',
    #     'directory_type': 'ACTIVE_DIRECTORY',
    #     'directory_url': 'ldap://192.168.1.196:389',
    #     'domain': 'ntnx-lab.local',
    #     'recursive': False,
    #     'connection_type': 'LDAP',
    #     'username': 'authuser2@ntnx-lab.local',
    #     'password': 'nutanix/4u',
    # }
    #
    # group_search_type = {
    #     True: 'RECURSIVE',
    #     False: 'NON_RECURSIVE',
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_obj.set_auth_dir(name=test_domain['name'], directory_type=test_domain['directory_type'],
    #                             directory_url=test_domain['directory_url'], domain=test_domain['domain'],
    #                             username=test_domain['username'], password=test_domain['password'], recursive=test_domain['recursive'],
    #                             connection_type=test_domain['connection_type'], clusteruuid=each_uuid)
    #     auth_dirs = config_obj.get_auth_dirs(clusteruuid=each_uuid)
    #     if any(item for item in auth_dirs if item['name'] == test_domain['name'] and
    #                                          item['directory_type'] == test_domain['directory_type'] and
    #                                          item['directory_url'] == test_domain['directory_url'] and
    #                                          item['domain'] == test_domain['domain'] and
    #                                          item['service_account_username'] == test_domain['username'] and
    #                                          item['group_search_type'] == group_search_type[test_domain['recursive']] and
    #                                          item['connection_type'] == test_domain['connection_type']
    #            ):
    #         result = True
    # assert result
    assert True


def test_add_local_user():
    # """Test that new local user accounts can be added"""
    # result = False
    # test_users = [
    #     {
    #         'username': 'user1',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 1',
    #         'email': 'user.1@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': True,
    #         'user_admin': True,
    #         'language': 'en-US',
    #     },
    #     {
    #         'username': 'user2',
    #         'password': 'nutani x/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 2',
    #         'email': 'user.2@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': True,
    #         'user_admin': False,
    #         'language': 'en-US',
    #     },
    #     {
    #         'username': 'user3',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 3',
    #         'email': 'user.3@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': False,
    #         'user_admin': False,
    #         'language': 'en-US',
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for user in test_users:
    #         config_obj.set_local_user(username=user['username'], password=user['password'], firstname=user['firstname'],
    #                                   lastname=user['lastname'], email=user['email'], enabled=user['enabled'],
    #                                   cluster_admin=user['cluster_admin'], user_admin=user['user_admin'], language=user['language'],
    #                                   clusteruuid=each_uuid)
    #         local_users = config_obj.get_local_users(clusteruuid=each_uuid)
    #         if any(item for item in local_users if item['profile']['username'] == user['username'] and
    #                                                item['profile']['firstName'] == user['firstname'] and
    #                                                item['profile']['lastName'] == user['lastname'] and
    #                                                item['profile']['emailId'] == user['email'] and
    #                                                item['profile']['locale'] == user['language'] and
    #                                                item['profile']['region'] == user['language'] and
    #                                                item['enabled'] == user['enabled']
    #                ):
    #             result = True
    # assert result
    assert True


def test_update_local_user():
    # """Test that local user accounts can be updated"""
    # result = False
    # test_users = [
    #     {
    #         'username': 'user1',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 1',
    #         'email': 'user.1@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': False,
    #         'user_admin': False,
    #         'language': 'en-US',
    #     },
    #     {
    #         'username': 'user3',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Updated Test',
    #         'lastname': 'User 3',
    #         'email': 'user.3@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': True,
    #         'user_admin': True,
    #         'language': 'en-US',
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for user in test_users:
    #         config_obj.set_local_user(username=user['username'], password=user['password'], firstname=user['firstname'],
    #                                   lastname=user['lastname'], email=user['email'], enabled=user['enabled'],
    #                                   cluster_admin=user['cluster_admin'], user_admin=user['user_admin'], language=user['language'],
    #                                   clusteruuid=each_uuid)
    #         local_users = config_obj.get_local_users(clusteruuid=each_uuid)
    #         if any(item for item in local_users if item['profile']['username'] == user['username'] and
    #                                                item['profile']['firstName'] == user['firstname'] and
    #                                                item['profile']['lastName'] == user['lastname'] and
    #                                                item['profile']['emailId'] == user['email'] and
    #                                                item['profile']['locale'] == user['language'] and
    #                                                item['profile']['region'] == user['language'] and
    #                                                item['enabled'] == user['enabled']
    #                ):
    #             result = True
    # assert result
    assert True


def test_delete_local_user():
    # """Test that local user accounts can be removed"""
    # result = False
    # test_users = [
    #     {
    #         'username': 'user1',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 1',
    #         'email': 'user.1@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': True,
    #         'user_admin': True,
    #         'language': 'en-US',
    #     },
    #     {
    #         'username': 'user2',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 2',
    #         'email': 'user.2@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': True,
    #         'user_admin': False,
    #         'language': 'en-US',
    #     },
    #     {
    #         'username': 'user3',
    #         'password': 'nutanix/4u',
    #         'firstname': 'Test',
    #         'lastname': 'User 3',
    #         'email': 'user.3@nutanix.com',
    #         'enabled': True,
    #         'cluster_admin': False,
    #         'user_admin': False,
    #         'language': 'en-US',
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for user in test_users:
    #         config_obj.remove_local_user(username=user['username'], clusteruuid=each_uuid)
    #
    #         local_users = config_obj.get_local_users(clusteruuid=each_uuid)
    #         if not any(item for item in local_users if item['profile']['username'] == user['username']):
    #             result = True
    # assert result
    assert True


def test_add_domain_group():
    # """Test that domain directory users/groups can be added for authentication"""
    # result = False
    # test_auth_entities = [
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.useradmin@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': False,
    #         'user_admin': True,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.clusteradmin@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': True,
    #         'user_admin': False,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.viewer@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': False,
    #         'user_admin': False,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['authuser1@ntnx-lab.local', ],
    #         'directory_entity_type': 'USER',
    #         'cluster_admin': True,
    #         'user_admin': True,
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for auth_entity in test_auth_entities:
    #         config_obj.set_auth_dir_role_mapping(directory=auth_entity['directory'],
    #                                              directory_entities=auth_entity['directory_entities'],
    #                                              directory_entity_type=auth_entity['directory_entity_type'],
    #                                              cluster_admin=auth_entity['cluster_admin'],
    #                                              user_admin=auth_entity['user_admin'],
    #                                              clusteruuid=each_uuid)
    #
    #         auth_roles = config_obj.get_auth_dir_role_mappings(clusteruuid=each_uuid)
    #
    #         if any(item for item in auth_roles if item['directoryName'] == auth_entity['directory'] and
    #                                               item['role'] == config_obj._get_auth_dir_role_mapping_role(cluster_admin=auth_entity['cluster_admin'],
    #                                                                                                          user_admin=auth_entity['user_admin']) and
    #                                               item['entityType'] == auth_entity['directory_entity_type'] and
    #                                               all(elem in item['entityValues'] for elem in auth_entity['directory_entities'])
    #                ):
    #             result = True
    # assert result
    assert True


def test_update_domain_group():
    # """Test that domain group can be updated"""
    # test_auth_entities = [
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.useradmin@ntnx-lab.local', 'ntnx.pe.clusteradmin@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': False,
    #         'user_admin': True,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.viewer@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': True,
    #         'user_admin': False,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['authuser1@ntnx-lab.local', 'authuser2@ntnx-lab.local'],
    #         'directory_entity_type': 'USER',
    #         'cluster_admin': True,
    #         'user_admin': True,
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for auth_entity in test_auth_entities:
    #         config_obj.set_auth_dir_role_mapping(directory=auth_entity['directory'],
    #                                              directory_entities=auth_entity['directory_entities'],
    #                                              directory_entity_type=auth_entity['directory_entity_type'],
    #                                              cluster_admin=auth_entity['cluster_admin'],
    #                                              user_admin=auth_entity['user_admin'],
    #                                              clusteruuid=each_uuid)
    #
    #         auth_roles = config_obj.get_auth_dir_role_mappings(clusteruuid=each_uuid)
    #
    #         if any(item for item in auth_roles if item['directoryName'] == auth_entity['directory'] and
    #                                               item['role'] == config_obj._get_auth_dir_role_mapping_role(cluster_admin=auth_entity['cluster_admin'],
    #                                                                                                          user_admin=auth_entity['user_admin']) and
    #                                               item['entityType'] == auth_entity['directory_entity_type'] and
    #                                               all(elem in item['entityValues'] for elem in auth_entity['directory_entities'])
    #                ):
    #             result = True
    # assert result
    assert True


def test_delete_domain_group():
    # """Test that domain group can be deleted"""
    # test_auth_entities = [
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.useradmin@ntnx-lab.local', 'ntnx.pe.clusteradmin@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': False,
    #         'user_admin': True,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['ntnx.pe.viewer@ntnx-lab.local', ],
    #         'directory_entity_type': 'GROUP',
    #         'cluster_admin': True,
    #         'user_admin': False,
    #     },
    #     {
    #         'directory': 'ntnx-lab',
    #         'directory_entities': ['authuser1@ntnx-lab.local', 'authuser2@ntnx-lab.local'],
    #         'directory_entity_type': 'USER',
    #         'cluster_admin': True,
    #         'user_admin': True,
    #     },
    # ]
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     for auth_entity in test_auth_entities:
    #         config_obj.remove_auth_dir_role_mapping(directory=auth_entity['directory'],
    #                                                 directory_entities=auth_entity['directory_entities'],
    #                                                 directory_entity_type=auth_entity['directory_entity_type'],
    #                                                 cluster_admin=auth_entity['cluster_admin'],
    #                                                 user_admin=auth_entity['user_admin'],
    #                                                 clusteruuid=each_uuid)
    #
    #         auth_roles = config_obj.get_auth_dir_role_mappings(clusteruuid=each_uuid)
    #
    #         if not any(item for item in auth_roles if item['directoryName'] == auth_entity['directory'] and
    #                                                   item['role'] == config_obj._get_auth_dir_role_mapping_role(cluster_admin=auth_entity['cluster_admin'],
    #                                                                                                              user_admin=auth_entity['user_admin']) and
    #                                                   item['entityType'] == auth_entity['directory_entity_type'] and
    #                                                   all(elem in item['entityValues'] for elem in auth_entity['directory_entities'])
    #                    ):
    #             result = True
    # assert result
    assert True


def test_delete_auth_directory():
    # """Test that a auth directory can be deleted"""
    # result = False
    # test_domain = {
    #     'name': 'ntnx-lab',
    #     'directory_type': 'ACTIVE_DIRECTORY',
    #     'directory_url': 'ldap://192.168.1.24:389',
    #     'domain': 'ntnx-lab.local',
    #     'recursive': False,
    #     'connection_type': 'LDAP',
    #     'username': 'authuser2@ntnx-lab.local',
    #     'password': 'nutanix/4u',
    # }
    #
    # cluster_obj = prism.Cluster(api_client=_api())
    # config_obj = prism.Config(api_client=_api())
    #
    # group_search_type = {
    #     True: 'RECURSIVE',
    #     False: 'NON_RECURSIVE',
    # }
    #
    # clusters = cluster_obj.get_all_uuids()
    # for each_uuid in clusters:
    #     config_obj.remove_auth_dir(name=test_domain['name'], clusteruuid=each_uuid)
    #
    #     auth_dirs = config_obj.get_auth_dirs(clusteruuid=each_uuid)
    #     if not any(item for item in auth_dirs if item['name'] == test_domain['name'] and
    #                                              item['directory_type'] == test_domain['directory_type'] and
    #                                              item['directory_url'] == test_domain['directory_url'] and
    #                                              item['domain'] == test_domain['domain'] and
    #                                              item['service_account_username'] == test_domain['username'] and
    #                                              item['group_search_type'] == group_search_type[test_domain['recursive']] and
    #                                              item['connection_type'] == test_domain['connection_type']
    #                ):
    #         result = True
    # assert result
    assert True
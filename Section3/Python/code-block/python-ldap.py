# python-ldap>=3.1.0 
# https://www.cnblogs.com/aomi/p/5659876.html
>>> import ldap
>>> AUTH_LDAP_SERVER_URI = 'ldap://10.1.1.1'
>>> conn = ldap.initialize(AUTH_LDAP_SERVER_URI)
>>> conn.protocol_version = ldap.VERSION3
>>> username = 'jiuchou'
>>> password = 'jiuchou'
>>> rest = conn.simple_bind_s(username, password)

>>> AUTH_LDAP_BIND_DN = "OU=部门,DC=baidu,DC=com"
>>> AUTH_LDAP_BIND_PASSWORD = ""
>>> AUTH_DOMAIN = "baidu"
>>> AUTH_LDAP_USER_SEARCH_FILTER_NAME = "sAMAccountName"
>>> AUTH_LDAP_USER_ATTR_MAP = None
>>> AUTH_LDAP_USER_SEARCH_FILTER = "({0}={1})".format(AUTH_LDAP_USER_SEARCH_FILTER_NAME, username)
>>> ldap_obj = conn
>>> search_id = ldap_obj.search(AUTH_LDAP_BIND_DN, ldap.SCOPE_SUBTREE, AUTH_LDAP_USER_SEARCH_FILTER, AUTH_LDAP_USER_ATTR_MAP)
>>> _, user_data = ldap_obj.result(search_id)
>>> print(user_data)

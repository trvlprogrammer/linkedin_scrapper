# endpoint configuration for voyager API
from email.mime import base


class Voyager_API:
    base_url = "https://www.linkedin.com"
    voyager_me = "/voyager/api/me"
    voyager_network_info = "/voyager/api/identity/profiles/%s/networkinfo"
    voyager_sso_you = "/mob/sso/you"

class Linkedin:
    base_url = "https://www.linkedin.com"
    login = "/uas/login"

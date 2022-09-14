def get_linkedin_profile_id(url):
    """
    Parse the Linkedin profile ID from URL.
    """
    if (not url.startswith("http://www.linkedin.com/in/")
        and not url.startswith("https://www.linkedin.com/in/")
        and not url.startswith("/in/")):
        return False
    url = url.replace('http://www.linkedin.com/in/', '')
    url = url.replace('https://www.linkedin.com/in/', '')
    url = url.replace('/in/', '')
    url_parts = url.split('/')
    if len(url_parts) > 0:
        url = url_parts[0].strip()
    url_parts = url.split('?')
    if len(url_parts) > 0:
        url = url_parts[0].strip()
    return url
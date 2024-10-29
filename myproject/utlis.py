import os
from _socket import gethostbyname, gethostname


def get_pod_ip():
    """
    Get Pod IP through multiple methods:
    1. First try POD_IP environment variable (set by Kubernetes)
    2. Then try to get hostname IP resolution
    3. Fail if the above don't return an ip
    """
    # Try getting POD_IP from environment variable
    pod_ip = os.environ.get('POD_IP')

    if not pod_ip:
        try:
            # Try resolving hostname to IP
            pod_ip = gethostbyname(gethostname())
        except EnvironmentError as e:
            raise Exception(f"Error reading POD_IP: {str(e)}")

    return pod_ip

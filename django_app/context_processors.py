import socket

def get_hostname():
    return socket.gethostname()

def pod_info_context(request):
    return {
        'pod_hostname': get_hostname(),
    }

import aerospike
from src.constants import AEROSPIKE_CONFIG


def poll_for_profile_update(profile: str, timestamp: int) -> bool:
    client = aerospike.client(config={'hosts': [(AEROSPIKE_CONFIG['host'], AEROSPIKE_CONFIG['port'])]}).connect()
    key = (AEROSPIKE_CONFIG['namespace'], 'post', profile)
    (key, metadata) = client.exists(key)
    needs_update = True
    if metadata is not None:
        (key, metadata, last_post) = client.get(key)
        if timestamp <= last_post['timestamp']:
            needs_update = False

    if needs_update:
        new_post = {'timestamp': timestamp}
        client.put(key, new_post)

    client.close()
    return needs_update


if __name__ == '__main__':
    updated = poll_for_profile_update('test-profile-01', 1233)
    print(updated)

import hashlib
import requests
import sys


ENDPOINT = 'https://api.pwnedpasswords.com/range/'


def get_sha1_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()


def evaluate_results(password_hash, response):
    password_hash = password_hash.upper()

    for result in response.content.decode().splitlines():
        result, occurrences = result.split(':')

        if password_hash == password_hash[:5] + result:
            return occurrences
    return False


def poll_api(prefix):
    return requests.get(ENDPOINT + prefix)


if __name__ == '__main__':
    try:
        password = sys.argv[1]
        password_hash = get_sha1_hash(password)
        response = poll_api(password_hash[:5])

        if response.status_code == 200:
            occurrences = evaluate_results(password_hash, response)

            if occurrences:
                print(password + ' was found')
                print('Hash ' + password_hash + ', ' + occurrences + ' occurrences')
            else:
                print(password + ' was not found')
        else:
            print('Invalid API request')
    except IndexError:
        print('No password argument')

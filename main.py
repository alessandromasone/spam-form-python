import requests
import concurrent.futures
import argparse
import json
import logging
import datetime
from faker import Faker


def register_user(url, data, user_num):
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        logging.info(f'Registration successful for user {user_num} with data: {data}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Registration failed for user {user_num} with data: {data}: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The URL of the registration page')
    parser.add_argument('json_file', help='The path of the JSON file containing registration data')
    parser.add_argument('-t', '--threads', type=int, default=100, help='The number of threads to use')
    parser.add_argument('-n', '--num_users', type=int, default=500000, help='The number of users to register')
    parser.add_argument('-r', '--use_random', action='store_true', help='Use random data for registration')
    parser.add_argument('-l', '--log_file', default=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log', help='The path of the log file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print log messages to console')

    args = parser.parse_args()

    url = args.url
    json_file = args.json_file
    max_thread = args.threads
    num_users = args.num_users
    use_random = args.use_random
    log_file = args.log_file
    verbose = args.verbose

    # Configure the logger
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')

    # Add the url to the log file
    logging.info(f'URL: {url}')

    # Add the json file name and path to the log file
    logging.info(f'JSON file: {json_file}')

    # Load the JSON data from file
    with open(json_file) as f:
        json_data = json.load(f)

    # Create a list of data to be used for registration
    if use_random:
        data_list = []
        for i in range(num_users):
            fake = Faker()
            data = {}
            for k, v in json_data.items():
                if isinstance(v, str) and v.startswith('faker'):
                    attr = v.split('.')[-1]
                    data[k] = getattr(fake, attr)()
                else:
                    data[k] = v
            data_list.append(data)
    else:
        data_list = [json_data for _ in range(num_users)]

    # Use concurrent.futures to register users in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread) as executor:
        futures = [executor.submit(register_user, url, data, i+1) for i, data in enumerate(data_list)]

    # Wait for all the futures to complete
    concurrent.futures.wait(futures)

    # Check for exceptions in the futures
    for future in futures:
        if future.exception() is not None:
            logging.error(f'Error during registration: {future.exception()}')

    print(f'All registrations complete for {num_users} users')

    # Print log messages to console if verbose flag is set
    if verbose:
        with open(log_file, 'r') as f:
            print(f.read())

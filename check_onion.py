import os.path
import requests
from bs4 import BeautifulSoup
import logging
from concurrent.futures import ThreadPoolExecutor


def create_log():
    """
       Creates the log file and configures logging settings.
       """
    logging.basicConfig(filename='script_log.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def check_tor_connection(proxies):
    """
        Checks the Tor connection and determines if the current IP is a Tor exit node IP.
        """
    logging.info("Tor Connection Check")
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            the_ip = requests.get('https://ident.me', proxies=proxies).text
            tor_iplist = requests.get('https://check.torproject.org/exit-addresses').text

            if the_ip in tor_iplist:
                logging.info(f'Tor_IP = {the_ip}')
                logging.info('Tor Connection Success')
                return True
            else:
                logging.error('The_IP not in Tor exit node list')
                if attempt < max_attempts - 1:
                    logging.info(F'Retry {attempt+1}/{max_attempts}')
                else:
                    return False
        except Exception as e:
            logging.error(f'Failed to establish Tor connection: {e}')
            if attempt < max_attempts - 1:
                logging.info(f'Retry {attempt+1}/{max_attempts}')
            else:
                return False
    return True


def url_file(filename):
    """
        Reads URLs from the given file name and returns them as a list.
        """
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        logging.error('File not found')
        return None


def scraping_urls(urls, proxies):
    """
        Scrapes URLs and processes their contents based on the given URL list and proxies.
        """
    for url in urls:
        url = url.strip()
        try:
            r = requests.get(url, proxies=proxies, timeout=30)
            if r.status_code == 200:
                s = BeautifulSoup(r.text, 'html.parser')
                page_title = s.title.string if s.title else 'No title'
                logging.info(f'Active: {url} - {page_title}')
            else:
                logging.info(f'Inactive HTTP {r.status_code} : {url}')
        except requests.RequestException as e:
            logging.error(f'Error accessing... {url} : {e}')


def main():
    create_log()

    proxies = {
            'http': 'socks5h://127.0.0.1:1337',
            'https': 'socks5h://127.0.0.1:1337'
    }
    if not check_tor_connection(proxies):
        return
    while True:
        path = input('Enter the URL File Path >')
        if os.path.isfile(path):
            break
        else:
            logging.error('Invalid file path. Please try again.')
    urls = url_file(path)
    if urls is not None:
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(lambda url: scraping_urls(url, proxies), urls)


if __name__ == '__main__':
    main()

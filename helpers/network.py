# r001
import requests
import logging


class Network:
    logger_name = 'ddd_network'
    logger = logging.getLogger(logger_name)
    logger.addHandler(logging.NullHandler())

    def __init__(self, headers=''):
        if headers == '':
            self.logger.warning("Empty header parameter")

        self.headers = headers
        self.last_answer = None
        self.session = requests.Session()

    def get_data(self):
        return self.last_answer.text

    def get_data_json(self):
        return self.last_answer.json()

    def do_get(self, url):
        self.logger.debug("Get url: {}".format(url))

        try:
            self.last_answer = self.session.get(url, headers=self.headers)
            self.logger.debug("Result url ({:d}): {}".format(self.last_answer.status_code, self.last_answer.url))

            if self.last_answer.url.lower() != url.lower():
                self.logger.warning("Redirect to: {}".format(self.last_answer.url))

        except requests.exceptions.RequestException as e:
            self.logger.warning("Fatal error [get url]: {}".format(e))
            return False

        self.logger.debug("Get url: ok")
        return True

    def do_post(self, url, data):
        self.logger.debug("Post url: {}".format(url))

        try:
            self.last_answer = self.session.post(url, headers=self.headers, data=data)
            self.logger.debug("Result url ({:d}): {}".format(self.last_answer.status_code, self.last_answer.url))

        except requests.exceptions.RequestException as e:
            self.logger.warning("Fatal error [post url]: {}".format(e))
            return False

        self.logger.debug("Post url: ok")
        return True

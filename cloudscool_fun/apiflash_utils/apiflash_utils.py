import os
import requests
import datetime
from urllib3.util import parse_url
from requests import PreparedRequest

from munch import Munch

from .common import APIFLASH_URL, APIFLASH_TOKEN

class ApiflashMicroClient:

    commands = Munch(dict(
        url_to_image='urltoimage',
        ))

    def __init__(self, url=APIFLASH_URL, token=APIFLASH_TOKEN,
            screenshot_dir=None):

        self.url = url
        self.ver = 'v1'
        self.token = token
        self.screenshot_dir = screenshot_dir if screenshot_dir else '/tmp'

    def send_request(self, url, **params):
        # i'm using requests to test the URL
        PreparedRequest().prepare_url(url, dict())

        http_ep = '{}/{}/{}?'.format(
            self.url,
            self.ver,
            self.commands.url_to_image,\
            )

        if not self.token:
            raise OSError(
                    ('Token could not be found in'
                     'env variable APIFLASH_TOKEN')
                    )

        params.update(dict(
            access_key=self.token,
            url=url,
            ))
        response = requests.get(http_ep, params=params)
        return response

    def get_image_default(self, for_url):
        response = self.send_request(for_url).content
        print(response)
        fn = 'screenshot_{}.jpeg'.format(
                str(datetime.datetime.now()).replace(' ', '_')
                )
        fp = os.path.join(self.screenshot_dir, fn)
        with open(fp, 'wb') as f:
            f.write(response)
        return True

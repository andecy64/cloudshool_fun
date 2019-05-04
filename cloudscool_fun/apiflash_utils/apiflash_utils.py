import sys
import os
import requests
import datetime
from urllib3.util import parse_url
from requests import PreparedRequest
try:
    from StringIO import BytesIO
except ImportError:
    from io import BytesIO

from munch import Munch
from PIL import Image

from .common import APIFLASH_URL, APIFLASH_TOKEN
from ..util.logs import get_logger

class ApiflashMicroClient:

    commands = Munch(dict(
        url_to_image='urltoimage',
        ))

    def __init__(self, url=APIFLASH_URL, token=APIFLASH_TOKEN,
            screenshot_dir=None):

        self.logger = get_logger(__name__)
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

    def process_image(self, image_bytes):
        buf = BytesIO()
        buf.write(image_bytes)
        buf.seek(0)
        try:
            image = Image.open(buf)
        except IOError as e:
            self.logger.error(e)
            return False
        else:
            fn = 'screenshot_{}.jpeg'.format(
                    str(datetime.datetime.now()).replace(' ', '_')
                    )
            fp = os.path.join(self.screenshot_dir, fn)
            with open(fp, 'wb') as f:
                f.write(image_bytes)
            self.logger.info('Image written successfully: {}'.format(fp))
            return True
        finally:
            del buf
        
    def get_image_default(self, for_url):
        response = self.send_request(for_url).content
        status = self.process_image(response)
        if not status:
            self.logger.error('Something went wrong: {}'.format(response))
        return status

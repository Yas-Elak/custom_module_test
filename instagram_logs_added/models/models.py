# -*- coding: utf-8 -*-

import json
import requests

from odoo import models, fields
from werkzeug.urls import url_join
import logging

_logger = logging.getLogger(__name__)

class instagram_logs_added(models.Model):
    _inherit = 'social.live.post'
    def _post_instagram(self):
        """ Posting on Instagram is done in 2 separate successive steps.

        First create what they call the 'media container', that basically means upload the image and
        the associated message using a first HTTP call.

        Then mark this 'container' as published using the ID returned by the first call.
        Without this second step, the content is not visible on the Instagram account.

        More information & examples:
        - https://developers.facebook.com/docs/instagram-api/reference/ig-user/media
        - https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish """

        self.ensure_one()
        _logger.warning("I am in the function of the custom module")
        account = self.account_id
        post = self.post_id

        base_url = self.get_base_url()

        media_result = requests.post(
            url_join(
                self.env['social.media']._INSTAGRAM_ENDPOINT,
                "/%s/media" % account.instagram_account_id
            ),
            data={
                'caption': self.message,
                'access_token': account.instagram_access_token,
                'image_url': url_join(
                    base_url,
                    f'/social_instagram/{post.instagram_access_token}/get_image'
                )
            },
            timeout=10
        )

        if media_result.status_code != 200 or not media_result.json().get('id'):
            _logger.warning("I am in the first failed possibility")
            _logger.warning(json.loads(media_result.text or '{}').get('error', {}).get('message', ''))
            _logger.warning("Media result")
            _logger.warning(media_result)
            res = super(instagram_logs_added, self)._post_instagram()
            return res

        publish_result = requests.post(
            url_join(
                self.env['social.media']._INSTAGRAM_ENDPOINT,
                "/%s/media_publish" % account.instagram_account_id
            ),
            data={
                'access_token': account.instagram_access_token,
                'creation_id': media_result.json()['id'],
            },
            timeout=5
        )

        if (publish_result.status_code == 200):
            self.instagram_post_id = publish_result.json().get('id', False)
            values = {
                'state': 'posted',
                'failure_reason': False
            }
        else:
            _logger.warning("I'am in the second possibility of failure")
            _logger.warning("publish result")
            _logger.warning(publish_result)
            res = super(instagram_logs_added, self)._post_instagram()
            return res

        res = super(instagram_logs_added, self)._post_instagram()
        return res






#     _name = 'instagram_logs_added.instagram_logs_added'
#     _description = 'instagram_logs_added.instagram_logs_added'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

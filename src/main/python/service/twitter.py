#
# Copyright 2014 Alien Laboratories, Inc.
#

from injector import Module, provides

import service.oauth


class ServiceModule(Module):
    ID = 'TWITTER'

    @provides(service.oauth.OAUTH_CONFIG_KEY)
    def provides_oauth_service_config(self):
        return {
            ServiceModule.ID: {
                'consumer_key':         'nYJVUFHXNhPThh55VCn3yEmN2',
                'consumer_secret':      'NIpWGuCSq6PV7xZpFghfOpkoNAyxHnYouj0zuG7bS8IYs43MBf',
                'admin_url':            'https://apps.twitter.com/app/8290846',

                'base_url':             'https://api.twitter.com/1/',
                'request_token_url':    'https://api.twitter.com/oauth/request_token',
                'access_token_url':     'https://api.twitter.com/oauth/access_token',
                'authorize_url':        'https://api.twitter.com/oauth/authorize'
            }
        }

# -*- coding: utf-8 -*-

import requests
import json


class PyGun(object):
    """
    Simple python module for communicating with Mailgun API.
    Mailgun documentation: https://documentation.mailgun.com/
    """

    def __init__(self, api_key, domain):

        self._api_key = api_key
        self._domain = domain

    def sender(self, sender_mail, sender_name=None):

        if sender_name:
            self._sender = "{} <{}>".format(sender_name, sender_mail)

        else:
            self._sender = sender_mail

    def to(self, to_mail, to_name):

        if to_name:
            self._to = "{} <{}>".format(to_name, to_mail)

        else:
            self._to = to_mail

    def subject(self, subject):

        self._subject = subject

    def text(self, text):

        self._text = text

    def send(self):

        r = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(self._domain),
            auth=("api", self._api_key),
            data={
                "from": self._sender,
                "to": self._to,
                "subject": self._subject,
                "text": self._text
            }
        )

        return json.loads(r.text)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import settings
from urls import urls_dict
from wsgiref.simple_server import make_server


def response_data(environ):
    # response_head
    coding_dream_response_head = [('Server', 'Coding-Dream')]
    # cookie
    coding_dream_cookie = environ.get('coding_dream_cookie', None)
    if coding_dream_cookie:
        cookie_str = ''
        for k, v in coding_dream_cookie.items():
            cookie_str += '{}={};'.format(k, v)
        coding_dream_response_head.append(('Set-Cookie', cookie_str))
    # Location
    coding_dream_location = environ.get('coding_dream_location', None)
    if coding_dream_location:
        coding_dream_response_head.append(('Location', coding_dream_location))
    # status
    coding_dream_status = environ.get('coding_dream_status', '200 OK')
    return coding_dream_status, coding_dream_response_head


def application(environ, response):
    path = environ.get('PATH_INFO')
    if path in urls_dict:
        res = urls_dict.get(path)(environ)
        status, head = response_data(environ)
        response(status, head)
    else:
        try:
            with open('./' + settings.STATIC_URL + path, 'rb') as f:
                response('200 OK', [('Server', 'Coding-Dream')])
                data = f.read()
                res = data
        except FileNotFoundError:
            response('404 Not Found', [('Serve', 'Coding-Dream')])
            res = b'<h1> 404 not found </h1>'
    return [res]


def run():
    http = make_server(settings.HOST, settings.PORT, application)
    http.serve_forever()



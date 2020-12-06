#!/usr/bin/env python
# -*- coding:utf-8 -*-
from coding_dream.html_rendering import render_html, redirect
from coding_dream.tools import get_request_data, post_request_data, get_request_method, get_cookie
from coding_dream.models import use_sql


def welcome(request):
    return b'hello coder'






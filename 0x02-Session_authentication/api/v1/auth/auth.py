#!/usr/bin/env python3
""" Authentication Module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ API Authentication Management Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns Authorization Header Request"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user Request Validation """
        return None

    def session_cookie(self, request=None):
        """ Request Returns SESSION_NAME cookie value """
        if request is None:
            return None

        cookie_key = getenv('SESSION_NAME')

        return request.cookies.get(cookie_key)

#!/usr/bin/env python3
"""API Authentication module.
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check API route Authentication
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Request that gets the authorization header field
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User Request
        """
        return None

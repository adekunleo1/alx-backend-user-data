#!/usr/bin/env python3
""" User Session Class
"""

from models.base import Base


class UserSession(Base):
    """ User Session Authentication class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ User Session Class instance Initialization.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')

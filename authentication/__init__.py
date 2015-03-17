#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides a simplified authentication framework."""


import binascii
from . import hashlib

USERS = {
    'augustus': ('thp=XjFHXbY4P4Nmsu', 'c71c843ce8fff691090c6cbca29441bf'),
    'charlie': ('GlGdTS-gHF7ZhpHx!a', '1658f297e47b8de4c080657c3b1aa3ea'),
    'mike': ('4HIctXCUYd5DIH_uAi', '2686ecd96a47c1f7e7ce555eb6867442'),
    'veruca': ('h7uDDhG290WCSAwmf6', 'c13a5f3dc8f41f1856a8861add6baa0e'),
    'violet': ('jFcpIzJN-Z9ZsXK8zO', 'a83f99cf8c7de63eb2b8471afac65ac1'),
}


def authenticate(username, password, userdb=USERS):  # pylint: disable=I0011, W0102
    """Authenticates a user against a password database.

    Password database must be in the form of a dict with two-item tuple
    values representing the salt and hashed password, respectively.

    .. code:: python

        {'username': ('salt', 'hashed password')}

    Args:
        username (str): The name of the user to authenticate.
        password (str): The plaintext password of the user to process.
        userdb (dict, optional): A user database in the form of a dict, as
            above.

    Returns:
        bool: True if the username and password are correct, else False.

    Examples:
        >>> authenticate('augustus', 'funny pages')
        False
    """
    authenticated = False
    if username in userdb:
        userinfo = userdb[username]
        if userinfo[1] == pbkdf2(password, userinfo[0]):
            authenticated = True

    return authenticated


def pbkdf2(password, salt, hashfunc='sha512', rounds=100000, dklen=16):
    """Returns a pbkdf2-processed hash as an ASCII hex.

    Args:
        password (str): The password to hash.
        salt (str): A salt to use in the hash.
        hashfunc (str, optional): The hashfunc to use, supported by hashlib.
        rounds (int, optional): Number of times to process the hash.
        dklen (int, optional): Length of the derived key produced.

    Returns:
        str: A derived key as an ASCII hex string.

    Examples:
        >>> pbkdf2('apples', 'oranges')
        'd430d86bbd2000ba97d04ec5b02ca389'
    """
    derived = hashlib.pbkdf2_hmac(hashfunc, password, salt, rounds, dklen)
    return binascii.hexlify(derived)

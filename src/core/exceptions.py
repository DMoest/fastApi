#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Custom Exceptions module
"""


class AuthError(Exception):
    """
    Exception raised for errors in the authentication process.
    """

    def __init__(self, message: str):
        """
        Constructor for the AuthError class
        """
        super().__init__(message)
        self.status_code = 401
        self.type = 'Unauthorized'

    def __str__(self):
        """
        String representation of the AuthError
        """
        return f"{self.type}: {self.args[0]}"


class BadRequestError(Exception):
    """
    Exception raised for errors in the request body.
    """

    def __init__(self, message: str):
        """
        Constructor for the BadRequestError class
        """
        super().__init__(message)
        self.status_code = 400
        self.type = 'BadRequest'

    def __str__(self):
        """
        String representation of the BadRequestError
        """
        return f"{self.type}: {self.args[0]}"


class NotFoundError(Exception):
    """
    Exception raised for errors when a resource is not found.
    """

    def __init__(self, message: str):
        """
        Constructor for the NotFoundError class
        """
        super().__init__(message)
        self.status_code = 404
        self.type = 'NotFound'

    def __str__(self):
        """
        String representation of the NotFoundError
        """
        return f"{self.type}: {self.args[0]}"


class ConflictError(Exception):
    """
    Exception raised for errors when a resource is in conflict.
    """

    def __init__(self, message: str):
        """
        Constructor for the ConflictError class
        """
        super().__init__(message)
        self.status_code = 409
        self.type = 'Conflict'

    def __str__(self):
        """
        String representation of the ConflictError
        """
        return f"{self.type}: {self.args[0]}"


class InternalServerError(Exception):
    """
    Exception raised for errors when an internal server error occurs.
    """

    def __init__(self, message: str):
        """
        Constructor for the InternalServerError class
        """
        super().__init__(message)
        self.status_code = 500
        self.type = 'InternalServer'

    def __str__(self):
        """
        String representation of the InternalServerError
        """
        return f"{self.type}: {self.args[0]}"


class DatabaseError(Exception):
    """
    Exception raised for errors when a database error occurs.
    """

    def __init__(self, message: str):
        """
        Constructor for the DatabaseException class
        """
        super().__init__(message)
        self.status_code = 500
        self.type = 'DatabaseError'

    def __str__(self):
        """
        String representation of the DatabaseException
        """
        return f"{self.type}: {self.args[0]}"


class ValidationError(Exception):
    """
    Exception raised for errors when a validation error occurs.
    """

    def __init__(self, message: str):
        """
        Constructor for the ValidationException class
        """
        super().__init__(message)
        self.status_code = 422
        self.type = 'ValidationException'

    def __str__(self):
        """
        String representation of the ValidationException
        """
        return f"{self.type}: {self.args[0]}"

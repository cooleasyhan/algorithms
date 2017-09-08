class OhnoException(Exception):
    pass


class StackException(OhnoException):
    pass


class StackEmptyException(StackException):
    pass


class StackFullException(StackException):
    pass

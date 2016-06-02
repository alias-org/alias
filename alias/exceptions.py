import alias

class AliasException(Exception):
    """Root for alias exceptions.  Used to define further exceptions.  Never raised"""
    pass

class ArgumentException(AliasException):
    pass

class FrameworkException(AliasException):
    pass

class LabellingException(AliasException):
    pass

class ParsingException(AliasException):
    pass

class DbException(AliasException):
    pass

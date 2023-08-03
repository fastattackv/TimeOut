class TimeTypeError(Exception):
    def __init__(self, time, message="The time type is not valid: "):
        message += str(type(time))
        super().__init__(message)


class NotCommandError(Exception):
    def __init__(self, message="The command entered is not callable"):
        super().__init__(message)


class InfosTypeError(Exception):
    def __init__(self, infos, message="The infos type is not valid: "):
        message += str(type(infos))
        super().__init__(message)


class BadTimingError(Exception):
    def __init__(self, state, wanted_state):
        message = f"The timeout timing could not be modified: the timeout was {state} and you tried to make it {wanted_state}"
        super().__init__(message)

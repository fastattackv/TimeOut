"""
Module to create timeouts in your python code.
During the timeout, your code runs normally because the timeout is running in a second thread
The accuracy of the timeout is roughly 0.1 seconds (maximum of 0.2) with the normal frequency.

Go check the GitHub page for the documentation and more information:

Developed by Fastattack

Version: 1.0
"""
import TimeOutErrors
from threading import Thread
import time


class TimeOut:
    def __init__(self, time: float, command, infos=False, frequency=0.02):
        """Create the TimeOut instance

        :param time: time to wait until command is activated
        :param command: function to execute when time has been reached
        :param infos: optional parameter, if set to True, the TimeOut will print when it starts/stops/get paused/get resumed
        :param frequency: optional parameter, modify the frequency to which the timeout changes (stops/pauses/resets...). Modifying this parameter is not recommanded
        :raise TimeTypeError: if the time entered is not an integer or float
        :raise NotCommandError: if the command entered is not callable
        """
        if type(time) != float and type(time) != int:
            raise TimeOutErrors.TimeTypeError(time)
        if not callable(command):
            raise TimeOutErrors.NotCommandError()
        if type(infos) != bool:
            raise TimeOutErrors.InfosTypeError(infos)
        self.time = time
        self.command = command
        self.infos = infos
        self.frequency = frequency
        self.state = "stopped"
        self.actual_time = time

    def configure_time(self, time: int):
        """Change the time to wait until command is activated

        :param time: time to wait until command is activated
        """
        if self.state == "stopped":
            if type(time) != int:
                raise TimeOutErrors.TimeTypeError(time)
            else:
                self.time = time
        else:
            raise TimeOutErrors.BadTimingError(self.state, "configure time")

    def configure_command(self, command):
        """Change the function to execute when time has been reached

        :param command: function to execute when time has been reached
        """
        if self.state == "stopped":
            if not callable(command):
                raise TimeOutErrors.NotCommandError()
            else:
                self.command = command
        else:
            raise TimeOutErrors.BadTimingError(self.state, "configure time")

    def configure_infos(self, infos: bool):
        """Change if the information about the TimeOut are printed or not

        :param infos: if set to True, the TimeOut will print when it starts/stops/get paused/get resumed
        """
        if type(time) != bool:
            raise TimeOutErrors.InfosTypeError(time)
        else:
            self.infos = infos

    def start(self):
        """Starts the timeout
        """
        if self.state == "stopped":
            self.state = "running"
            self.actual_time = self.time
            thread = Thread(target=self.thread_command)
            thread.start()
        else:
            raise TimeOutErrors.BadTimingError(self.state, "run")
        self.info("TimeOut started")

    def stop(self):
        """Ends the timeout (can not resume after stopping: you have to restart the timer to use it again)
        """
        if self.state != "stopped":
            self.state = "stopped"
        else:
            raise TimeOutErrors.BadTimingError(self.state, "stop")
        self.info("TimeOut stopped")

    def pause(self):
        """Pauses the timer
        """
        if self.state == "running":
            self.state = "paused"
        else:
            raise TimeOutErrors.BadTimingError(self.state, "pause")
        self.info(f"TimeOut has been paused, time left: {self.actual_time}")

    def resume(self):
        """Resumes the timer
        """
        if self.state == "paused":
            self.state = "running"
        else:
            raise TimeOutErrors.BadTimingError(self.state, "resume")
        self.info(f"TimeOut has been resumed")

    def reset(self):
        """Resets the timer to zero and restarts it
        """
        self.stop()
        time.sleep(self.frequency*1.5)
        self.start()

    def thread_command(self):
        """Internal function, function to assign to the thread
        """
        while True:
            if self.state == "running":
                if self.actual_time <= 0:
                    self.stop()
                    self.command()
                else:
                    self.actual_time -= self.frequency
                    time.sleep(self.frequency)
            elif self.state == "paused":
                time.sleep(self.frequency)
            else:
                break

    def info(self, message: str):
        """Internal function, function to print information if info is True

        :param message: message to print
        """
        if self.infos:
            print(message)

    def get_time_left(self) -> float:
        """Returns the time left before the command is executed

        :return: time left, if the TimeOut state is stopped: returns 0
        """
        if self.state != "stopped":
            return self.actual_time
        else:
            return 0

    def get_state(self) -> str:
        """Returns the current state of the TimeOut

        :return: current state (running/stopped/paused)
        """
        return self.state

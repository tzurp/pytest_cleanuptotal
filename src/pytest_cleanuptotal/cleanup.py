import inspect
import traceback
from typing import Callable
from helpers.logger import Logger

class Cleanup:
    _cleanupList = []
    """This field is private, please don't change it.
    """
    logger = Logger()

    def __init__(self):
        self._cleanupList = []
        
    def add_cleanup(self, cleanupFunction: Callable) -> None:
        """Add cleanup function to the cleanup stack.

        Args:
            cleanupFunction (Callable): a cleanup function. It can be a lambda or regular function.
        """
        self._cleanupList.append(cleanupFunction)
    
      
    def finalize(self) -> None:
        """Please don't call this method directly.
        """
        errors = []
        if len(self._cleanupList) == 0:
            return

        self._cleanupList.reverse()
        
        for cleanup_function in self._cleanupList:
            try:
                source = inspect.getsource(cleanup_function)
                cleanup_function()
                self.logger.debug(f"pytest-cleanuptotal[😊]: Successfully executed '{source}' ({cleanup_function})")
            except Exception as err:
                message = f"pytest-cleanuptotal[😕]: Failed to execute '{source}' ({cleanup_function}): {err}, ${traceback.format_exc()}"
                errors.append(message)
            

        if len(errors) > 0:
            self.logger.error(f"pytest-cleanuptotal: Warning!!!: Cleanup finished with {len(errors)} error(s):")

            for run_error in errors:
                self.logger.error(run_error)
            

        self._cleanupList = []
        
        

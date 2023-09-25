import traceback
from typing import Callable

class Cleanup:
    _cleanupList = []
    """This field is private, please don't change it.
    """
    
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
        # TODO remove print
        print("### Cleanup initialized ###")

        self._cleanupList.reverse()
        
        for cleanup_function in self._cleanupList:
            try:
                cleanup_function()
            except Exception as err:
                message = f"pytest-cleanuptotal[😕]: Failed to execute '{cleanup_function}': {err.args[0]}, ${traceback.format_exc()}"
                errors.append(message)
            

        if len(errors) > 0:
            print(f"pytest-cleanuptotal: Warning!!!: Cleanup finished with {len(errors)} error(s):")

            for run_error in errors:
                print(run_error)
            

        self._cleanupList = []
        # TODO remove print
        print(f"pytest-cleanuptotal-cleanup: ### Cleanup done ###)")
        
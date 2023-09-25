from pytest_cleanuptotal.cleanup import Cleanup

def test_fail(cleanuptotal: Cleanup):
  cleanuptotal.add_cleanup(lambda: print("cleanup error stage 1"))

  def cleanup_function():
    print("before-cleanup error stage 2")
    raise Exception("Intentional exception")
    print("after-cleanup error stage 2")
  
  cleanuptotal.add_cleanup(cleanup_function)
    

  cleanuptotal.add_cleanup(lambda: print("cleanup error stage 3"))

  

def test_pass(cleanuptotal: Cleanup):
  cleanuptotal.add_cleanup(lambda: print("Cleaning pytest_playwright stage 1"))

  cleanuptotal.add_cleanup(lambda: print("Cleaning pytest_playwright stage 2"))

  cleanuptotal.add_cleanup(lambda: print("Cleaning pytest_playwright stage 3"))

  cleanuptotal.add_cleanup(lambda: print("Cleaning pytest_playwright stage 4"))
  
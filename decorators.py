import time

def log_execution_time(func):
  """
  Implements and return wrapper function
  """

  def wrapper(*args, **kwargs):
    """
    This function implements additional functionalities 
    wrapping to original function
    """

    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"The execution time of {func.__name__} was {end - start}")
    return result

  return wrapper

@log_execution_time
def prepare_dish(name):
  print(f"Cooking {name}...")
  time.sleep(2) # preparing dish
  print(f"Dish {name} is ready")

prepare_dish("Maxican rice")
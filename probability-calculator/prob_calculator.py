import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for index, value in kwargs.items():
      for i in range(value):
        self.contents.append(index)    


  def draw(self, number_of_balls):
        balls_returned = list()
        for i in range(min(len(self.contents), number_of_balls)):
            removed = self.contents.pop(random.randrange(len(self.contents)))
            balls_returned.append(removed)

        return balls_returned 
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_no_of_balls = []
  for key in expected_balls:
      expected_no_of_balls.append(expected_balls[key])
  count_successes = 0

  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls_count = new_hat.draw(num_balls_drawn)

    num_balls = []
    for i in expected_balls:
      num_balls.append(balls_count.count(i))

    if num_balls >= expected_no_of_balls:
      count_successes = count_successes + 1

  num_expected_n_m = (count_successes/num_experiments)
  return num_expected_n_m
    
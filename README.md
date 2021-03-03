# dog_shelter
Dog Shelter Project

###### Project Requirements:
   * Python 3.8

###### Running the DogShelter.get_food_quantity() method:
   1. open a command prompt
   2. navigate to the project folder
   3. type `python` to enter the python terminal
   4. import the DogShelter object by typing `from Dev.DogShelter import DogShelter`
   5. test the method with various values by typing
       DogShelter.get_food_quantity(small, medium, large, left_over)
       e.g. `DogShelter.get_food_quantity(5, 3, 7, 17)`

###### Running the tests from a command prompt:
   1. open a command prompt
   2. navigate to the project folder
   3. install pytest if you don't already have it by typing `pip install pytest`
   4. type `pytest -m "regression"` to run all of the regression tests
       or typ `pytest -m "smoke"` to run just the smoke tests
       (technically these are all unit tests, but I'm adding these tags as an example)
    
###### Running the tests inside PyCharm:
   1. open the project in PyCharm
   2. type `pip install pipenv`
   3. create a virtual environment by typing `pipenv shell`
   4. in the File >> Settings >> Project:dog_shelter >> Project Interpreter
       add a new interpreter for the virtual environment
       * click the gear icon and select "add"   
       * select "existing environment"
       * select the "..." and navigate to the python.exe script in your virtual environment
           It's likely in `C:\Users\{username}\.virtualenvs\dog_shelter-{random numbers}\scripts\python.exe`
       * click "ok", select it from the list and click "ok" again, then click "ok" one last time
   5. setup a run configuration by clicking on "edit configuration" in the top right of PyCharm
      * click the "+" button and add a pytest configuration
      * for the target: script path add the project folder (e.g. `C:/dog_shelter`)
      * for the arguments enter `-m "regression"` to run the regression tests or
           `-m "smoke"` to run the smoke tests
      * click "ok" to finish setting the configuration
      * click the play button to run the tests

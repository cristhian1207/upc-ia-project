Execute the sql script in mysql: database/script.sql

Install the required libraries with the command:  
  ```pip install [LIBRARY NAME]```  
  or  
  ```python -m pip install [LIBRARY NAME]``` for Windows  
  or  
  ```python3 -m pip install [LIBRARY NAME]``` for Linux and Mac  

To execute a python file run the command:  
  ```python [PYTHON FILE]``` for Windows  
  or  
  ```python3 [PYTHON FILE]``` for Linux and Mac

To create the dataset execute the script ```dataset.py```  
To run the training process execute the script ```training.py```  
To mark the attendance execute the script ```reconigtion.py```  

For test purposes run the script ```reconigtion_test.py``` to show the person identifier and the confindence level.

The execute order is the next:
  1) dataset.py
  2) training.py
  3) reconigtion.py or reconigtion_test.py
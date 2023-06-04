```
project/
|----data/
|---notebooks/
|---scripts
|---README.md
|---requirements.txt
```
instaliation:

Download project to your local repository.
- open cmd or powershell in you folder
- enter this command in cmd or powershell
```git clone https://github.com/Polonez1/taxis-analysis "taxis-analysis"```

install all requirements
```pip install -r requirements.txt```

Run cmd or powershell in the folder.

Commands:
Run data heatmap visualisation
```python run.py --run_visualisation --action [save, show] --month [from 01 to 12] --by [tip, fare, passenger, profit_by_passenger]```

Run profit table
```python run.py --run_table --action [save, show] --month [from 01 to 12]```

Run bar visualisation by weather and passenger
```python run.py --run_weather_bar --action [save, show] --month [from 01 to 12]```

Run data compare
```python run.py --run_data_compare```


Goals:
1. Calculate and find the most profitable taxi options
2. create a visualization that shows the busiest days according to the number of customers, tips, earnings e.c.

```data``` 
/folder

```map_data```
/folder 
- The folder is for storing map tables
    
 ```yellow_trip_data_2022``` 
 /folder 
 - The folder is for storing taxis data
    
```notebooks```
/folder 
- This folder contains all the Jupyter notebooks used for the analysis. 

```scripts```
/folder 
- This folder contains all the modules. modules have calculation, data processing, data loading and visualization functions

```README.md``` 
this file have instructions about this project


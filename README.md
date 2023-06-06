```
project/
|---data/
    |---green_trip_data_2022
    |---map_data
    |---trip_data_2019_03
    |---yellow_trip_data_2022
|---output/
|---scripts/
        |---data_compare_scripts/
        |---weather_scripts/
|---README.md
|---requirements.txt
```
install:

Download project to your local repository.
- open cmd or powershell in you folder
- enter this command in cmd or powershell
```git clone https://github.com/Polonez1/taxis-analysis "taxis-analysis"```

install all requirements
```pip install -r requirements.txt```

Run cmd or powershell in the folder.

Commands:
Run data visualisation by week's names and time intervals. 
```python run.py --run_visualisation```

Run profit table and other stats.
```python run.py --run_table```

Run bar visualisation by weather and passengers count
```python run.py --run_weather_bar```

Run data compare. this command compares data from https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page and seaborn.
```python run.py --run_data_compare```

args:
Choose save or show visualisation
```--action show```
```--action save```

Choose data month
```--month 05```

choose what you want to count
```--by [tip, fare, passenger, profit_by_passenger]```

filter by date range
```-sd``` start_date
```-ed``` end_date
format yyyy-MM-dd




Goals:
1. Calculate and find the most profitable taxi options
2. create a visualization that shows the busiest days according to the number of passengers, tips, fare e.c.

```data``` 
/folder

```output``` 
/folder
- The folder is for storing all output data

```map_data```
/folder 
- The folder is for storing map tables
    
 ```...trip_data_2022``` 
 /folder 
 - The folder is for storing 2022 year taxis data

  ```trip_data_2019_03``` 
 /folder 
 - The folder is for storing 2019 03 yellow and green taxis data. this folder needed to compare seaborn data
    
```scripts```
/folder 
- This folder contains all the modules. modules have calculation, data processing, data loading and visualization functions

```README.md``` 
this file have instructions about this project


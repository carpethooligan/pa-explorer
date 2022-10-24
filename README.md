# pa-explorer
Exploring price action in an automated fashion.

This repo consists of a suit of modules for exploring price action concepts. Historical data is not included out of the box but sample historical data from a separate repository (details below) can be copied into this project for testing. 


# Installation
Create a virtual environment
```
python3 -m venv env/pa-explorer
```
Activate the environment
```
source env/pa-explorer/bin/activate
```
Install dependencies from requirements.txt
```
pip install -r requirements.txt
```

# Historical Data
Project loads historical prices from data files, split by day, from a directory called `data/ES` in the project. You can download a few months of sample data from https://github.com/carpethooligan/pa-sampledata and include those data files in your project for testing before expanding with your own datasets.

# Running
- Be sourced to the virtual environment
- Switch to the cloned repo `pa-explorer`
- Ensure `data/ES` directories exist in project, otherwise create them and add some historical data files for the code to run
- In `main.py` uncomment a module for testing some specific price action concept, for example, the code below will run a module for testing **Chance of Having Seen HOD/LOD by bar X**
```python
if __name__ == "__main__":
    exploreChanceSeenHODLOD()
```
- Execute with 
```
python3 main.py
```

# Output
The result will spit out dates processed and finally bar by bar statistics for chance of having seen HOD/LOD by that bar, assuming that module was selected for testing:
```
2022-01-03
2022-01-04
...
2022-10-12
2022-10-13
2022-10-14
Bar 1 25.0%
Bar 2 32.0%
Bar 3 37.0%
...
Bar 15 77.0%
Bar 16 78.0%
Bar 17 79.0%
Bar 18 81.0%
Bar 19 81.0%
...
Bar 79 100.0%
Bar 80 100.0%
Bar 81 100.0%
Total days: 204
```

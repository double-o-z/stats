# stats
A study purposes PyQt Application, showing various stats about the file-system.

Run the application like so:
- python app.py


The application makes use of PyQT5.7 to create various UI features to display data created in the background.
The application make use of MVC concept, separating between the UI, the data models and controllers connecting between the two.

Inside data_structures.py lies the logic, that collects and aggregates file system information to display.
For study purposes 3 algorithms were used to iterate over the file system structure to collect data.

One can create which algorithm is used by commenting in the desired algorithm and commenting out the other two.

The algorithms names are:
1. create_data - os.walk(topdown=False) - The premade python algorithm, that uses recursive depth-first-search.
2. create_data_dfs - A depth-first-search algorithm implemented in this function.
3. create_data_bfs - A Breadth-first-search algorithm implemented in this function.

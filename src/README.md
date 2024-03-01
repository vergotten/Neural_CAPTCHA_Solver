## Project Structure

The project has the following structure:

```
├── src/
│   ├── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   ├── visualization/
│   │   └── __init__.py
│   └── models/
│       └── __init__.py
```

- `src/`: This is the main source directory which contains all the scripts for pipeline. It's divided into several subdirectories:
  - `utils/`: Utility scripts that are used across the project.
  - `visualization/`: Scripts for visualizing data, results, etc.
  - `models/`: Scripts to define, train, and evaluate models.

Each directory contains an `__init__.py` file, which makes Python treat the directories as containing packages. This allows to import modules using the package name (directory name) and the module name (file name).

## Importing Modules

You can import your modules using the package name (directory name) and the module name (file name). Here's an example:

```python
from src.visualization import your_visualization_module
from src.models import your_model_module
```

In this example, `your_visualization_module` and `your_model_module` would be the names of the Python files (without the `.py` extension) in the `visualization` and `models` directories, respectively.


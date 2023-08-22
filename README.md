# Installing Anaconda Mini
The Python Enviroment Manager I suggest Using is MiniConda 

Navigate to [Anaconda's Website](https://docs.conda.io/en/latest/miniconda.html) to install Miniconda.

# Setting up MiniConda

Once MiniConda is installed launch a Anaconda Terminal and create a new python Enviroment:
### `conda create --name myenv python=3.9`

Then run `conda activate myenv`

You are now inside your new python enviroment!

# Installing Python dependencies
> :warning: **Important:** Make sure you are in the ws-backend Directory

### `pip install -r requirements.txt`

This will install all of the required python modules.

# Starting the Server
> :warning: **Important:** Make sure you are in the ws-backend Directory
### `python api.py`

The Server is now running on  http:localhost:8888.


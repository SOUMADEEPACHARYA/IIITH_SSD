The following command installs virtualenv

pip install virtualenv
This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.

Sudo apt-get install virtualenv
Once installed, new virtual environment is created in a folder.

mkdir newproj
cd newproj
virtualenv venv
venv/bin/activate
On Windows, following can be used

venv\scripts\activate
We are now ready to install Flask in this environment.

pip3 install Flask

then run python3 server.py
i only implemented server part

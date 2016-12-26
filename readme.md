# Terminal Streamer Client

The client is written in python. It requires the  [Terminal Streamer](https://github.com/vephinx/terminal-streamer) web application written in Meteor.

### What is it?

This allows you to pipe anything from your terminal to a web page.

### Prerequisites 

- Requires python 3.
- Requires the [python-meteor](https://github.com/hharnisc/python-meteor) library.

### Getting Started

1. Install the [Terminal Streamer](https://github.com/vephinx/terminal-streamer) web application written in Meteor.
2. Set the admin password in `main.py`
3. (Optional) move `main.py` to your path, make it executable and rename it. I named it `tstream` and it lives at `/usr/local/bin`.
4. Done!

Now try `ls | tstream`.

### Arguments

- Run `tstream clear` to clear the terminal stream.

### Screenshots

![terminal-streamer](https://cloud.githubusercontent.com/assets/2012398/21485202/16013a36-cb97-11e6-84d3-b93028333266.png)






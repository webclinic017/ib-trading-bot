# Interactive Brokers Trading Bot

Simple open source tool for trading shares on ASX with [Interactive Brokers Gateway API](https://interactivebrokers.github.io/tws-api/introduction.html)

## Authors

**James Dalton**

## Credits

- **[brentjm](https://github.com/brentjm/Interactive-Brokers-API)** starter python class for working with Interactive Brokers API

## Built with

- [Python](https://www.python.org/) - Scripting Language
- [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457) - Enabling API connection to Interactive Brokers API
- [Interactive Brokers Python API](http://interactivebrokers.github.io/) - Interactive Brokers API
- [Visual Studio Code](https://code.visualstudio.com/) - IDE

## Instructions

**1. Download and install [Interactive Brokers Python API](http://interactivebrokers.github.io/) and [Interactive Brokers Gateway](https://www.interactivebrokers.com.au/en/index.php?f=16457)\*\***

**2. Clone repo**

```sh
git clone https://github.com/jdalton92/ib-trading-bot.git
```

**3. Create python virtual environment in root directory**

```sh
ib-trading-bot$ python -m venv venv
```

**4. Activate virtual environment (below command for windows)**

windows:

```sh
ib-trading-bot$ venv\Scripts\activate
```

unix/mac:

```sh
ib-trading-bot$ source venv/bin/activate
```

**5. Create a wheel of the Interactive Brokers API from the directory of the TWS API installed in Step 1**

```sh
TWS API$ python setup.py bdist_wheel
```

**Note:** you will likely have to install wheel package to your Python virtual environment before being able to make a wheel

```sh
TWS API$ python -m pip install wheel
```

**6. Install Interactive Brokers API wheel**

```sh
ib-trading-bot$ python3 -m pip install --user --upgrade "C:/location/to/TWS API/dist/ibapi-9.75.1-py3-none-any.whl"
```

**Note:** the file name version will have to match your downloaded version of the Interactive Brokers API, so change _ibapi-9.75.1_ to your installed version

**7. TBC**

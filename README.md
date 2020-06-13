# full_stack_ml_project

### Project Overview

The main purpose of this project is to analyze Zomato data to build a model for an API that predicts rating for restaurant. And it also includes an Machine Learning API with user can predict restaurnt rating based on several parameters. 


### Project Components

This project contains three main parts: ETL Pipeline, Machine Learning Pipeline and Flask App. 

1. Data Gathering
   * **zomatoWrapper**: This is a packge developed to download data from Zomato. Full description can be found [here](https://github.com/ashish-gh/zomatoWrapper) 

#### How to use zomatoWrapper
#### Installation

```bash
$ pip install zomatoWrapper
```
or

```bash
$ python setup.py install
```

# Authentication

Register for an API key:

All you need to do is [register](https://developers.zomato.com/api) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret.

# Usage

With your key in hand, it's time to authenticate, so run:

```python
>>> from zomatoWrapper import Zomato

>>> zomato = Zomato('<apikey>')

>>> zomato.search('city_id','entity_type')

>>> zomato.getReviews()

```

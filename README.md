# Finance Control

This is a private project built for registering spends and (eventually) to have a realtime dashboard with grafana. The intent of this project is not to be accessible to the public user, if you want to use it you can spin up your own instance of this project


## Quickstart

1. Create a virtual enviroment
```shell
# windows
python -m venv venv && venv/scripts/activate

# bash
python -m venv venv && source venv/bin/activate
```

2. Install requirements
```shell
pip install -r requirements.txt
```

3. Set enviroment variables, just as `.env.example`; or don't, its up to you


## The project logic

The project consists of two apps: `control` which controls and manages the transactions made and `authentication`, responsible for user related rules

Each transaction, hereafter defined as any present or previous monetary incomes or expenses, must fall into a category

Each category represents a in or out "flow" (i couldn't think of a better word, its night too late)

Only active users can create, read and update any transaction or category

At this moment we doesn't have any dashboard, but this is comming soon

Further documentation is on the way
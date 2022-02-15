# lead-king-dl
automatically download leads from [Lead King](https://www.lead-king.net/amember/aff/go/supreme
)

This software logs into [Lead King](https://www.lead-king.net/amember/aff/go/supreme
) and downloads the leads for the day. It is designed to be
run once per day. It retrieves the daily file and creates a weekly file 
of all files retrieved per week.

# Installation

## Get the software

    git clone https://github.com/metaperl/lead-king-dl.git

## Build

    pip install -r requirements.txt
    cd lead-king-dl/src; mkdir data/weekly; mkdir data/daily

## Configure login

Copy `src/credentials-sample.py` to `src/credentials.py`
and put in your username and password.

## Setup a cron job

you can of course run the software manually and
locally, but the ideal is to run it automatically
every day.

```shell
# LEAD KING
@daily cd $HOME/prg/lead-king-dl/src python main.py
```

# ACKNOWLEDGEMENTS

## This code was written by Bartosz Kolodziej

In response to my [request](https://www.reddit.com/r/forhire/comments/srveyi/for_hire_software_embedded_engineer_remote_40/), he 
did a great job. He can be reached at:

* /u/hectorlab on reddit
* official website - http://bartoszkolodziej.com





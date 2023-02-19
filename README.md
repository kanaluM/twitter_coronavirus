# Coronavirus twitter analysis

I scanned all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

## Background

Approximately 500 million tweets are sent everyday.
Of those tweets, about 1% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
In total, there were about 1.1 billion tweets in the provided dataset (stored on a class server at in the `/data/Twitter dataset`).

The tweets are stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.

I used the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.

1. **Mapping:**
   The `map.py` file processes a single zip file of tweets.
   The command
   ```
   $ ./src/map.py --input_path=/data/Twitter\ dataset/geoTwitter20-02-16.zip
   ```
   creates a folder `outputs` that contains a file `geoTwitter20-02-16.zip.lang`.
   This is a file that contains JSON formatted information summarizing the tweets from 16 February.

1. **Visualizing:**
   The `visualize.py` file displays the output from running the `map.py` and `reduce.py` files.
   The command
   ```
   $ ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
   ```
   generates a bar graph of the frequency of tweets in each language containing the hashtag '#coronavirus'
    
## What I did 

1. I modified the `map.py` file so that it tracks the usage of the hashtags on both a language and country level.

1. I created a shell script `run_maps.sh` that loops over each file in the dataset and runs `map.py` on that file.
   I used the `nohup` command to ensure the program ran while I was not connected to the server and the `&` operator to ensure that all `map.py` commands ran in parallel.

1. I modified the visualize.py file so that it generated bar graphs of the results (using matplotlib) of the top 10 keys


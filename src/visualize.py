#!/usr/bin/env python3

# plotting tools
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
kr = fm.FontProperties(fname='./src/NotoSansKR-Black.otf')
import matplotlib.pyplot as plt

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
# if args.percent:
#    for k in counts[args.key]:
#        counts[args.key][k] /= counts['_all'][k]

# print the count values
# items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
# for k,v in items:
#    print(k,':',v)


# stuff I added to generate plots
category = "country" if args.input_path == "reduced.country" else "language"
language = "English" if args.key == "#coronavirus" else "Korean"

L = [(counts[args.key][k], k) for k in counts[args.key]]
L.sort(reverse=True, key=lambda x: x[0])
x = [e[1] for e in reversed(L[:10])]
y = [e[0] for e in reversed(L[:10])]

fig = plt.figure(figsize = (10, 5))
plt.bar(range(len(x)), y, color ='maroon', width = 0.8)
plt.xticks(range(len(x)), x)
plt.xlabel(f"{category.capitalize()}")
plt.ylabel(f"Number of Tweets")
if language == "English":
    plt.title(f"{args.key} Tweets in 2020 by {category.capitalize()}")
else:
    plt.title(f"{args.key} Tweets in 2020 by {category.capitalize()}", fontproperties=kr)
fig.savefig(f"{category}_{language}.png")
plt.close(fig)

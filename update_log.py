from datetime import datetime
import argparse

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Add Parser
parser = argparse.ArgumentParser(description ='Process some integers.')
parser.add_argument('-wo','--working-on',
                    type = str,
                    help ='the data structure or algorithm or a leetcode problem that you are working on.')
parser.add_argument('-bm','--base-mood', 
                    type = str,
                    help ="how are you feeling on a basic level. Mention in terms of 'positive', 'negative', 'neutral'.")
parser.add_argument('-ds','--description', 
                    type = str,
                    help ="describe your feelings and elaborate on what is exciting/bothering you.")


log = open('feelings.md', 'a')
log.write(f"\n\n__Date: {now}__")
args = parser.parse_args()
log.write(f'\n* __Working on:__ {args.working_on}')
log.write(f'\n* __Feeling:__ {args.base_mood}')
log.write(f'\n* __Description:__ {args.description}')
log.close()
# log.write()
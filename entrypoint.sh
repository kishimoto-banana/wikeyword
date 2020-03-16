#!/bin/bash
set -e

#wget https://velvet-public.s3-ap-northeast-1.amazonaws.com/jawiki_dic.pkl -P models
#wget https://velvet-public.s3-ap-northeast-1.amazonaws.com/jawiki_mention.pkl -P models

gunicorn -b 0.0.0.0:$PORT -w 2 --chdir wikeyword main:app

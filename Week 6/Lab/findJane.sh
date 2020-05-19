#!/bin/bash

> oldFiles.txt
cat ../data/list.txt | grep -w jane | cut -d ' ' -f3 >> oldFiles.txt

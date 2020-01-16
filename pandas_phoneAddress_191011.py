#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

inputFile = 'pandas_contacts.csv'

df = pd.read_csv(inputFile, encoding='cp1252', engine='python')

print(df)
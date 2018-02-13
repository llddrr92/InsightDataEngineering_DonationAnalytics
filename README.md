

# Introduction

This code streams in transactions sequentially. It cleans for and stores meaningful data, then loop through the list of transactions again.

For each transaction, the code looks through all previous inputs for repeated donors, before recording recipient, zip code, year of contribution, running percentile, total contribution amount and total number of transactions.
These are concatenated into a string and outputted.

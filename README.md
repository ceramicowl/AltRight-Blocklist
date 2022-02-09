# AltRight-Blocklist
A collection of alt-right websites, for PiHole filtering

A list of known hate groups was pulled from https://www.splcenter.org/hate-map by downloading the .csv data for all years between 2010 and 2020. All data was rejected aside from the group names, combined into a single master list, and duplicates were removed. The resulting list is saved as groups.txt.

A simple Python script runs groups.txt through the public ClearBit API, which performs a web search and returns organization info in JSON format. If a result is returned, the first web address result is passed into results.txt. In theory, this file can then be added directly into the PiHole Adlists.

Additionally, individually discovered domains are added to ManualAdditions.txt manually. This list is, by nature, overwhelmingly incomplete. However, it can provide a more convenient central list than individual blacklist entries.

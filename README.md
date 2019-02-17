# gap-trading

We are interested in characterizing the gaps; the time they take to close, and discovering ways to differentiate between gaps that close and those that don't.
60min data is attached, includes day/time stamp, open, high, low, close and misc.
NFLX includes the Volume information the others do not (for now)
Ignore the Gap columns in the text- (you can erase)
1. GAP Definition: If Open at interval T(1) < Low of interval T(0) then it's a gap down at T(1); while we will look at all gap sizes, we are most interested in gaps >.5% and <2.0%.

2. When High T(x) >= Low T(0) then the gap is considered "filled". NOTE: It's conceivable and likely that a gap will fill in the very first T(1) interval, so need to remember to check the high of T(1).  This would mean is that the stock gapped down but then rose immediately to potentially fill the gap in the same time interval.

3. Count the number of intervals between #1 and #2 and store data for analysis & outputs

4. Plot the % of total gap filled (i.e 0 to 100%) over the Time intervals (i.e. horizontal axis is time intervals required for close vs vertical axis which is % of gaps closed).  

5. Independently plot each gap size (so will turn out to be a family of curves). Practically, this may mean grouping gap sizes in buckets; e.g. 0-.49%, .5%-1.0%, etc.

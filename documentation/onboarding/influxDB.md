# Time Series Databases
- Time Series Databases (TSDB) are optimized for milisecond level query time over monthes of data
- Often, one will keep high precision data for a short period of time, and then aggregated and downsampled into longer term trend data.
- Key properties include:
    - time-stamp data storage
    - data lifecycle management
    - time series dependent scans
    - time series aware queries

# [InfluxDB](https://docs.influxdata.com/influxdb/v2.0/)
- TSDB are most rapidly growing type of database
- InfluxDB is most popular of TSDB

- Mapping Relational Datbases to InfluxDB
    - *Measurement* := like a table with primary key being a timestamp
    - *Point* := like a row in relational database, but indicates measure at a certain time
    - *Field* := data at point (a column)
    - *Tags* := additional indexes to help with query filtering
    - *Retention Policy* := the way one manages the lifecycle of the data
- For more key concepts, see [here](https://docs.influxdata.com/influxdb/v2.0/reference/key-concepts/)

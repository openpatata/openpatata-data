This repo hosts the raw data of [*openpatata*](https://github.com/openpatata/), a Cypriot-parliament tracker.
Travis produces a [completeness and validity report](https://travis-ci.org/openpatata/openpatata-data).
If you'd like to help with the collection of the data, kindly head to the [*openpatata-scrapers* repo](https://github.com/openpatata/openpatata-scrapers).

## Data analysis

Structured data lends itself easily to data analysis.
The following are some ideas about how our data could be harnessed:

- to produce plenary attendance statistics (per party and MP; seasonal
  trends; etc.), and similarly with questions (e.g. by plotting question
  frequency against time);
- to identify MPs' topics of interest by [analysing](https://en.wikipedia.org/wiki/Natural_language_processing)
  the text of their questions;
- to calculate MPs' average tenure and see how it compares with the rest of the
  world.

## Getting started

The entire dataset is distributed as a [data package](http://frictionlessdata.io/).
To load the data into Python, you can do:

```py
import datapackage

dp = datapackage.DataPackage('https://raw.githubusercontent.com/openpatata/openpatata-data/export/datapackage.json')
resources = {r.descriptor['name']: r for r in dp.resources}

# Print all of the MPs' names in Greek
for mp in resources['mps'].iter():
    print(mp['name']['el'])
```

You will need to have previously installed the `datapackage` library
(`pip3 install datapackage`).

## License

*[openpatata-data](https://github.com/openpatata/openpatata-data)* is licensed under CC BY 4.0.

# WolframAlpha Client
v1.3

Python Client built against the [Wolfram|Alpha](http://wolframalpha.com)
v2.0 API.

Original project is hosted on [bitbucket](http://bitbucket.org/jaraco/wolframalpha).

## Installation

* Clone git archive via the following command; 
  
  `git clone https://github.com/bmikolaj/wolframalpha.git wolframalpha`
* Change directories via `cd wolframalpha`
* Run the following command to install;
  
  `sudo python setup.sh install`

## Usage

Basic usage is pretty simple. Create the client with your App ID (request from
Wolfram Alpha);

    import wolframalpha
    client = wolframalpha.Client(app_id)

Then, you can send queries, which return Result objects;

    res = client.query('temperature in Washington, DC on October 3, 2012')

If you need to need to specify an assumption, you can do the following;

    res = client.query('1s + 1s','*C.s-_*Unit-')

This will assume s is a unit instead of a varaible

Result objects have `pods` attribute (a Pod is an answer from Wolfram Alpha);

    for pod in res.pods:
        do_something_with(pod)

You may also query for simply the pods which have 'Result' titles;

    print(next(res.results).text)

## Changelog
* v1.3 (21 October 2014)

  Added assumption option to query

* v1.2 (08 June 2014)

  Release by [jaraco](http://bitbucket.org/jaraco/wolframalpha) forked

## Authors
[Brian Mikolajczyk](https://github.com/bmikolaj), brianm12@gmail.com

[Jason R. Coombs](http://bitbucket.org/jaraco), jaraco@jaraco.com

## Legal
Copyright (c) 2014, Brian Mikolajczyk, brianm12@gmail.com

### Licence
Please see file LICENCE.

### Copying
Please see file COPYING.


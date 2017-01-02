
# Counterfacto

Counterfactual (noun)

Definition: the tendency to create possible alternatives to life events
that have already occurred; something that is contrary to what actually
happened.

Effects: it starts off with disappointment, then one will be able to
uncover insights or knowledge that can be used to enhance future
performance, leading to a better outcome in life.

----------------------------------------------------------------------------------

Counterfacto is a small software tool that can analyse search results
on twitter to highlight counterfactual statements on certain topics.

This tool is used by PIEnews.eu researchers for sentiment analysis
about poverty and other related topics, to understand actual stories
elaborated as counterfactual.

We deem such a tool as a useful experiment, considering the importance
of counterfactual analysis for political sentiment assessments and
focus on news stories.

## Dependencies

Python is required along the following packages:

```
python-twitter python-nltk
```

Your distro may have an outdated nltk (less than 3.2) without the
perceptron module, in that case an update from `pip` is needed:

```
pip install nltk --upgrade
```

After installing the necessary python modules, run `make`, which will
then download the needed data for nltk, and tell you how to use your
twitter credentials in counterfacto

### Running the web edition of counterfacto

To run counterfacto along with its web interface, you will need
additional dependencies:

```
python-flask
```

## Usage

```
usage: ./counterfacto [-a account] [-f tweetfile] [-s searchterm]
```

The web interface can be ran with (port defaults to 5000):

```
usage: ./counterfacto-web [-p port]
```

## References

- [Learning Representations for Counterfactual Inference (2016)](http://jmlr.org/proceedings/papers/v48/johansson16.pdf)

- [Bounding and Minimizing Counterfactual Error (2016)](https://arxiv.org/abs/1606.03976)

- [Counterfactuals in the Language of Social Media: A Natural Language Processing Project in Conjunction with the World Well Being Project (2015)](http://www.seas.upenn.edu/~cse400/CSE400_2015_2016/reports/report_15.pdf)

## Licensing

Counterfacto is Copyright (C) 2016 by the Dyne.org Foundation
as part of the PIEnews project

Software written by Ivan J. <parazyd@dyne.org>
with contributions by Denis Roio <jaromil@dyne.org>

This source code is free software; you can redistribute it and/or
modify it under the terms of the GNU Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

This source code is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  Please refer to
the GNU Public License for more details.

You should have received a copy of the GNU Public License along with
this source code; if not, write to: Free Software Foundation, Inc.,
Mass Ave, Cambridge, MA 02139, USA.

This project has received funding from the European Union’s Horizon 2020
Programme for research, technological development and demonstration under
grant agreement nr. 687922

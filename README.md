# NavicoLineSegment
[![Build Status](https://travis-ci.org/derrix060/NavicoLineSegment.svg?branch=master)](https://travis-ci.org/derrix060/NavicoLineSegment)
[![Coverage Status](https://coveralls.io/repos/github/derrix060/NavicoLineSegment/badge.svg?branch=master)](https://coveralls.io/github/derrix060/NavicoLineSegment?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/21c1742a91c8223bcbcd/maintainability)](https://codeclimate.com/github/derrix060/NavicoLineSegment/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ff75dec6d587415fb3657d02d832438c)](https://www.codacy.com/app/derrix060/NavicoLineSegment?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=derrix060/NavicoLineSegment&amp;utm_campaign=Badge_Grade)
[![GitHub license](https://img.shields.io/github/license/derrix060/NavicoLineSegment.svg)](https://github.com/derrix060/NavicoLineSegment/blob/master/LICENSE)


Repository created to exemplify one good implementation of a [Line Segment](https://www.khanacademy.org/math/basic-geo/basic-geo-lines/lines-rays/a/lines-line-segments-and-rays-review).

## LineSegment
Representation of a Line Segment in a 2-D space written in `python`, where with two distinct points is it possible to make a line segment.

The Line Segment has a lengh and a slope. The class has methods to determine if two instances of LineSegment are parallel or perpendicular.

## Tests
The tests were created using `Boundary value analysis` and `Equivalence Partitioning`, both `black-box` techniques.

The tests were improved using `Mutation` test technique. You can see more about this topic [on my other repository](https://github.com/derrix060/MutationTestingPresentation#mutation)

To run tests on your computer, just use the following command:

```bash
# It works from python version equal or above 2.7
$ python tests.py
```
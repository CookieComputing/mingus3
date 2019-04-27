# mingus3  &middot; [![Build Status](https://travis-ci.com/CookieComputing/mingus3.svg?branch=master)](https://travis-ci.com/CookieComputing/mingus3)  &middot; ![Issues](https://img.shields.io/github/issues/CookieComputing/mingus3.svg) &middot; ![License](https://img.shields.io/github/license/CookieComputing/mingus3.svg)

## What is this repository?
This repository is a ported and revamped version of the discontinued project 
`mingus`, which is a Python-based music theory library. I had wanted a port 
for mingus to Python 3, but all of the existing repositories that ported 
to Python 3 were either unusable or unmaintained. I took it upon myself 
to port the project and manually adjust for any changes needed 
that weren't addressed by 2 to 3.

As I mentioned before, this is also a continuation of the `mingus` project under
my vision of the project's future. I anticipate that most of the original 
code will remain very similar to it's previous state, but it is also very likely
that I will consider redesigning sections of the project.

## Contributions
I welcome all contributions, be it suggestions, pull requests, or general 
feedback on the project itself. Here's a few remarks regarding some sections
for contributions:

### Issues
Feel free to create any issues regarding your thoughts on the project, as well
as any bugs you happen to discover. Regarding Windows and Mac OSX platforms,
my own development environment is on Ubuntu 19.04, so I cannot guarantee that
all of the features will work on the other target platforms, but I have ran
the code once on Mac OS X immediately after successfully porting the project to 
Python 3, and it seemed to have worked.

### Pull Requests
Pull requests are accepted here, and don't be afraid to provide a PR if you 
think that either the original author or I messed up somewhere, or if you
want to see a new feature being shown.

There are a few things I'd like to see in your PRs:
- If you're introducing a new feature, I would like to see tests for these
features to show both me and the Travis PR build that the feature should work
(at least from a unit test stand point)
- Please run `pylint3` on your code, so that there is consistency with how
the code looks like.

## Original Repository
Once again, this project is forked from 
[the original mingus project](https://github.com/bspaans/python-mingus). Without
their hard work, this project probably would not have existed. Go check out
the original Python 2 project!

## License
The original repository (and this fork) is under the GNU GPL license. Refer
to the License file for more information.


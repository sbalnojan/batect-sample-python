# Batect-Python: Example Batext Usages for Python Development

[batect](https://github.com/charleskorn/batect) is an interesting tool, tackling an issue I've been dealing with.
It's created by a smart guy named Charles Korn.

It contains a bunch of usage examples, but as always I like to start
with really simple examples and work my way up until I really understand
what this is about.

So here:

- example0: I fell in love with how simple it is to shell into a container.
- example1: Is about getting dependencies and running tests, caching locally to
  also be able to do REPL in the same venv.
- more to come

## First, already loving it: Example 0

So first, while setting up this example, I already fell in love with it.

Cd into "example0", then to build & get into the container, simply do:`./batect shell`
and you're in!

`Best Practice: Use a batect "shell" to exec into your built container. You'll need this while setting things up...`

Now let's start a real example.

## The simplest example

A python use case: I have a python 3.7 dummy script here, and I want everyone
to know how to set up this thing, and how to work with it (i.e. by using
pipenv). So I use batect for that, to make sure the unit tests work, no
dependencies go missing, and everyone knows how to set it up.

cd into "example1".
Run:

```
./batect --version
...
```

will download the right version to your computer. We can check the tasks we created:

```
/batect --list-tasks
...
Available tasks:

- dep: Install dependencies via pipenv
- unitTest: Run the unit tests.
```

Nice, so you can then run

```
./batect dep
```

to get the docker image and check whether the dependency installation works.

What we should notice:

- If something breaks, use the option "--no-cleanup-after-failure" to
  let the failed container running to diagnose the issue.
- You could even use the cached container venv to connect to and use basic
  REPL style programming...

## Why?

Polygot programming,..., lots of tools, companies,...

Implementation of the idea:
"You know you're on a mature dev team when your instructions as a new team member are "check out the repo, run ./go, and you're done"." [ThoughtWorks Blog](https://www.thoughtworks.com/insights/blog/praise-go-script-part-i)

"Onboard new team members in minutes: no installation required"

### Alternatives: the Make or shell all the way.

So the "go script" is a great idea. We started to use the "central Makefile" with
a common syntax, and a default "make help" in all projects. But that still left
us to use a bunch of docker-compose to set up everything else.

One way around that is to use something that makes the docker-compose
magic easier, like [Cage](http://cage.faraday.io/) that could work
with different environments (test, dev, prod).

### More cool things & notes on batect

- Override references: Use anchors & mergers together like so:
  &env => <<< merge one env var.
- use option: cached for improved Mac performance.
- on windows: use Unix style paths to be cross-compatible.

```

```

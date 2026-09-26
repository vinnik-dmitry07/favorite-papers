You are using an outdated browser. Please upgrade your browser to improve your experience.

# Why the Third Axis Is Freedom

### Authors/Creators

Bennett, Michael Timothy

## Description

In generative pretraining, a model generates outputs and is updated to minimise the distance between said outputs and known examples. With one output per comparison, a model generating only a small part of the target distribution (generalises poorly) looks no different than a model that has learned the entire target distribution. Explorative Modeling (XM) addresses this by producing (K) outputs per comparison and updates using the closest one. The XM authors claim exploration is a “third pretraining axis” that improves generalisation. Here I prove their proposed scaling axis is actually an indirect intervention on a more general function-space quantity, freedom of function. Directly optimizing for freedom improves ImageNet generation without increasing the exploration budget. Previous work proved maximising freedom maximises probability of generalisation. Here I prove exploration increases freedom. Larger (K) increases measured freedom, and freedom selected the better XM model in 29 of 30 distribution shifts. I reproduced the XM experiments using freedom to guide XM’s ImageNet training loop. Freedom guidance produced better, more varied images than standard XM with model, data, schedule and (K=25) fixed. Freedom reduced Fréchet Inception Distance faster, so the advantage grew with training steps. Put provocatively, generative expressivity is merely a mode-count proxy for freedom, one that discards the very extension structure underlying generalisation. The improvement in XM’s performance using freedom demonstrates this, and the formal proofs serve to explain why. Hence the third pretraining axis is freedom, not exploration.

## Files

### WtTAIF.pdf

### Files (2.8 MB)

Total views

Total downloads

Total data volume

More info on how stats are collected....

## Versions

## External resources

OpenAIRE

## Communities

## Details

#### DOI

#### 10.5281/zenodo.21979851

### Markdown

### reStructuredText

### HTML

### Image URL

### Target URL

## Rights

## Citation

## Export

## Technical metadata

## About

About

Policies

Infrastructure

Principles

Projects

Roadmap

Contact

## Blog

Blog

## Support

Help

FAQ

## Developers

REST API

OAI-PMH

## Contribute

GitHub

Donate

## Funded by

Powered by CERN Data Centre & InvenioRDM

Status

Privacy policy

Cookie policy

Terms of Use

This site uses cookies. Find out more on how we use cookies

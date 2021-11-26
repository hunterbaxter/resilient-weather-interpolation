# Documentation Guide

## Directory Structure

- [Onboarding](./onboarding) contains introductory material to the technical stack
- [Project Proposal](./project_proposal) contains the initial project proposal before starting the project
- [Project Presentation](./project_proposal) contains the class presentation early in development
- [Project Report](./project_report) contains the final report for the project

## Documentation Contribution Guidelines

- Try to make well structured markdown files for all non-presentation or non-submission materials
- For anything that is submitted, use *LaTex* or *Tex* variant (overleaf is a good resource/tool)
- A new sentence should be on a new line (so every time you make a ".", press "enter")

### Creating Documents
```
pdflatex <name>.tex
```
### Creating Presentations

- If markdown was used, can convert to pdf presentation with
```
pandoc <something>.md -t beamer -o <something>.pdf
```
- If *Tex* with *Beamer* was used, can convert to pdf presentation with
```
pdflatex <something>.tex
```

## Source Code Contribution Guidelines

- For commit messages, please follow [Conventional Commits Guidelines](https://www.conventionalcommits.org)
- Follow [Pep8 style guidelines](https://pep8.org/) for python

# Wikidata Biomedical Subgraph 

## Overview
This code acts as the current approach to access and usage of the Wikidata biomedical subgraph for downstream analyses, such as identification of repurposable drug candidates. Older versions of this pipeline commit history can be found [here as WRP](https://github.com/sabahzero/WRP), note [‘Issues’ section](https://github.com/sabahzero/WRP/issues) of repository for potentially relevant task items.
<br>
<br>
Examples of previous applications:<br>
* [Waagmeester et al 2020 eLife](https://elifesciences.org/articles/52614) article, and associated Github repository [WD-rephetio-analysis](https://github.com/SuLab/WD-rephetio-analysis)
* [Mayers et al 2022 Bioinformatics](https://academic.oup.com/bioinformatics/article/38/10/2880/6564220) article, and associated Github repository [MechRepoNet](https://github.com/SuLab/MechRepoNet/)

## Pipeline
There are 18 node types and 41 edge types in this subgraph. Categories are up for discussion as to whether or not they have retained relevancy for when the subgraph is next utilized.<br>

This subgraph is retrieved from Wikidata on January 3rd 2022 utilizing the [Wikibase Dump Filter (WDF)](https://github.com/maxlath/wikibase-dump-filter) json dump tool. Parallel efforts that include RDF dump approaches can be found here from [Biohackathon 2021](https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/21) and [Biohackaton 2022](https://github.com/elixir-europe/biohackathon-projects-2022/tree/main/11).

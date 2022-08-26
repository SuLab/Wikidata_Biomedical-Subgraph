# Wikidata Biomedical Subgraph 

### Contributors and Acknowledgements (alphabetical)
This research is funded under the currently tabled Gene Wiki Project.
<br>
Andra Waagmeester ([@andrawaag](https://github.com/andrawaag)), Andrew I Su ([@andrewsu](https://github.com/andrewsu)), Carolina Gonzalez-Cavazos ([@Carolina1396](https://github.com/Carolina1396)), Jose Emilio Labra Gayo ([@labra](https://github.com/labra)), Kat Thornton ([@emulatingkat](https://github.com/emulatingkat)), Lynn Schriml ([@lschriml](https://github.com/lschriml)), Michael D Mayers ([@mmayers](https://github.com/mmayers12)), Sabah Ul-Hasan ([@sabahzero](https://github.com/sabahzero)), Sai Siddhartha ([@saisiddu](https://github.com/saisiddu)), Seyed Amir Hosseini Beghaeiraveri ([@seyedahbr](https://github.com/seyedahbr)), Tyler Bettilyon ([@tebba-von-mathenstein](https://github.com/tebba-von-mathenstein))

## Overview
This code acts as the current approach to access and usage of the Wikidata biomedical subgraph for downstream analyses, such as identification of repurposable drug candidates. Older versions of this pipeline commit history can be found [here as WRP](https://github.com/sabahzero/WRP), note [‘Issues’ section](https://github.com/sabahzero/WRP/issues) of repository for potentially relevant task items.
<br>
<br>
Examples of previous applications:<br>
* [Waagmeester et al 2020 eLife](https://elifesciences.org/articles/52614) article, and associated Github repository [WD-rephetio-analysis](https://github.com/SuLab/WD-rephetio-analysis)
* [Mayers et al 2022 Bioinformatics](https://academic.oup.com/bioinformatics/article/38/10/2880/6564220) article, and associated Github repository [MechRepoNet](https://github.com/SuLab/MechRepoNet/)

## Pipeline
This subgraph is retrieved from the [Wikidata January 3rd 2022 archive](https://academictorrents.com/details/229cfeb2331ad43d4706efd435f6d78f40a3c438) utilizing the [Wikibase Dump Filter (WDF)](https://github.com/maxlath/wikibase-dump-filter) json dump tool. Parallel efforts that include RDF dump approaches can be found here from [Biohackathon 2021](https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/21) and [Biohackaton 2022](https://github.com/elixir-europe/biohackathon-projects-2022/tree/main/11).

Raw files from Jan 3rd 2022 .json dump through .csv output can be found within the avalanche HPC folder: sulhasan/Wikidata_Biomedical-Subgraph. This folder neighbors code forked from the WD-rephetio-anaylysis Github repository.

There are 18 node types and 41 edge types in this subgraph. Categories are up for discussion as to whether or not they have retained relevancy for when the subgraph is next utilized.<br>

## Reproducibility
Relevant code is available [here](https://github.com/SuLab/Wikidata_Biomedical-Subgraph/blob/main/src/01a-DataUpload.ipynb). All other code available acts as a point of reference that may be applicable downstream or as a means of yielding more efficient output. 
<br>
<br>
<br>
License CC0

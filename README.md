# POPP datasets

This repository contains 3 datasets created within the POPP project ([Project for the Oceration of the Paris Population Census](https://popp.hypotheses.org/#ancre2)) for the task of handwriting text recognition.
These datasets have been publised in [*Recognition and information extraction in historical handwritten tables: toward understanding early 20th century Paris census* at DAS 2022](https://link.springer.com/chapter/10.1007/978-3-031-06555-2_10).

The 3 datasets are called "Generic dataset", "Belleville", and "Chaussée d'Antin" and contains lines made from the extracted rows of census tables from 1926. Each table in the Paris census contains 30 rows, thus each page in these datasets corresponds to 30 lines.

The images are stored in a separate [Git LFS repository](https://git.litislab.fr/tconstum/popp-datasets).
The structure of each dataset is the following:
- double-pages : images of the double pages
- pages:
  - images: images of the pages
  - xml: METS and ALTO files of each page containing the coordinates of the bounding boxes of each line
- lines: contains the labels in the file ```labels.json``` and the line images splitted into the folders *train*, *valid* and *test*.

The double pages were scanned at a resolution of 200dpi and saved as PNG images with 256 gray levels.
The line and page images are shared in the TIFF format, also with 256 gray levels.

Since the lines are extracted from table rows, we defined 4 special characters to describe the structure of the text:
- ¤ : indicates an empty cell
- / : indicates the separation into columns
- ? : indicates that the content of the cell following this symbol is written above the regular baseline
- ! : indicates that the content of the cell following this symbol is written below the regular baseline

We provide a script ```format_dataset.py``` to define which special character you want to use.


The split for the *Generic Dataset* and *Belleville* have been made at the double-page level so that each writer only appears in one subset among train, evaluation and test. The following table summarizes the splits and the number of writers for each dataset:
|      Dataset     | train - # of lines| validation - # of lines | test - # of lines | # of writers |
|:----------------:|:-----:|:----------:|:----:|:------------:|
|      Generic     |  3840 (128 pages)|     480 (16 pages)   |  480  (16 pages)|      80      |
|    Belleville    |  1140 (38 pages)|     150 (5 pages)  |  180 (6 pages)|       1      |
| Chaussée d'Antin |  625  |     78     |  77  |      10      |
## Generic dataset

- This dataset is made 4800 annotated lines extracted from 80 double pages of the 1926 Paris census.
- There is one double page for each of the 80 districts of Paris
- There is one writer per double page so the dataset contains 80 different writers.

## Belleville dataset

This dataset is a mono-writer dataset made of 1470 lines (49 pages) from the *Belleville* district census of 1926.

## Chaussée d'Antin dataset

This dataset is a multi-writer dataset made of 780 lines (26 pages) from the *Chaussée d'Antin* district census of 1926 and written by 10 different writers.

## Terms of Use and Citation Request
This dataset is for non-commercial research purpose. 

License:  This dataset and the corresponding annotations are licensed under a Attribution-NonCommercial-ShareAlike 4.0 International License.

If you publish material based on this database, we request you to include a reference to paper `T. Constum, N. Kempf, T. Paquet, P. Tranouez, C. Chatelain, S. Brée, and F. Merveille,Recognition and information extraction in historical handwritten tables: toward understanding early 20th century Paris census ,Document Analysis Systems (DAS), pp. 143- 157, La Rochelle, 2022.`

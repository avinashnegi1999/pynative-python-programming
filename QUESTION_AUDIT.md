# Question wording audit

Checked on 2026-11-21 against freshly retrieved PYnative exercise-category pages.

## Result

- All 794 local exercise files were paired with questions on their 29 source pages, in page order.
- All exercise title text matches after allowing local numbering and label changes.
- 714 exercises retain source question wording. Their required question text, available input data, and expected-output text match after ignoring HTML layout, Python comment prefixes, list bullets, and whitespace, except the documented database example corrections below.
- The first 80 prompts (Basics and Loops) remain deliberately reworded. Each was reviewed against the original requirements; they are not verbatim copies.
- The gentle hints are independently written and were excluded from source-wording comparisons.
- All existing hints and executable code were preserved. No user answers were run.

## Omissions fixed in this audit

- [Basics exercise 1](01-python-basic-exercise-for-beginners/exercise001.py): restored both example input pairs and their expected outputs; fixed a stray leading dot in the question comment.
- [Basics exercise 15](01-python-basic-exercise-for-beginners/exercise015.py): restored the actual five-row output pattern, which the old file referred to without showing.

## Deliberate differences from the website

- The first 80 prompts use simpler wording, sometimes drawing constraints from the source explanation or examples. Their wording is not presented as an exact transcription.
- Source exercise labels are normalised to local file order. The loop page repeats number 4; the tuple page jumps from 14 to 22. The database page mixes Exercise, Question, and Operation labels.
- [Loop exercise 12](03-python-if-else-and-for-loop-exercise/exercise012.py) keeps the corrected consonant count of 6. The source gives 7 for the same sentence.
- [Database exercise 5](29-python-database-programming-exercise/exercise005.py) keeps a corrected starter-function typo and explains that experience depends on the current date, rather than copying the historical example value as a permanent answer.
- Local reference-image paths replace web image URLs where images were downloaded.
- Website solution blocks, explanatory answer sections, and tutorial reference lists are not part of the question files. Exercise-purpose paragraphs are generally omitted.

## Coverage and original pages

Each row was checked against the linked category page.

| Local folder | Questions | Wording | Original page |
| --- | ---: | --- | --- |
| [01-python-basic-exercise-for-beginners](01-python-basic-exercise-for-beginners/) | 40 | Reworded; requirements reviewed | [PYnative](https://pynative.com/python-basic-exercise-for-beginners/) |
| [03-python-if-else-and-for-loop-exercise](03-python-if-else-and-for-loop-exercise/) | 40 | Reworded; requirements reviewed | [PYnative](https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/) |
| [25-intermediate-python-exercises](25-intermediate-python-exercises/) | 65 | Source wording retained | [PYnative](https://pynative.com/intermediate-python-exercises/) |
| [02-python-input-and-output-exercise](02-python-input-and-output-exercise/) | 23 | Source wording retained | [PYnative](https://pynative.com/python-input-and-output-exercise/) |
| [04-python-functions-exercise](04-python-functions-exercise/) | 18 | Source wording retained | [PYnative](https://pynative.com/python-functions-exercise-with-solutions/) |
| [05-python-string-exercise](05-python-string-exercise/) | 38 | Source wording retained | [PYnative](https://pynative.com/python-string-exercise/) |
| [06-python-list-exercise](06-python-list-exercise/) | 45 | Source wording retained | [PYnative](https://pynative.com/python-list-exercise-with-solutions/) |
| [07-python-dictionary-exercise](07-python-dictionary-exercise/) | 40 | Source wording retained | [PYnative](https://pynative.com/python-dictionary-exercise-with-solutions/) |
| [08-python-set-exercise](08-python-set-exercise/) | 31 | Source wording retained | [PYnative](https://pynative.com/python-set-exercise-with-solutions/) |
| [09-python-tuple-exercise](09-python-tuple-exercise/) | 25 | Source wording retained | [PYnative](https://pynative.com/python-tuple-exercise-with-solutions/) |
| [10-python-data-structure-exercise-for-beginners](10-python-data-structure-exercise-for-beginners/) | 10 | Source wording retained | [PYnative](https://pynative.com/python-data-structure-exercise-for-beginners/) |
| [18-python-comprehensions-exercises](18-python-comprehensions-exercises/) | 25 | Source wording retained | [PYnative](https://pynative.com/python-comprehensions-exercises/) |
| [19-python-collections-module-exercises](19-python-collections-module-exercises/) | 25 | Source wording retained | [PYnative](https://pynative.com/python-collections-module-exercises/) |
| [16-python-date-and-time-exercise](16-python-date-and-time-exercise/) | 30 | Source wording retained | [PYnative](https://pynative.com/python-date-and-time-exercise/) |
| [14-python-object-oriented-programming-oop-exercise](14-python-object-oriented-programming-oop-exercise/) | 31 | Source wording retained | [PYnative](https://pynative.com/python-object-oriented-programming-oop-exercise/) |
| [11-python-exception-handling-exercises](11-python-exception-handling-exercises/) | 20 | Source wording retained | [PYnative](https://pynative.com/python-exception-handling-exercises/) |
| [24-python-math-statistics-exercises](24-python-math-statistics-exercises/) | 30 | Source wording retained | [PYnative](https://pynative.com/python-math-statistics-exercises/) |
| [12-python-file-handling-exercises](12-python-file-handling-exercises/) | 34 | Source wording retained | [PYnative](https://pynative.com/python-file-handling-exercises/) |
| [15-python-os-sys-module-exercises](15-python-os-sys-module-exercises/) | 30 | Source wording retained | [PYnative](https://pynative.com/python-os-sys-module-exercises/) |
| [17-python-regex-exercises](17-python-regex-exercises/) | 30 | Source wording retained | [PYnative](https://pynative.com/python-regex-exercises/) |
| [20-python-lambda-functional-programming-exercises](20-python-lambda-functional-programming-exercises/) | 20 | Source wording retained | [PYnative](https://pynative.com/python-lambda-functional-programming-exercises/) |
| [21-python-iterators-generators-exercises](21-python-iterators-generators-exercises/) | 30 | Source wording retained | [PYnative](https://pynative.com/python-iterators-generators-exercises/) |
| [22-python-itertools-functools-exercises](22-python-itertools-functools-exercises/) | 20 | Source wording retained | [PYnative](https://pynative.com/python-itertools-functools-exercises/) |
| [23-python-random-number-generation-exercise-questions-and-challenge](23-python-random-number-generation-exercise-questions-and-challenge/) | 10 | Source wording retained | [PYnative](https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/) |
| [26-python-numpy-exercise](26-python-numpy-exercise/) | 50 | Source wording retained | [PYnative](https://pynative.com/python-numpy-exercise/) |
| [27-python-pandas-exercise](27-python-pandas-exercise/) | 10 | Source wording retained | [PYnative](https://pynative.com/python-pandas-exercise/) |
| [28-python-matplotlib-exercise](28-python-matplotlib-exercise/) | 10 | Source wording retained | [PYnative](https://pynative.com/python-matplotlib-exercise/) |
| [29-python-database-programming-exercise](29-python-database-programming-exercise/) | 5 | Source wording retained | [PYnative](https://pynative.com/python-database-programming-exercise-with-solution/) |
| [13-python-json-exercise](13-python-json-exercise/) | 9 | Source wording retained | [PYnative](https://pynative.com/python-json-exercise/) |

## Limits

This is a wording, requirement, example-transfer, and coverage audit. It is not an independent correctness proof for every expected result on the website. The first 80 prompts are semantically reviewed paraphrases, not exact quotations. Visual matching of plots and rendering of the GitHub README were not rechecked.

No packages were installed. The audit used parsed source text; HTML layout, tutorial links, solution code, and independently written hints were outside exact-text matching.

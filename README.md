# Python Practice

A topic-wise Python practice library: **794 exercise files across 29 folders**, based on [PYnative's Python exercises](https://pynative.com/python-exercises-with-solutions/).

Each `exerciseN.py` contains the question, available input/output examples, a gentle hint, and space to write your answer. Solution implementations are not supplied.

Folders are numbered `01` through `29` in learning order; individual topics can still contain harder questions.

## Where to start

Start with **Basics → Loops → Functions → Strings → Lists → Dictionaries**. Use Input/Output alongside these whenever you need practice reading values or formatting output.

Then explore Sets, Tuples, and the mixed Data Structures folder. Move into files, error handling, JSON, and classes when those concepts become useful.

This is a reference library, not a requirement to finish all 794 questions. Skip repeated patterns once you can solve them confidently. Several folders begin with simple questions and end with harder ones; you can return to those later.

## Core Python

| Folder | Questions | Types of questions | Purpose | Source |
| --- | ---: | --- | --- | --- |
| [Basics](01-python-basic-exercise-for-beginners/) | 40 | Arithmetic, conditions, digit problems, strings, lists, patterns, introductory files and classes | Get comfortable turning a small problem into Python steps. | [PYnative](https://pynative.com/python-basic-exercise-for-beginners/) |
| [Input and Output](02-python-input-and-output-exercise/) | 23 | User input, number conversion, separators, formatted output, menus, basic file operations | Read inputs correctly and present useful results. | [PYnative](https://pynative.com/python-input-and-output-exercise/) |
| [Loops and Conditions](03-python-if-else-and-for-loop-exercise/) | 40 | `for` and `while`, `break`/`continue`, patterns, number sequences, filtering, nested loops | Practise repetition, decisions, and tracking changing values. | [PYnative](https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/) |
| [Functions](04-python-functions-exercise/) | 18 | Parameters, return values, default arguments, `*args`, nested functions, recursion, higher-order functions | Break a problem into reusable pieces with clear inputs and outputs. | [PYnative](https://pynative.com/python-functions-exercise-with-solutions/) |
| [Strings](05-python-string-exercise/) | 38 | Indexing, slicing, character counts, searching, whitespace, symbol replacement, rotations | Work with text and build basic text-processing logic. | [PYnative](https://pynative.com/python-string-exercise/) |
| [Lists](06-python-list-exercise/) | 45 | Adding/removing items, slicing, traversal, filtering, sorting, comprehensions, subsets | Manage ordered collections and practise common sequence problems. | [PYnative](https://pynative.com/python-list-exercise-with-solutions/) |
| [Dictionaries](07-python-dictionary-exercise/) | 40 | Key/value operations, mapping lists, merging, nested data, filtering, copying | Organise records and look up information by key. | [PYnative](https://pynative.com/python-dictionary-exercise-with-solutions/) |
| [Sets](08-python-set-exercise/) | 31 | Unique values, membership, union, intersection, differences, subsets | Recognise problems involving uniqueness and relationships between groups. | [PYnative](https://pynative.com/python-set-exercise-with-solutions/) |
| [Tuples](09-python-tuple-exercise/) | 25 | Packing/unpacking, slicing, nesting, mapping, named tuples, hashability | Understand immutable sequences and how they differ from lists. | [PYnative](https://pynative.com/python-tuple-exercise-with-solutions/) |
| [Mixed Data Structures](10-python-data-structure-exercise-for-beginners/) | 10 | Combining lists, sets, and dictionaries; counting, removing duplicates, membership checks | Choose and combine the right collection for a problem. | [PYnative](https://pynative.com/python-data-structure-exercise-for-beginners/) |

## Working with programs and data

| Folder | Questions | Types of questions | Purpose | Source |
| --- | ---: | --- | --- | --- |
| [Exception Handling](11-python-exception-handling-exercises/) | 20 | `try`/`except`, division errors, multiple exceptions, input validation, re-raising, generator/thread errors | Handle expected failures without hiding the underlying problem. | [PYnative](https://pynative.com/python-exception-handling-exercises/) |
| [File Handling](12-python-file-handling-exercises/) | 34 | Reading/writing, counting contents, file size, filtering logs, splitting files | Read, process, and save information beyond a program's runtime. | [PYnative](https://pynative.com/python-file-handling-exercises/) |
| [JSON](13-python-json-exercise/) | 9 | Encoding/decoding, nested values, sorting keys, validation, object conversion | Work with structured data commonly used in APIs and configuration. | [PYnative](https://pynative.com/python-json-exercise/) |
| [Object-Oriented Programming](14-python-object-oriented-programming-oop-exercise/) | 31 | Classes, attributes, methods, inheritance, polymorphism, small models such as vehicles and playlists | Group related data and behaviour into objects. | [PYnative](https://pynative.com/python-object-oriented-programming-oop-exercise/) |
| [OS and Sys](15-python-os-sys-module-exercises/) | 30 | Directories, paths, environment variables, directory traversal, process exit, file search | Write scripts that interact with the filesystem and runtime environment. | [PYnative](https://pynative.com/python-os-sys-module-exercises/) |
| [Date and Time](16-python-date-and-time-exercise/) | 30 | Parsing/formatting dates, date differences, time arithmetic, time zones, working days | Represent and calculate dates and times correctly. | [PYnative](https://pynative.com/python-date-and-time-exercise/) |
| [Regular Expressions](17-python-regex-exercises/) | 30 | Character rules, repetitions, boundaries, validation, extracting numbers, replacements | Recognise and transform text that follows a pattern. | [PYnative](https://pynative.com/python-regex-exercises/) |

## Deeper Python and mixed challenges

| Folder | Questions | Types of questions | Purpose | Source |
| --- | ---: | --- | --- | --- |
| [Comprehensions](18-python-comprehensions-exercises/) | 25 | List/dict/set comprehensions, filtering, nested combinations, grouping, generator comparisons | Express collection transformations clearly once ordinary loops are familiar. | [PYnative](https://pynative.com/python-comprehensions-exercises/) |
| [Collections Module](19-python-collections-module-exercises/) | 25 | `Counter`, `defaultdict`, `OrderedDict`, `deque`, `namedtuple`, queues, cache exercises | Use specialised standard-library containers instead of rebuilding their behaviour. | [PYnative](https://pynative.com/python-collections-module-exercises/) |
| [Lambda and Functional Programming](20-python-lambda-functional-programming-exercises/) | 20 | Lambdas, sorting keys, `map`, `filter`, composition, caching, higher-order functions | Pass behaviour as a value and combine small transformations. | [PYnative](https://pynative.com/python-lambda-functional-programming-exercises/) |
| [Iterators and Generators](21-python-iterators-generators-exercises/) | 30 | Custom iteration, `yield`, lazy sequences, file readers, `send`, stream interleaving, cleanup | Process values one at a time and understand iteration state. | [PYnative](https://pynative.com/python-iterators-generators-exercises/) |
| [Itertools and Functools](22-python-itertools-functools-exercises/) | 20 | Permutations, combinations, grouping, chaining, reduction, partial functions, lazy pipelines | Reuse tools for iteration, combinations, and callable behaviour. | [PYnative](https://pynative.com/python-itertools-functools-exercises/) |
| [Random Data](23-python-random-number-generation-exercise-questions-and-challenge/) | 10 | Random numbers, sampling, characters, passwords, dice, random dates | Practise generating test data and understanding reproducible randomness. | [PYnative](https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/) |
| [Math and Statistics](24-python-math-statistics-exercises/) | 30 | Roots, powers, geometry, mean/median/mode, quartiles, distributions, regression, outliers | Apply Python's numerical standard-library tools to calculations and analysis. | [PYnative](https://pynative.com/python-math-statistics-exercises/) |
| [Intermediate Challenges](25-intermediate-python-exercises/) | 65 | Mixed collections, comprehensions, linked lists, decorators, caching, dataclasses, concurrency, patterns | Combine concepts after you have practised the individual topics. | [PYnative](https://pynative.com/intermediate-python-exercises/) |

## Specialist tracks

Pick these when the topic interests you; they are separate directions you can explore.

| Folder | Questions | Types of questions | Purpose | Source |
| --- | ---: | --- | --- | --- |
| [NumPy](26-python-numpy-exercise/) | 50 | Array creation, reshaping, slicing, masks, indexing, missing values, numerical summaries | Work with numerical arrays and operations across many values. | [PYnative](https://pynative.com/python-numpy-exercise/) |
| [Pandas](27-python-pandas-exercise/) | 10 | Inspecting/cleaning CSV data, filtering rows, grouping, averages, sorting, joining tables | Practise tabular data analysis with DataFrames. | [PYnative](https://pynative.com/python-pandas-exercise/) |
| [Matplotlib](28-python-matplotlib-exercise/) | 10 | Line, scatter, bar, histogram, pie, subplot, and stacked plots; styling and saving figures | Communicate data through charts. | [PYnative](https://pynative.com/python-matplotlib-exercise/) |
| [Databases](29-python-database-programming-exercise/) | 5 | Connecting, reading hospital/doctor records, parameterised filters, updating experience | Connect Python to a relational database and practise queries and updates. | [PYnative](https://pynative.com/python-database-programming-exercise-with-solution/) |

## How to use a question file

1. Open a topic folder and choose an `exerciseN.py` file.
2. Read the question and examples under `# ========question========`.
3. Write your answer below `# Write your code below.`.
4. Read `# ========hints========` when stuck. Hints are plain comments and remain visible.
5. Run the file and compare your result with the example.

From this repository's root in PowerShell, for example:

```powershell
python .\python-functions-exercise\exercise1.py
```

Some existing files may already contain your attempts. Keep improving those answers as you learn.

## Datasets and setup

- **Pandas:** `Automobile_data.csv` and reference images are included in its folder.
- **Matplotlib:** `company_sales_data.csv` and reference images are included in its folder.
- **Databases:** `setup.sql` supplies the hospital/doctor tables and sample records for SQLite. Read that folder's `SETUP.md` first.
- Run data exercises from their folder, or resolve data paths relative to your script.
- Some file exercises ask you to create sample files yourself.
- NumPy, Pandas, and Matplotlib exercises require their respective packages. Some other questions may specify additional dependencies; none were installed automatically.
- For questions that overwrite or delete files, use disposable practice files.

## About the collection

Question counts reflect the exercise files actually present. The tuple source skips numbers 15–21, so its 25 local files are numbered consecutively; affected files record the original source number. The loops source repeats number 4; local files use consecutive numbering.

Questions and examples come from PYnative. A full wording audit checked all 794 exercises against their source pages: 714 retain source wording; the first 80 have reworded prompts, checked for matching requirements. Gentle hints remain independently written. See [QUESTION_AUDIT.md](QUESTION_AUDIT.md) for the comparison method, fixed omissions, and documented source errors. Example results were compared with the pages, not all independently recalculated.

See [EXERCISES.md](EXERCISES.md) for the compact folder index.

**Source:** [PYnative Python Exercises](https://pynative.com/python-exercises-with-solutions/)

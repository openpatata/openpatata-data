
* [required] **`belongs_to`** (`array [string]`)

    A list of identifiers of bills this report is on.

* **`date`** (`string|null`)

    The date that appears after a report, in ISO format (YYYY-MM-DD).

* [required] **`mps_present`** (`array [object]`)

    A list of MPs who were present.

    * [required] **`name`** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **`note`** (`string|null`)

        What appears next to their name, e.g. 'πρόεδρος'.

* **`reps_present`** (`array [object]|null`)

    A list of represenatives who were present. Omit or leave blank if not applicable.

    * [required] **`name`** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **`note`** (`string|null`)

        What appears next to their name, e.g. 'πρόεδρος'.

* [required] **`text`** (`string`)

    The actual report, in Markdown.

* [required] **`title`** (`string`)

    The title of the report.

* **`url`** (`string|null`)

    A link to the report on parliament.

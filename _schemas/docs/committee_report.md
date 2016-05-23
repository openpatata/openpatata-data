* **_id** (`string`)

* [required] **_sources** (`array [string]`)

* [required] **date_circulated** (`string`)

    The date when the report was circulated in the plenary, in the ISO format (YYYY-MM-DD).

* **date_prepared** (`string|null`)

    The date that appears after a report, in the ISO format (YYYY-MM-DD).

* **mps_present** (`array [object]`)

    A list of MPs who were present.

    * [required] **name** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **note** (`string|null`)

        What appears next to their name, e.g. 'πρόεδρος'.

* **relates_to** (`array [string|null]`)

    A list of identifiers of bills this report relates to.

* **reps_present** (`array [object]|null`)

    A list of represenatives who were present. Omit or leave blank if not applicable.

    * [required] **name** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **note** (`string|null`)

        What appears next to their name, e.g. 'πρόεδρος'.

* **text** (`string|null`)

    The actual report, in Markdown.

* [required] **title** (`string`)

    The title of the report.

* [required] **url** (`string|null`)

    A link to the report on Parliament.

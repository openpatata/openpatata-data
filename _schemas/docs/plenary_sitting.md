
* [required] **`agenda`** (`object`)

    The day's agenda.

    * [required] **`debate`** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 4 of the agenda.

    * [required] **`legislative_work`** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 1 of the agenda.

* [required] **`date`** (`string`)

    The date the plenary was held on, in ISO format (YYYY-MM-DD).

* **`links`** (`array [object]`)

    Links to relevant pages. Currently either the agenda as published, or the transcript.

    * [required] **`type`** (`string`)

        The type of resource.

        One of:

        * agenda
        * transcript

    * [required] **`url`** (`string`)

        The link.

* **`mps_present`** (`array [string]|boolean|null`)

    A list of MPs who were present.

* [required] **`parliament`** (`string`)

    The number of the parliament, e.g. 'Ι΄'.

* **`reps_present`** (`array [string]|boolean|null`)

    A list of religious representatives who were present. Set to `false` if none where present; otherwise, leave blank or omit.

* **`session`** (`string|null`)

    The number of this parliament's session, e.g. 'Γ΄'.

* **`sitting`** (`number|null`)

    The number of this sitting, e.g. '5'.

* [required] **`type`** (`string`)

    The type of sitting.

    One of:

    * ordinary
    * extraordinary
    * special

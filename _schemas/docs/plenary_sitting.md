
* [required] **agenda** (`object`)

    The day's agenda.

    * [required] **debate** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 4 of the agenda.

    * [required] **legislative_work** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 1 of the agenda.

* [required] **date** (`string`)

    The date the plenary was held on, in ISO format (YYYY-MM-DD).

* **links** (`array [object]`)

    Links to relevant pages. Currently either the agenda as published, or the transcript.

    * [required] **type** (`string`)

        The type of resource.

        One of:

        * agenda
        * transcript

    * [required] **url** (`string`)

        The link.

* **mps_present** (`array [string]|boolean|null`)

    A list of MPs who were present.

* [required] **parliament** (`string`)

    The number of the parliament, as published on the agenda, e.g. 'Ι΄'. This signifies the whole period between elections.

* **reps_present** (`array [string]|boolean|null`)

    A list of religious representatives who were present. Set to `false` if none were present; otherwise, leave blank or omit.

* **session** (`string|null`)

    The current legislative session, as published on the agenda, e.g. 'Γ΄'. A session lasts a year. If the sitting is of type `special`, it might fall outside a session.

* **sitting** (`number|null`)

    The number of this sitting, as published on the agenda, e.g. '5'. If the sitting is of type `special`, it might not be numbered.

* [required] **type** (`string`)

    The type of sitting.

    One of:

    * ordinary
    * extraordinary
    * special

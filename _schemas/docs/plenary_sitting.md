* [required] **_sources** (`array [string]`)

* [required] **agenda** (`object`)

    The day's agenda.

    * [required] **debate** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 4 of the agenda.

    * [required] **legislative_work** (`array [string]|boolean`)

        A list of identifiers of items on Chapter 1 of the agenda.

* [required] **attendees** (`array [string]|boolean|null`)

    A list of MPs who were present at the meeting.

* [required] **date** (`string`)

    The date the plenary was held on, in ISO format (YYYY-MM-DD).

* [required] **links** (`array [object]`)

    Links to relevant pages. Currently either the agenda as published, or the transcript.

    * [required] **type** (`string`)

        The type of resource.

        One of:

        * agenda
        * transcript

    * [required] **url** (`string`)

        The link.

* [required] **parliamentary_period** (`string`)

    The parliamentary period, as published on the agenda, e.g. 'Ι'. This signifies the entire period between elections.

* [required] **session** (`string|null`)

    The current legislative session, as published on the agenda, e.g. 'Γ'. A session lasts a year. If the sitting is of type `special`, it might fall outside a session.

* [required] **sitting** (`number|null`)

    The number of this sitting, as published on the agenda, e.g. '5'. If the sitting is of type `special`, it might not be numbered.

* [required] **type** (`string`)

    The type of sitting.

    One of:

    * ordinary
    * extraordinary
    * special

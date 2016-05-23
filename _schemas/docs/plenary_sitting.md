* **_id** (`string`)

* [required] **_sources** (`array [string]`)

* [required] **agenda** (`object`)

    The day's agenda.

    * [required] **cap1** (`array [string]|boolean`)

        A list of the numbers of documents on Chapter 1 of the agenda.

    * [required] **cap2** (`array [string]|boolean`)

        A list of the numbers of documents on Chapter 2 of the agenda.

    * [required] **cap4** (`array [string]|boolean`)

        A list of the numbers of documents on Chapter 4 of the agenda.

* [required] **attendees** (`array [string]|boolean`)

    A list of MPs who were present at the meeting.

* [required] **date** (`string`)

    The date the plenary was held on, in the ISO format (YYYY-MM-DD).

* [required] **links** (`array [object]`)

    Links to relevant documents.  Either the source of the agenda or the transcript.

    * [required] **type** (`string`)

        The type of resource.

        One of:

        * agenda
        * transcript

    * [required] **url** (`string`)

        The link.

* [required] **parliamentary_period_id** (`string`)

    The parliamentary period, as published on the agenda, e.g. 'Ι'.  The parliamentary period is the period between elections.

* [required] **session** (`string|null`)

    The legislative session, as published on the agenda, e.g. 'Γ'.  The session is the time during which Parliament regularly meet.  They take a break between July and August, and a new session is convened every September.  Extraordinary sittings may be held outside of a session.

* [required] **sitting** (`number|null`)

    The number of the sitting, as published on the agenda, e.g. '5'. Extraordinary sittings may not carry a number.

* **type** (`string`)

    The type of sitting.

    One of:

    * ordinary
    * extraordinary
    * special

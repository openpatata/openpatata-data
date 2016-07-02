* **_id** (`string`)

* **_position_on_page** (`number`)

* [required] **_sources** (`array [string]`)

* [required] **answers** (`array [string]`)

    URL to the answer(s) on Parliament's website.

* [required] **by** (`array [object]`)

    The name(s) of the MP(s) asking the question.

    * **mp_id** (`string`)

        The `id` of the asking MP.

* [required] **date** (`string`)

    Date when the question was asked.

* [required] **heading** (`string`)

    The heading of the question.

* [required] **identifier** (`string`)

    The question's number.

* [required] **text** (`string`)

    The question itself, formatted in Markdown.

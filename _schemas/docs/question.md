* [required] **answers** (`array [string]`)

    URL to the answer(s) on parliament's website.

* [required] **identifier** (`string`)

    The question's tracking identifier.

* [required] **question** (`object`)

    The question posed by the MP(s).

    * [required] **by** (`array [string]`)

        The names of the MPs asking the question.

    * [required] **date** (`string`)

        Date the question was asked.

    * [required] **text** (`string`)

        The question itself, formatted in Markdown.

    * [required] **title** (`string`)

        The heading of the question.

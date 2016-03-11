* **actions** (`array [object]`)

    A list of actions parliament has taken on this bill, in chronological order.  An action must be one of the following predefined types.

    Each item must be compliant with exactly one of:

    * 

        * [required] **action** (`string`)

            One of:

            * submission

        * [required] **at_plenary** (`string`)

            The plenary sitting's unique id.

        * [required] **committees_referred_to** (`string`)

            The committees the bill was referred to.

        * [required] **sponsors** (`string`)

            The bill's sponsors.

* **explanatory_note** (`object|null`)

    An accompanying explanatory note as published in the Government Gazette.

    * [required] **authors** (`array [object]`)

        The author(s) of the note.

        * [required] **name** (`string`)

            The name of the author, in Greek, in the following order: last name, middle name, first name.

        * **note** (`string|null`)

            What's written under the author's name, usually the capacity in which they're proposing a bill.

    * [required] **in** (`object`)

        Where the note can be found in the Gazette.

        * [required] **issue** (`integer`)

            The issue of the Gazette.

        * [required] **pages** (`string|number`)

            Page or page range where the note has been printed. If a page range is used, separate pages with an en dash, e.g. '546–7'.

    * [required] **text** (`string`)

        The note itself, in Markdown.

* [required] **identifier** (`string`)

    The bill's number assigned to it by parliament.

* **law** (`string|null`)

    The law number, if the bill has been enacted.

* **sources** (`array [object]|null`)

    A list of references used by editors in prose (e.g. in the `summary` field), or anywhere you might wanna direct readers.

    * **id** (`string|null`)

        A keyword for this source, to be used as an anchor. Not required if not a reference.

    * [required] **text** (`string`)

        The source, in Markdown.

* **status** (`string|null`)

    The status of the bill.

    One of:

    * pass
    * fail
    * withdrawn
    * pending

* **summary** (`string|null`)

    A summary of this bill authored by an editor, in Markdown.

* [required] **title** (`string`)

    The title of this bill. This should be the title used in parliament, which may be different from the title of the law, if the bill has been enacted.

* **votes** (`array [object]`)

    * **breakdown** (`array [object]`)

        Individual MP votes; inferred.

        * [required] **name** (`string`)

            The name of the MP, in Greek, in the following order: last name, middle name, first name.

        * [required] **option** (`string`)

            Whether the MP has voted for or against, or abstained.

            One of:

            * yes
            * no
            * abstain

    * [required] **counts** (`array`)

        Official counts. Options must be in the following order: yes, no, abstain. This is to ensure that there is only one of each option.

        1. 

            * [required] **count** (`integer`)

                The vote tally for this `option`.

            * [required] **option** (`string`)

                Whether this option is for MPs who've voted for or against, or abstained.

                One of:

                * yes

        1. 

            * [required] **count** (`integer`)

                The vote tally for this `option`.

            * [required] **option** (`string`)

                Whether this option is for MPs who've voted for or against, or abstained.

                One of:

                * no

        1. 

            * [required] **count** (`integer`)

                The vote tally for this `option`.

            * [required] **option** (`string`)

                Whether this option is for MPs who've voted for or against, or abstained.

                One of:

                * abstain

    * **remarks** (`string`)

        Editor remarks.

    * [required] **result** (`string`)

        The outcome of the vote.

        One of:

        * pass
        * fail

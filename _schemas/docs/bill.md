
* **`actions`** (`array [object]`)

    A list of actions parliament has taken on this bill, in chronological order. An action must be one of the following predefined types.

    Each item must be compliant with exactly one of:

    * 

        * [required] **`action`** (`string`)

            One of:

            * submit

        * [required] **`by`** (`array [string]`)

            The bill's sponsors.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

    * 

        * [required] **`action`** (`string`)

            One of:

            * refer

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * [required] **`to`** (`array [object]`)

            The committees the bill has been referred to.

            * [required] **`el`** (`string`)

                The name of the committee in Greek.

            * [required] **`en`** (`string`)

                The name of the committee in English.

    * 

        * [required] **`action`** (`string`)

            One of:

            * resubmit

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

    * 

        * [required] **`action`** (`string`)

            One of:

            * postpone

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * [required] **`what`** (`string`)

            Stage at which the bill was postponed.

            One of:

            * second reading
            * third reading
            * veto

    * 

        * [required] **`action`** (`string`)

            One of:

            * vote

        * **`breakdown`** (`array [object]`)

            Individual MP votes; inferred.

            * [required] **`name`** (`string`)

                The name of the MP, in Greek, in the following order: last name, middle name, first name.

            * [required] **`option`** (`string`)

                Whether the MP has voted for or against, or abstained.

                One of:

                * yes
                * no
                * abstain

        * **`counts`** (`array`)

            Official counts. Options must be in the following order: yes, no, abstain. This is to ensure that there is only one of each option.

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of:

                    * yes

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of:

                    * no

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of:

                    * abstain

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * **`motion`** (`string`)

            The motion, word-for-word.

        * **`remarks`** (`string`)

            Editor remarks.

        * [required] **`result`** (`string`)

            The outcome of the vote.

            One of:

            * pass
            * fail

        * [required] **`type`** (`string`)

            The "type" of vote.

            One of:

            * second reading
            * third reading
            * veto

    * 

        * [required] **`action`** (`string`)

            One of:

            * other

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * [required] **`description`** (`object`)

            A brief description of this action.

            * [required] **`el`** (`string`)

                The description in Greek.

            * [required] **`en`** (`string`)

                The description in English.

* **`explanatory_note`** (`object|null`)

    An accompanying explanatory note published in the Government Gazette.

    * [required] **`authors`** (`array [object]`)

        The author(s) of the note.

        * [required] **`name`** (`string`)

            The name of the author, in Greek, in the following order: last name, middle name, first name.

        * **`note`** (`string|null`)

            What's written under the author's name, usually the capacity in which they're proposing a bill.

    * [required] **`in`** (`object`)

        Where the note is found in the Gazette.

        * [required] **`issue`** (`integer`)

            The issue of the Gazette.

        * [required] **`pages`** (`string|number`)

            Page or page range where the note has been printed. If a page ranged is used, separate pages with an en dash, e.g. '546–7'.

    * [required] **`text`** (`string`)

        The note itself, in Markdown.

* [required] **`identifier`** (`string`)

    The bill's unique identifier assigned to it by parliament.

* **`law`** (`string|null`)

    The law number, if the bill has been enacted.

* **`sources`** (`array [object]|null`)

    A list of references used by editors in prose (e.g. in the `summary` field), or anywhere you might wanna direct readers.

    * **`id`** (`string|null`)

        A keyword for this source, to be used as an anchor. Not required if not a reference.

    * [required] **`text`** (`string`)

        The source, in Markdown.

* **`status`** (`string|null`)

    The status of the bill.

    One of:

    * pass
    * fail
    * withdrawn
    * pending

* **`summary`** (`string|null`)

    A summary of this bill authored by an editor, in Markdown.

* [required] **`title`** (`string`)

    The title of this bill. This should be the title used in parliament, which may be different from the title of the law, if the bill has been enacted.

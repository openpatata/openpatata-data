
## bill.yaml

* **`actions`** (`array`)

    A list of actions parliament has taken on this bill, in chronological order. An action must be one of the following predefined types.

    Each item must be compliant with exactly one of:

    * 

        * [required] **`action`** (`string`)

            One of: 'submit'.

        * [required] **`by`** (`array`)

            The bill's sponsors.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).
    * 

        * [required] **`action`** (`string`)

            One of: 'refer'.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * [required] **`to`** (`array`)

            The committees the bill has been referred to.

            * [required] **`el`** (`string`)

                The name of the committee in Greek.

            * [required] **`en`** (`string`)

                The name of the committee in English.
    * 

        * [required] **`action`** (`string`)

            One of: 'resubmit'.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).
    * 

        * [required] **`action`** (`string`)

            One of: 'postpone'.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * [required] **`what`** (`string`)

            Stage at which the bill was postponed.

            One of: 'second reading', 'third reading', 'veto'.
    * 

        * [required] **`action`** (`string`)

            One of: 'vote'.

        * **`breakdown`** (`array`)

            Individual MP votes; inferred.

            * [required] **`name`** (`string`)

                The name of the MP, in Greek, in the following order: last name, middle name, first name.

            * [required] **`option`** (`string`)

                Whether the MP has voted for or against, or abstained.

                One of: 'yes', 'no', 'abstain'.

        * **`counts`** (`array`)

            Official counts. Options must be in the following order: yes, no, abstain. This is to ensure that there is only one of each option.

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of: 'yes'.

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of: 'no'.

            1. 

                * [required] **`count`** (`integer`)

                    The vote tally for this `option`.

                * [required] **`option`** (`string`)

                    Whether this option is for MPs who've voted for or against, or abstained.

                    One of: 'abstain'.

        * [required] **`date`** (`string`)

            The date, in ISO format (YYYY-MM-DD).

        * **`motion`** (`string`)

            The motion, word-for-word.

        * **`remarks`** (`string`)

            Editor remarks.

        * [required] **`result`** (`string`)

            The outcome of the vote.

            One of: 'pass', 'fail'.

        * [required] **`type`** (`string`)

            The "type" of vote.

            One of: 'second reading', 'third reading', 'veto'.
    * 

        * [required] **`action`** (`string`)

            One of: 'other'.

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

    * [required] **`authors`** (`array`)

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

        The note itself.

* [required] **`identifier`** (`string`)

    The bill's unique identifier assigned to it by parliament.

* **`law`** (`string|null`)

    The law number, if the bill has been enacted.

* **`sources`** (`array|null`)

    A list of references used by editors in prose (e.g. in the `summary` field), or anywhere you might wanna direct readers.

    * **`id`** (`string|null`)

        A keyword for this source, to be used as an anchor. Not required if not a reference.

    * [required] **`text`** (`string`)

        The source, in Markdown.

* **`status`** (`string|null`)

    The status of the bill.

    One of: 'pass', 'fail', 'withdrawn', 'pending'.

* **`summary`** (`string|null`)

    A summary of this bill authored by an editor, in Markdown.

* [required] **`title`** (`string`)

    The title of this bill. This should be the title used in parliament, which may be different from the title of the law, if the bill has been enacted.

## committee_report.yaml

* [required] **`belongs_to`** (`array`)

    A list of identifiers of bills this report is on.

* **`date`** (`string|null`)

    The date that appears after a report, in ISO format (YYYY-MM-DD).

* [required] **`mps_present`** (`array`)

    A list of MPs who were present.

    * [required] **`name`** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **`note`** (`string|null`)

        What appears under their name, e.g. 'πρόεδρος'.

* **`reps_present`** (`array|null`)

    A list of represenatives who were present. Omit or leave blank if not applicable.

    * [required] **`name`** (`string`)

        Their name, in Greek, in the following order: last name, middle name, first name.

    * **`note`** (`string|null`)

        What appears under their name, e.g. 'πρόεδρος'.

* [required] **`text`** (`string`)

    The actual report, in Markdown.

* [required] **`title`** (`string`)

    The title of the report.

* **`url`** (`string|null`)

    A link to the report on parliament.

## mp.yaml

* **`links`** (`array|null`)

    A list of pertinent links, e.g. the MP's page on parliament. No more than five. If linking to Wikipedia, link only to one language version of it, preferably English.

    * [required] **`note`** (`object`)

        * [required] **`el`** (`string`)

            A very short description of this link in Greek.

        * [required] **`en`** (`string`)

            A very short description of this link in English.

    * [required] **`url`** (`string`)

        The link itself.

* **`mugshot`** (`string|null`)

    A link to the MP's mugshot on parliament's website. Use the highest resolution available. Omit or leave blank if there isn't one.

* [required] **`name`** (`object`)

    The MP's name.

    * [required] **`el`** (`string`)

        Their name in Greek, in the following order: last name, middle name, first name.

    * [required] **`en`** (`string`)

        Their name in English, ISO 843-transliterated, in the following order: last name, middle name, first name.

* [required] **`tenures`** (`array`)

    The MP's tenures in parliament, from 2001 onwards.

    * [required] **`district`** (`object`)

        District served.

        * [required] **`el`** (`string`)

            The name of the district in Greek.

        * [required] **`en`** (`string`)

            The name of the district in English, ISO 843-transliterated from Greek.

    * [required] **`end`** (`string|null`)

        The end date, in ISO format (YYYY-MM-DD). Leave blank if MP currently in office.

    * [required] **`parl_group`** (`string|null`)

        The parliament group the MP is affiliated to, if any; otherwise blank.

    * [required] **`start`** (`string`)

        The start date, in ISO format (YYYY-MM-DD).

## plenary_sitting.yaml

* [required] **`agenda`** (`object`)

    The day's agenda.

    * [required] **`debate`** (`array|boolean`)

        A list of identifiers of items on Chapter 4 of the agenda.

    * [required] **`legislative_work`** (`array|boolean`)

        A list of identifiers of items on Chapter 1 of the agenda.

* [required] **`date`** (`string`)

    The date the plenary was held on, in ISO format (YYYY-MM-DD).

* **`links`** (`array`)

    Links to relevant pages. Currently either the agenda as published, or the transcript.

    * [required] **`type`** (`string`)

        The type of resource; either an `agenda` or a `transcript`.

        One of: 'agenda', 'transcript'.

    * [required] **`url`** (`string`)

        The link.

* **`mps_present`** (`array|boolean|null`)

    A list of MPs who were present.

* [required] **`parliament`** (`string`)

    The number of the parliament, e.g. 'Ι΄'.

* **`reps_present`** (`array|boolean|null`)

    A list of religious representatives who were present. Set to `false` if none where present; otherwise, leave blank or omit.

* **`session`** (`string|null`)

    The number of this parliament's session, e.g. 'Γ΄'.

* **`sitting`** (`number|null`)

    The number of this sitting, e.g. '5'.

* [required] **`type`** (`string`)

    The type of sitting.

    One of: 'ordinary', 'extraordinary', 'special'.

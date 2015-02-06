
* **dofi** (`string|null`)

    Link to the MP's latest declaration of financial interests.

* **links** (`array [object]|null`)

    A list of pertinent links, e.g. the MP's page on parliament. Generally, no more than five. If linking to Wikipedia, link only to one language version of it, preferably English.

    * [required] **note** (`object`)

        * [required] **el** (`string`)

            A very short description of this link in Greek.

        * [required] **en** (`string`)

            A very short description of this link in English.

    * [required] **url** (`string`)

        The link itself.

* **mugshot** (`string|null`)

    A link to the MP's mugshot on parliament's website. Use the highest resolution available.

* [required] **name** (`object`)

    The MP's name.

    * [required] **el** (`string`)

        Their name in Greek, in the following order: last name, middle name, first name.

    * [required] **en** (`string`)

        Their name in English, ISO 843-transliterated, in the following order: last name, middle name, first name.

* [required] **tenures** (`array [object]`)

    The MP's tenures in parliament.

    * [required] **district** (`object`)

        District served.

        * [required] **el** (`string`)

            The name of the district in Greek.

        * [required] **en** (`string`)

            The name of the district in English, ISO 843-transliterated from Greek.

    * [required] **end_date** (`string|null`)

        The end date, in ISO format (YYYY-MM-DD). Leave blank if MP currently in office.

    * [required] **parl_group** (`string|null`)

        The parliament group the MP is affiliated to, if any; otherwise blank.

    * [required] **start_date** (`string`)

        The start date, in ISO format (YYYY-MM-DD).

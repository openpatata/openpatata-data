* **_sources** (`array [string]`)

* **birth_date** (`string|null`)

    Their date of birth in the ISO format.

* **dofi** (`string|null`)

    A link to the MP's latest declaration of financial interests.

* **email** (`string|null`)

    Official e-mail address.

* **gender** (`string`)

    See [`foaf:gender`](http://xmlns.com/foaf/spec/#term_gender).

* **links** (`array [object]|null`)

    A list of pertinent links, e.g. to the MP's page on Parliament.  Generally no more than five.  If linking to Wikipedia, link only to one language edition of it, preferably the English Wikipedia.

    * [required] **note** (`object`)

        * [required] **el** (`string`)

            A brief description in Greek.

        * [required] **en** (`string`)

            A brief description in English.

    * [required] **url** (`string`)

        The link itself.

* **mugshot** (`string|null`)

    A link to the MP's head shot on Parliament. Use the highest resolution available.

* [required] **name** (`object`)

    The MP's name.

    * [required] **el** (`string`)

        Their name in Greek, in the following order: last name, middle name, first name.

    * [required] **en** (`string`)

        Their name in English, ISO 843-transliterated, in the following order: last name, middle name, first name.

* **other_names** (`array [object]|null`)

    Alternate names and spellings.

    * [required] **name** (`string`)

        The name itself.

    * [required] **note** (`string`)

        What sort of name is it?

* [required] **tenures** (`array [object]`)

    The MP's tenures in parliament.

    * [required] **district** (`object`)

        The district served.

        * [required] **el** (`string`)

            The name of the district in Greek.

        * [required] **en** (`string`)

            The name of the district in English, ISO 843-transliterated from Greek.

    * [required] **end_date** (`string|null`)

        The end date, in ISO format (YYYY-MM-DD).  Leave blank if MP currently in office.

    * [required] **parl_group** (`object|null`)

        The parliament group the MP is affiliated to, if any; otherwise leave blank.

        * [required] **el** (`string`)

            Name in Greek.

        * [required] **en** (`string`)

            Name in Eglish, ISO 843-transliterated from the Greek.

    * [required] **start_date** (`string`)

        The start date, in ISO format (YYYY-MM-DD).

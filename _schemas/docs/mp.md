* **_sources** (`array [string]`)

* **birth_date** (`string|null`)

    Their date of birth in the ISO format.

* **dofi** (`string|null`)

    A link to the MP's latest declaration of financial interests.

* **email** (`string|null`)

    Official e-mail address.

* **gender** (`string`)

    See [`foaf:gender`](http://xmlns.com/foaf/spec/#term_gender).

* **identifiers** (`array [object]|null`)

    A mapping of issued identifiers.

    * **identifier** (`string|null`)

    * [required] **scheme** (`string`)

        One of:

        * http://www.wikidata.org/entity/

* **image** (`string|null`)

    A link to a preferred image of the MP.

* **images** (`array [string|null]|null`)

    All images of the MP available on Parliament.

* **links** (`array [object]|null`)

    A list of pertinent links, e.g. to the MP's page on Parliament.  Generally no more than five.  If linking to Wikipedia, link only to one language edition of it, preferably the English Wikipedia.

    * [required] **note** (`object`)

        * [required] **el** (`string`)

            A brief description in Greek.

        * [required] **en** (`string`)

            A brief description in English.

        * [required] **tr** (`string`)

            A brief description in Turkish.

    * [required] **url** (`string`)

        The link itself.

* [required] **name** (`object`)

    The MP's name.

    * [required] **el** (`string`)

        Their name in Greek, in the following order: last name, middle name, first name.

    * [required] **en** (`string`)

        Their name in English, ISO 843-transliterated, in the following order: last name, middle name, first name.

    * [required] **tr** (`string`)

        Their name in Turkish, in the following order: last name, middle name, first name.

* **other_names** (`array [object]|null`)

    Alternate names and spellings.

    * [required] **name** (`string`)

        The name itself.

    * [required] **note** (`string`)

        What sort of name is it?

* [required] **tenures** (`array [object]`)

    The MP's tenures in parliament.

    * [required] **electoral_district** (`object`)

        The district served.

        * [required] **el** (`string`)

            The name of the district in Greek.

        * [required] **en** (`string`)

            The name of the district in English, ISO 843-transliterated from Greek.

        * [required] **tr** (`string`)

            The name of the district in Turkish

    * [required] **end_date** (`string|null`)

        The end date, in ISO format (YYYY-MM-DD).  Leave blank if MP currently in office.

    * [required] **parliamentary_group_id** (`string|null`)

        The `id` of the parliament group the MP is affiliated to, if any; otherwise leave blank.

    * [required] **start_date** (`string`)

        The start date, in ISO format (YYYY-MM-DD).

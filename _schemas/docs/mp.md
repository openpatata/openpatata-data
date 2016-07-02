* [required] **_id** (`string`)

* [required] **_sources** (`array [string]`)

* [required] **birth_date** (`string|null`)

    Their date of birth in the ISO format.

* [required] **contact_details** (`array [object]`)

    The MP's contact details.  Their preferred email address should be duplicated here.

    * [required] **type** (`string`)

        The contact medium as per the [Popolo standard](http://www.popoloproject.com/specs/contact-detail.html).

    * [required] **value** (`string`)

        The corresponding value, e.g. a phone number or an email address.

* **dofi** (`string|null`)

    A link to the MP's latest declaration of financial interests.

* [required] **email** (`string|null`)

    Official e-mail address.

* [required] **gender** (`string|null`)

    See [`foaf:gender`](http://xmlns.com/foaf/spec/#term_gender).

* [required] **identifiers** (`array [object]`)

    A mapping of issued identifiers.

    * **identifier** (`string|null`)

    * [required] **scheme** (`string`)

        One of:

        * http://www.wikidata.org/entity/

* [required] **image** (`string|null`)

    A link to a preferred image of the MP.

* [required] **images** (`array [string|null]`)

    All images of the MP available on Parliament.

* [required] **links** (`array [object]`)

    A list of pertinent links, e.g. to the MP's page on Parliament.  Generally no more than five.

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

* [required] **other_names** (`array [object]`)

    Alternate names and spellings.

    * [required] **name** (`string`)

        The name itself.

    * [required] **note** (`string`)

        What sort of name is it?

* [required] **tenures** (`array [object]`)

    The MP's tenures in parliament.

    * [required] **electoral_district_id** (`string`)

        The district served.

    * **end_date** (`string|null`)

        The end date, in ISO format (YYYY-MM-DD).  Leave blank if MP currently in office.

    * [required] **parliamentary_period_id** (`string`)

        The parliamentary period number during their term of office.

    * [required] **party_id** (`string|null`)

        The `id` of the party the MP is affiliated to, if any; otherwise leave blank.

    * **start_date** (`string|null`)

        The start date, in ISO format (YYYY-MM-DD).

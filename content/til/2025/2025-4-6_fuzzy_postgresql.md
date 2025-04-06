+++
title = 'How to use Fuzzy String Matching with PostgreSQL'
date = 2025-04-06T11:42:16-05:00
draft = false
tags = ['Peter Gleeson','postgresql', 'fuzzy', 'string', 'pg_trgm', 'trigram', 'phonetic', 'fuzzystrmatch', 'soundex', 'string_to_array', 'metaphone', 'similarity', 'levenshtein']
summary = 'Good article from Peter.'
comments = true
+++

From https://www.freecodecamp.org/news/fuzzy-string-matching-with-postgresql/.

## Using Trigrams

```sql
CREATE EXTENSION pg_trgm;
```

Trigrams are formed by breaking a string into groups of three consecutive
letters.
For example, the string "hello" would be represented by the following set of
trigrams:

* "h", "he", "hel", "ell", "llo", "lo"

By comparing how similar the set of trigrams are between two strings, it is
possible to estimate how similar they are on a scale between 0 and 1.
This allows for fuzzy matching, by setting similarity threshold above which
strings are considered to match.

```sql
select *
  from artists
 where similarity(name, 'Claud Monay') > 0.4;
```

The default threshold is 0.3.
You can use the `%` operator in this case as shorthand for fuzzy matching names
against a potential match:

```sql
select *
  from artists
 where name % 'Andrey Deran';
```

Perhaps you only have an idea of one part of the name.
The `%` operator lets you compare against elements of an array, so you can
match against any part of the name.
The next query uses Postgres' `STRING_TO_ARRAY` function to split to split the
artists' full names into arrays of separate names.

```sql
select *
  from artists
 where 'Cadinsky' % ANY(STRING_TO_ARRAY(name, ' '));
```

## Phonetic Algorithms

Phonetic algorithms use sets of rules to represent a string using a short code.
The code contains the key information about how the string should sound if read
aloud.
By comparing these shortened codes, it is possible to fuzzy match strings which
are spelled differently but sound alike.

Postgres comes with an extension that lets you make use of some of these
algorithms.

```sql
CREATE EXTENSION fuzzstrmatch;
```

One example is an algorithm called Soundex which works by converting strings
into four letter codes which describe how they sound.
For example, the Soundex representations of 'flower' and 'flour' are both F460.

The query below finds the record which sounds like the name 'Damian Hurst':

```sql
select *
  from artists
 where nationality in ('American', 'British')
   and soundex(name) = soundex('Damian Hurst');
```

Another algorithm is called metaphone in that it converts strings into a code
representation using a set of rules.
The metaphone algorithm will return codes of different lengths (unlike Soundex,
which always returns four characters).
Tou can pass argument to the `METAPHONE` function indicating the maximum length
code you want it to return.

```sql
select artist_id
      ,name
      ,metaphone(name, 10)
 from artists
where nationality = 'American'
limit 5;
```

Because both metaphone and Soundex return strings as outputs you can use them
in other fuzzy string matching functions.
For example below finds the five closest matches for the name Si Tomlee.

```sql
  select *
    from artists
   where nationality = 'American'
order by similarity(
                     metaphone(name, 10)
                    ,metaphone('Si Tomlee', 10)
                   ) desc
   limit 5;
```

## Going the Distance

You can calculate the distance between strings using Levenshtein distance for
example.
If you have the words `bigger` and `better` is 3 because you can transform
`bigger` into `better` by substituting `igg` to `ett`.

```sql
  select *
        ,levenshtein(name, 'Freda Kallo')
    from artists
order by levenshtein(name, 'Freda Kallo') asc
   limit 5;
```

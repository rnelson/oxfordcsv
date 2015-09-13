# oxfordcsv

## About

Why use plain old CSV when you can use [Oxford CSV][tweet]?

## Usage

To use _oxfordcsv_, simple pipe CSV data into it: `oxfordcsv.py <infile.csv`

```
$ cat sample.csv
id,name,address,city,state
1,Alice,213 Elk St.,New York,NY
2,Bob,84924 1st Ave.,Boulder,CO
3,Cheryl,99376 Apple Pkwy. Apt. #1632,Los Angeles,CA
4,Dean,153 8th St. So.,Houston,TX
$ oxfordcsv.py < sample.csv > oxford.csv
$ cat oxford.csv
id,name,address,city,and state
1,Alice,213 Elk St.,New York,and NY
2,Bob,84924 1st Ave.,Boulder,and CO
3,Cheryl,99376 Apple Pkwy. Apt. #1632,Los Angeles,and CA
4,Dean,153 8th St. So.,Houston,and TX
$
```

For those of you who want stricter adherence to the rules of the English 
language, the `-E` argument will cause extra spaces to be added:

```
$ oxfordcsv.py -E < sample.csv
id, name, address, city, and state
1, Alice, 213 Elk St., New York, and NY
2, Bob, 84924 1st Ave., Boulder, and CO
3, Cheryl, 99376 Apple Pkwy. Apt. #1632, Los Angeles, and CA
4, Dean, 153 8th St. So., Houston, and TX
```

## License

[MIT](https://github.com/rnelson/oxfordcsv/blob/master/LICENSE)



[tweet]: https://twitter.com/zapjackson/status/530941076492648448

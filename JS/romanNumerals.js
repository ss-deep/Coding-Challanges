/* Write a function in romanNumerals.js that converts an integer (<= 1,000) to its Roman numeral equivalent.
For reference, these are the building blocks for how we encode numbers with Roman numerals:
Decimal Roman
1       I
5       V
10      X
50      L
100     C
500     D
1,000   M
For example:
toRoman(5) 'V'
toRoman(267) 'CCLXVII'
Important: You should convert to “old - school Roman numerals”, where subtraction isn’t used.
    So, for exmple, 4 is “IIII” and 9 is “VIIII”. You may be more used to a different style, where 
subtraction is used, as 4 would be “IV” and 9 would be “IX”. This is not what we want here(though 
    it’s a good, but much harder challenge).
For example:
toRoman(99) 'LXXXXVIIII' */

function toRoman(numToConvert) {
    let romanObjArr = [
        [1000, 'M'],
        [500, 'D'],
        [100,'C'],
        [50, 'L'],
        [10,'X'],
        [5,'V'],
        [1, 'I']
    ]
    let result=""
    for (let i = 0; i < romanObjArr.length; i++) {
        while (numToConvert >= romanObjArr[i][0]) {
            numToConvert -= romanObjArr[i][0]
            result+=romanObjArr[i][1]
        }
    }
    console.log(result);
}
toRoman(99);// 'LXXXXVIIII'
toRoman(5) //'V'
toRoman(267) //'CCLXVII'

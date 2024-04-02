/* Write a function that turns a string of 24-hour time into words.
You can trust that you’ll be given a valid string (it will always have a two-digit hour 00-23, 
and a two-digit minute 00-59). Hours 0-11 are am, and hours 12-23 are pm. Handle noon and midnight 
specially:
timeWord("00:00") // 'midnight'
timeWord("12:00") // 'noon'
timeWord("01:00") // "one o'clock am"
timeWord("06:01") // 'six oh one am'
timeWord("06:10") // 'six ten am'
timeWord("06:18") // 'six eighteen am'
timeWord("06:30") // 'six thirty am'
timeWord("10:34") // 'ten thirty four am'
Don’t forget to handle early morning properly:
timeWord("00:12") // 'twelve twelve am'
For times after noon, add ‘pm’:
timeWord("12:09") // 'twelve oh nine pm'
timeWord("23:23") // 'eleven twenty three pm'
 */

function timeWord(timeStr) {
    let ones = ["", 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
        'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    let tens = ['Twenty','Thirty','Forty','Fifty'];
    let minuts

    if (timeStr === "00:00")
        return "Midnight";
    if(timeStr === "12:00")
        return "Noon"
        
    let hh = +(timeStr.slice(0, 2))
    let mm = (timeStr.slice(3))

    //convert minuts
    if (+mm <= 9)
        (+mm === 0) ? minuts= `o'clock` : minuts= `oh ${ones[+mm]}`
    else 
        minuts= ((+mm>19) ? `${tens[mm[0]-2]} ${ones[mm[1]]}` : `${ones[+mm]}`) 
    
    // convert hours
    if (hh <= 11)
        return (hh === 0) ? `${ones[12]} ${minuts} am` : `${ones[hh]} ${minuts} am`
    else 
        return (hh === 12) ? `${ones[12]} ${minuts} pm` : `${ones[hh%12]} ${minuts} pm`
}

console.log(timeWord("00:00")) // 'midnight'
console.log(timeWord("12:00")) // 'noon'
console.log(timeWord("01:00")) // "one o'clock am"
console.log(timeWord("23:23"));  // 'eleven twenty three pm'
console.log(timeWord("06:01")) // 'six oh one am'
console.log(timeWord("06:10")) // 'six ten am'
console.log(timeWord("06:18")) // 'six eighteen am'
console.log(timeWord("06:30")) // 'six thirty am'
console.log(timeWord("10:34")) // 'ten thirty four am'
console.log(timeWord("00:12")) // 'twelve twelve am'
console.log(timeWord("12:09")) // 'twelve oh nine pm'
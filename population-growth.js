/* At the end of the first year there will be: 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
At the end of the 2nd year there will be: 1070 + 1070 * 0.02 + 50 => 1141 inhabitants
    (** number of inhabitants is an integer **) At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213
It will need 3 entire years.
 */

function nbYear(p0, percent, aug, surpass) {
    let year = 0
    
    while (p0<=surpass) {
        p0 = p0+(Math.floor( (p0 * (percent / 100)) + aug))
        year++
        
    }
    console.log(year);
}


nbYear(1500, 5, 100, 5000)//--> 15

nbYear(1500000, 2.5, 10000, 2000000) //--> 10

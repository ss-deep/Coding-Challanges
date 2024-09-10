/* Given a string, return true or false depending on whether that string has balanced parentheses.
For the purposes of this problem, you only need to worry about parentheses(and), not other
opening - and - closing marks, like curly brackets, square brackets, or angle brackets.
For example:
You may consider a string with no parentheses balanced:
>>> has_balanced_parens("Hey...there are no parens here!") // true
let sample1 = "This ( is unbalanced."
let sample2 = "(This (is (a) balanced) string.)"
let sample3 = "This is () also ) unbalanced."
let sample4 = "Balanced."
 */

function has_balanced_parens(str) {
    let counter = 0
    for (let i = 0; i < str.length; i++){
        if (str[i] === '(' && counter >= 0) {
            counter++
        } else if(str[i] === ')'){
            counter--;
        }
    }
    if (counter === 0) {
        return true
    } else {
        return false
    }
}

console.log(has_balanced_parens("()"));  // true
console.log(has_balanced_parens("(Oh (Noes!)")) // false
console.log(has_balanced_parens("((There's a bonus open paren here.)"));  // false
console.log(has_balanced_parens(")("));  // false
console.log(has_balanced_parens("("));  // false
console.log(has_balanced_parens("(This has (too many closes.) ) )"));  // false

//Prompt
let result = prompt ("Please Enter Your Name.\n");
console.log ("Hello", result);

let num = prompt("Enter any number!\n");
num = Number(num);
// num = num + 10;
console.log (num+1);
//If Statement
if (isNaN(num)) {
    num =10;
}
console.log(num);
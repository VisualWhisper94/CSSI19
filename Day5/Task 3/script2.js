//f(x) is a funtion that takes a single parameter 
//then multiply it by three and adds seven.
function g(x) {
    return 5 * x + 5;
}   
//Displays result of calling function f( )with the argument within.
console.log ("\n")
console.log (g(2))
console.log (g(7))
console.log (g(3))

function h(x) {
    return 5 * x ** 2 - 4 * x + 2;
}
console.log ("\n")
console.log (h(2))
console.log (h(7))
console.log (h(3))

function i(x,y) {
    return x ** 2 - y ** 2;
}
console.log ("\n")
console.log (i(2,3))
console.log (i(7,5))
console.log (i(3,9))

function k(r) {
    return 2* Math.PI * r;
}
console.log ("\n")
console.log (i(2,3))
console.log (i(7,5))
console.log (i(3,9))

function l(a,b,c){
    var d = b**2 - 4 * a * c;
    if (d >= 0) {
        var srd = Math.sqrt(d);
        return (-1 * b + srd)/(2 * a);
    }
    else {
        return NaN;
    }
} 
console.log ("\n")
console.log (i(1,4,4))
console.log (i(1,1,-1))
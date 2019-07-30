// mutl is an incoming parameter thats an ARRAY
//m is a parameter that is 
function Multiples(mult,m,n){
// For loop creates the variable i and sets it to 1
// It then compares it to the value of n which goes up 1 (++)
//Everytime it gets executed it goes to the next 
   for (let i = 1; i <= n; i++){
       mult.push(m * i);
   }
   return mult;
}
console.log (Multiples([],5,5))
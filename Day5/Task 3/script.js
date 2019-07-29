let mygrade = promt ("Enter a Grade!");
grade = Number(mygrade);
if (!isNaN(grade)) {
    if (grade >= 70){
    console.log ("You passed!");
    }
    else {
        console.log ("You failed!");
    }
}
else {
    console.log (mygrade, "This is not a grade/number");
}
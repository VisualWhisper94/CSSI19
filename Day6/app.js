const CountToN = (x) => {
    let absX = Math.abs(x);
    let index = 1;
    while (index <= absX){
        MediaQueryList.push(index)
        console.log (index);
        index = index+1; //you can also use index++; index +=1
    }
}
const GetNumber = () => 
{
    let num = Number(promt("Enter a Number"))
    while (!isNaN(num)) {
        return num;
        index++;
    }
    GetNumber()
}
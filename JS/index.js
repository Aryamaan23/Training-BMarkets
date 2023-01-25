/*
function checkAge(age)
{
    return age >18;
}
function myFunc()
{
    console.log(ages.find(checkAge));
}
const ages=[3,4,5,6,7,8,9]
myFunc()*/

//block scope
//function scope
//global scope

//Block scope
m=3;
n=2;
if(m>n)
{
    var p=4;//accessible
}

console.log(p);
if(m>n)
{
    let g=10;//not accessible
}
console.log(g);


//Function Scope
function f1(){let v1=9;}
function f2(){var v2=10;}
function f3(){const v3=11;}
console.log(v1,v2,v3); // not accessible as v1,v2,v3 have function based scope

//global scope
var v5=43;
let v6=5;
const v7=3;
function check()
{
    v5=66;
    v6=77;
}

console.log(v5,v6,v7);//accessible due to global scope
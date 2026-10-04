//1. Sum until zero
// let sum = 0;
// let input = Number(prompt("Enter the number: "));

// while (input != 0){
//   sum += input;
//   input = Number(prompt("Enter the number: "));

// }
// console.log(sum)

//2. Count digits
// let num = Number(prompt("Enter the digits: "))
// let count=0;

// while(num > 0){
//     let last = num % 10;
//     count++

//   num = (num - last)/10
// }
// console.log(count)


//3. Menu Program do...while
// let i;

// do{
//     console.log("1. Add");
//     console.log("2. Subtract");
//     console.log("3. Multiply");
//     console.log("4. Exit");

//     i = Number(prompt("Enter the value: "))

//     if(i === 1){
//         console.log("Selected add");
//     } else if (i === 2){
//         console.log("Selected Subtract");
//     } else if (i === 3){
//         console.log("Selected multiply")
//     } else {
//         console.log("exit");
//     }
// } while ( i != 4)


//4. Simple Calculator
// let i;

// do{
//     let a = Number(prompt("Enter the 1st number: "));
//     let operator = prompt("Enter the operator: ");
//     let b = Number(prompt("Enter the 2nd number:"));

//     if (operator === "+"){
//         console.log(a + b);
//     } else if (operator=== "-"){
//         console.log(a-b);
//     } else if (operator=== "*"){
//         console.log(a*b)
//     }else if (operator === "/"){
//         console.log(a/b)
//     }else{
//         console.log("Invalid Operatpr")
//     }

//     i = prompt("Do you want to continue? (y/n)")

// } while (i != "n" )


//5. Guessing name
// let secretNum = 7;
// let user;

// do{
//   user = Number(prompt("Enter the guessed number: "));
//   if(user > secretNum){
//     console.log("lower")
//   } else if (user < secretNum){
//     console.log("higher")
//   } else {
//     console.log("correct")
//   }
// }while(user != 7)


//6. print numbers
// let i=1;
// do{
//     console.log(i);
//     i++;
// } while (i <= 10)

//7. Multiplication Table
// let n=5;
// let i=1;
// let mul;

// do{
//     mul = n * i;
//     console.log(n,"*",i,"=",mul)
//     i++;
// } while(i <= 10)

//8. print numbers in reverse order
// let i=10;
// do{
//     console.log(i);
//     i--
// }while (i >= 1)


//9. print even numbers
// let i=1;
// do{
//     if(i % 2 ==0){
//         console.log(i)
//     } i++;
// } while(i <= 10)

//10. keep asking for a number until reaches 0
// let userInput

// do{
//   userInput = Number(prompt("Enter the Number: "));
  
// } while (userInput != 0);
// console.log("stopped")
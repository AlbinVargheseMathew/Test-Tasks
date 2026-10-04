//Pattern Based question
//1. square pattern

// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for (let j=1;j<=5;j++){
//         pattern += "*";
//     }
//     console.log(pattern);
// }


//2. Right angle triangle
// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         pattern += "*"
//     }
//     console.log(pattern)
// }


//3. Reverse right angle triangle
// for(let i=5;i>=1;i--){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         pattern += "*"
//     }
//     console.log(pattern)
// }


//4. Number triangle horizontal
// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         pattern += j
//     }
//     console.log(pattern)
// }


//5. repeated triable
// for(let i=1;i<=5;i++){
//     let pattern="";
//     for(let j=1;j<=i;j++){
//         pattern += i;
//     }
//     console.log(pattern)
// }


//6. Same number in every row;
// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=5;j++){
//         pattern += i;
//     }
//     console.log(pattern)
// }


//7. Continuous number
// let num=1;

// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         pattern += num + " ";
//         num++;
//     }
//     console.log(pattern)
// }


//8. Alphabet Triangle
// let letters = ["A", "B", "C", "D", "E"];

// for(let i=0;i<=4;i++){
//     let pattern = "";
//     for(let j=0;j<=i;j++){
//         pattern += letters[j];
//     }
//     console.log(pattern)
// }


//9. Repeated Alphabet
// let letters = ["A","B","C","D","E"]

// for(let i=0;i<=4;i++){
//     let pattern="";
//     for(let j=0; j<=i; j++){
//         pattern += letters[i]
//     }
//     console.log(pattern)
// }

//10. Zero one pattern
// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         if((i +j) % 2 == 0){
//             pattern += 1
//         } else {
//             pattern += 0;
//         }
//     }
//     console.log(pattern)
// }
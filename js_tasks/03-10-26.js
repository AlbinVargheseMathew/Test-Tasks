//1. Right-aligned triangle
// let n=5;

// for(i=1;i<=n;i++){
//     let pattern = "";
//     for(j=1;j<=n-i;j++){
//         pattern +=" ";
//     }
//     for(k=1;k<=i;k++){
//         pattern += "*"
//     }
//     console.log(pattern)
// }


//2. Reverse right aligned triangle
// let n=5;

// for(i=5;i>=1;i--){
//     let pattern = "";
//     for(j=1;j<=n-i;j++){
//         pattern += " "
//     }
//     for(k=1;k<=i;k++){
//         pattern += "*"
//     }
//     console.log(pattern)
// }


//3. pyramid
// let n=5;

// for(let i=1;i<=n;i++){
//     let pattern = "";
//     for(let j=1;j<=n-i;j++){
//         pattern += " ";
//     }
//     for(let k=1;k<=2*i-1;k++){
//         pattern += "*"
//     };
//     console.log(pattern)
// }


//4. Reverse Pyramid
// let n=5;

// for(let i=5;i>=1;i--){
//     let pattern = "";
//     for(let j=1;j<=n-i;j++){
//         pattern += " ";
//     }
//     for(let k=1;k<=2*i-1;k++){
//         pattern += "*"
//     }
//     console.log(pattern)
// }


// let n = 5;

// for(let i = 1; i <= n; i++){
//     let pattern = "";
//     for(let j = 1; j <= i; j++){
//         pattern += " ";
//     }
//     for(let k = 1; k <= 2*(n-i)+1; k++){
//         pattern += "*";
//     }
//     console.log(pattern);
// }


//5. Number pyramid
// let n=5;

// for(i=1;i<=5;i++){
//     let pattern = "";
//     for(j=1;j<=n-i;j++){
//         pattern += " ";
//     }
//     for(k=1;k<=2*i-1;k++){
//         pattern += k;
//     }
//     console.log(pattern)
// }


//6. Repeated NUmber pyramid
// let n=5;
// for(i=1;i<=n;i++){
//     let pattern = "";
//     for(j=1;j<=n-i;j++){
//         pattern += " ";
//     }
//     for(k=1;k<=2*i-1;k++){
//         pattern += i
//     }
//     console.log(pattern)
// }


//7. Hollow square
// let n=5;

// for(i=1;i<=5;i++){
//     let pattern = "";
//     for(j=1;j<=5;j++){
//         if(i === 1 || j === 1 || i === n || j ===n){
//             pattern += "*"
//         } else {
//             pattern += " "
//         }
//     }
//     console.log(pattern)
// }


//8. Hallow right triangle
// let n=5;
// for(let i=1;i<=n;i++){
//     let pattern = "";
//     for(let j=1;j<=i;j++){
//         if(i=== n || j === 1 || j === i){
//             pattern += "*"
//         }else{
//             pattern += " ";
//         }
//     }
//     console.log(pattern)
// }


//Diamond
// let n=5

//   for(let i=1;i <= n; i++){
//     let pattern = "";
//       for(let j=1; j<=n-i; j++){ //space
//           pattern += " ";
//       }
//         for(let k=1; k<=2*i-1;k++){
//                 pattern += "*";
//         }
//         console.log(pattern)
//         }

// for(let i=4;i>=0;i--){
// 	let pattern="";
// 		for(let j=1; j<=n-i;j++){
// 			pattern+=" ";
// 		}
// 		for(let k=1; k<=(2*i)-1;k++){
// 			pattern+="*";
// 		}
// 		console.log(pattern)
// }


//10. Alternating rows
// for(let i=1;i<=5;i++){
//     let pattern = "";
//     for(let j=1;j<=5;j++){
//         if(i % 2 == 1){
//             pattern += "*"
//         }else{
//             pattern += "-"
//         }
//     }
//     console.log(pattern)
// }
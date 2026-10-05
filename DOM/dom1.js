

//task1
const title = document.getElementById("title")
const studentName = document.getElementById("studentName")
const studentList = document.getElementById("studentList")

//task2
title.textContent ="Student List";

//task3
// const name = studentName.value
// console.log(name)

//task4
const student = document.createElement("p");
student.textContent="Anjali"
studentList.append(student)
console.log(student)

//task5
const secondstudent = document.createElement("p");
secondstudent.textContent="Vishnu"
studentList.appendChild(secondstudent)
console.log(secondstudent)

//task6
document.getElementById("2").remove()

//task7
const students = document.querySelectorAll("#studentList");
for (let student of students){
    console.log(student.textContent)
}

//task8
const heading = document.createElement("h2");
// heading.textContent = "Students"
heading.innerHTML = "Students"
studentList.append(heading)
console.log(heading)





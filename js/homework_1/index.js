const hiddenNumber = Math.floor(Math.random() * 1000);
console.log(`Загаданное число: ${hiddenNumber}`);

const welcomeText = `Здравствуйте!
Это игра: "Угадай число"
У вас есть 4 попытки

Введите число:`

let enteredNumber = prompt(welcomeText);
let i = 3;

while (i) {
if (hiddenNumber === +enteredNumber) {
    alert('Вы угадали!')
    break;
} else if (enteredNumber === 'q') {
    break;
} else if (isNaN(+enteredNumber) || 0 >= +enteredNumber >= 1000) {
    alert(`Вы ввели некоректные данные`);
    enteredNumber = prompt(`Введите число: `);
} else if (hiddenNumber > enteredNumber) {
    console.log(`Осталось попыток: ${i}`);
    alert("Больше");
    enteredNumber = prompt(`Введите число: `);
    i--;
} else if (hiddenNumber < enteredNumber) {
    console.log(`Осталось попыток: ${i}`);
    alert("Меньше");
    enteredNumber = prompt(`Введите число: `);
    i--;
}  
};

if (i === 0) {
    alert('Вы не угадали, попробуйте в следующий раз.');
}
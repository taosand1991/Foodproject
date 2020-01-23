
let num1 = document.getElementById('num1');
let num2 = document.getElementById('num2');
let final1 = num1.innerHTML = Math.floor(Math.random(1)* 11 + 1);
let final2 = num2.innerHTML = Math.floor(Math.random(1)* 11 + 1);

let guess = document.getElementById('check')
let check3 = document.querySelector('#dont')
let result = document.getElementById('answer')
check1 = final1 * final2;
console.log(check1)
let h1 = document.createElement('p')
buton = document.getElementById('mino').disabled = true


function handleSubmit() {
    if(parseInt(guess.value)  ===parseInt(check1)) {
        result.innerHTML = 'Correct'
        result.style.color = 'green'
        buton = document.getElementById('mino').disabled = false
    }else{
        result.innerHTML = 'Incorrect!!!'
        result.style.color = 'red'
    }

}

check3.addEventListener('click', handleSubmit)


let redirect = document.getElementById('mine')


let dooP = document.getElementsByClassName('jumbotron')

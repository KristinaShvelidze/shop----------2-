let cookies = document.cookie.split(' ')
console.log(cookies.length)

document.querySelector('.final-count-num').textContent = cookies.length

let count = document.querySelector('.count')
let price = document.querySelectorAll('.price')

// let num = 10;
if (cookies.length > 1 && cookies.length < 5) {
    document.querySelector('.total-count').textContent = '-товари на суму'
    // console.log(999999999)
}

if (cookies.length == 1 ) {
    document.querySelector('.total-count').textContent = '-товар на суму'
}

let finalCount = document.querySelector(".final-count")
finalCount.textContent = cookies.length * Number(price)

document.querySelector('.processing').addEventListener(
    'click', (event) => {
        document.querySelector('.popup-processing').style.display = "flex"


    }
)


window.onscroll = function(){toFixHeader()}

var header = document.getElementById('header')
var headerOffsetHeight = header.offsetHeight

function toFixHeader(){
	if (window.pageYOffset >= headerOffsetHeight){
		header.classList.add('fixed')
	}else{header.classList.remove('fixed')}
}

//Cart//
class Cart{
	constructor(requestURL){
		this.requestURL = requestURL
	}
	cartRender(){
		let html__basket_counters = document.querySelectorAll('.basket__counter')
		for (let counter of html__basket_counters){
			var cart_amount = Number(counter.innerHTML)
			cart_amount += 1
			counter.innerHTML = cart_amount
		}
	}
	cartAdd(id){
		const xhr = new XMLHttpRequest()
		
		xhr.open('GET', this.requestURL + id)
		xhr.onload = () =>{
			if (xhr.status >= 400){
				alert("Oops!")
			}else{
				this.cartRender()
			}
		}
		xhr.send()
	}
}

//Smooth scroll//
let nav__links = document.querySelectorAll('.nav__link')

for (let link of nav__links){	
	link.addEventListener('click', function(elem){
		elem.preventDefault()
		var itemID = link.getAttribute('href').substring(1)
		document.getElementById(itemID).scrollIntoView({
			behavior: 'smooth',
			block: 'start'
		})
	})
}

//Slider//
const slides = document.querySelectorAll('.slide'),
	  arrow_prev = document.querySelector('.arrow-prev'),
	  arrow_next = document.querySelector('.arrow-next');

let position = 0 
function activateSlide(n){
	for (let slide of slides){
		slide.classList.remove('active')
	}
	slides[n].classList.add('active')
}

function prevSlide(){
	if(position == 0){
		position = slides.length-1
		activateSlide(position)
	}else{
		position--
		activateSlide(position)
	}
}
function nextSlide(){
	if(position == slides.length-1){
		position = 0
		activateSlide(position)
	}else{
		position++
		activateSlide(position)
	}
}

let interval = setInterval(nextSlide, 2500)

arrow_prev.addEventListener('click', function(elem){
	prevSlide()
	clearInterval(interval)
	interval = setInterval(nextSlide, 2500)
})
arrow_next.addEventListener('click', function(elem){
	nextSlide()
	clearInterval(interval)
	interval = setInterval(nextSlide, 2500)
})

//Init//
function cartBtnsInit(cart){
	let btns_buy = document.querySelectorAll('.btn-buy')
	for (let btn_buy of btns_buy){
		btn_buy.addEventListener('click', function(elem){
			elem.preventDefault()
			cart.cartAdd(btn_buy.dataset.id, requestURL)
		})
	}
}

const cart = new Cart(requestURL = '/cart/add/')
cartBtnsInit(cart)


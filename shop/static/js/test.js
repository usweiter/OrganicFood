window.onscroll = function(){toFixHeader()}

var header = document.getElementById('header')
var headerOffsetHeight = header.offsetHeight

function toFixHeader(){
	if (window.pageYOffset >= headerOffsetHeight){
		header.classList.add('fixed')
	}else{header.classList.remove('fixed')}
}

const requestURL = '/cart/add/'

function cartAdd(id){
	
	const xhr = new XMLHttpRequest()
	
	xhr.open('GET', requestURL + id)
	xhr.onload = () =>{
		if (xhr.status >= 400){
			alert("Oops!")
		}else{
			cart_render()
		}
	}
	xhr.send()	
}

let cart = {}
let html__basket_count = document.querySelector('.basket__counter')
let btns_buy = document.querySelectorAll('.btn-buy')

function cart_render(){
	var cart_amount = Number(html__basket_count.innerHTML)
	cart_amount += 1
	html__basket_count.innerHTML = cart_amount
}

for (let btn_buy of btns_buy){
	btn_buy.addEventListener('click', function(elem){
		elem.preventDefault()
		cartAdd(btn_buy.dataset.id)
	})
}

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
const slides = document.querySelectorAll('slide'),
	  arrow_prev = document.querySelector('arrow-prev'),
	  arrow_next = document.querySelector('arrow-next');

let position = 0 
function activateSlide(n){
	for (slide of slides){
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


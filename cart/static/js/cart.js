let xhr = new XMLHttpRequest()
let forms = document.forms
let cart_removes = document.querySelectorAll('.cart-remove')

for (let cart_remove of cart_removes){
	cart_remove.addEventListener('click', function(elem){
		let dataset_id = cart_remove.dataset.id
		elem.preventDefault()
		cartRemove(dataset_id)
	})
}

for (let form of forms ){
	form.submit_button.addEventListener('click', function(){
		cartAdd(xhr, form.dataset.id)
	})
}

function cartItemRender(item){

}

function getFormBydataset_id(forms, dataset_id){
    for(let form of forms){
        if(form.dataset.id == dataset_id){
            return form
        }
    }
}

function cartAdd(xhr, dataset_id){
	let form = new FormData(getFormBydataset_id(forms, dataset_id))
	let add_url = '/cart/add/' + dataset_id

	xhr.open('POST', add_url)
	xhr.onload = ()=>{
		if (xhr.status >= 400){
			alert('Oops!')
		}
	}
	xhr.send(form)
}

function cartRemove(dataset_id){
	let xhr = new XMLHttpRequest()
	let remove_url = '/cart/remove/' + dataset_id

	xhr.open('GET', remove_url)
	xhr.onload = ()=>{
		if (xhr.status >= 400){
			alert('Oops!')
		}else{
			let id = dataset_id
			let tabel_row = document.getElementById(id)
			tabel_row.remove()
		}
	}
	xhr.send()
}
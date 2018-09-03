//Cria um vetor com apenas os logins


//~ console.log(valuesBCC);


//Escolhe o objeto html que sera a barra de busca
var input = document.getElementById("search_input");
var awesomplete = new Awesomplete(input);


//Cria o evento que sera acionado ao selecionar um dos valores propostos
awesomplete.replace = function(text){
	id=names.names.indexOf(text.label);
	$("#display").attr("src","img/"+id+".png");

};

//Seta a lista de valores para o autocomplete
awesomplete.list = names.names;







function verifyPokemon() {
    var pokemon_provided = document.getElementById("pokemon").value;
    if (!pokemon_provided) {
        document.getElementById("userPrompt").textContent = "Please enter a Pokemon!";
    }
}

function getPokemon() {
    var pokemon = document.getElementById("pokemon").value;
        return pokemon;
    }
getPokemon();

function getGeneration() {
     // assume that generation will be a string for uniformity
     var generation = document.getElementById("generation").value;
     return generation
    }
getGeneration();

// create a function to get the preferred pokedex type

function getDexType() {
       // get either national or galar dex
       var nationalDexChosen = document.getElementById("national").checked;
       var galarDexChosen = document.getElementById("galar").checked;

       if (nationalDexChosen) {
            return "national"
       }
       else if (galarDexChosen) {
            return "galar"
       }
}

// if Enter is pressed in the text box, obtain the output value
// https://www.w3schools.com/howto/howto_js_trigger_button_enter.asp

// Get the input field
var input = document.getElementById("pokemon");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {

// Number 13 is the "Enter" key on the keyboard
if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("button_pokemon").click();
    }
});

// same thing for generations

// Get the input field
var input = document.getElementById("generation");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {

// Number 13 is the "Enter" key on the keyboard
if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("button_generation").click();
    }
});

function convertRomanNumeral(x) {
    if (x == 'i') {
        return 1;
    }
    else if (x == 'ii') {
        return 2;
    }
    else if (x == 'iii') {
        return 3;
    }
    else if (x == 'iv') {
        return 4;
    }
    else if (x == 'v') {
        return 5;
    }
    else if (x == 'vi') {
        return 6;
    }
    else if (x == 'vii') {
        return 7;
    }
    else if (x == 'viii') {
        return 8;
    }
}

// <!-- take the base pokemondb link and concat a new url depending on given pokemon and generation -->

function redirectPage() {
    // if getPokemon() will be false if string is empty and true if string is not empty
    // similarly, if getGeneration() will be false if no integer is provided (or 0)

    pokemon = getPokemon()
    generation = String(getGeneration())

    // if pokemon and generation are provided, then link to pokemondb
    // if pokemon and pokedex entry are provided, then link to veekun

    var pokedexEntryBool = document.getElementById("pokedex").checked;
    var learnsetBool = document.getElementById("learnset").checked;

    // error checking - make sure that pokemon input is a string and generation is integer or roman numeral

    var pokemonIsString;
    var generationIsStringNumber;

    // pokemon input
    if (isNaN(parseInt(pokemon))) {
        pokemonIsString = true; // strings that can't be parsed to ints are actual strings - 'two', not '2'
    }
    else {
        pokemonIsString = false; // if the string can be parsed, we don't want that output
    }

    // generation input
    var generationNums = ['1', '2', '3', '4', '5', '6', '7', '8'] // assume string, makes url concat easier
    var romanNums = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii']

    if (generationNums.includes(generation)) { // is the provided string generation in string number form?
        generationIsStringNumber = true;
    }
    // pythonic "in" only works for ints, not for strings
    // https://www.w3schools.com/jsref/jsref_includes_array.asp - for strings
    else if (romanNums.includes(generation.toLowerCase())) {
        generationIsStringNumber = true;
    }
    else {
        generationIsStringNumber = false;
    }

    // for all branches, pokemon needs to be a string and generation needs to be a number (e.g. '1' or 'I')

    // if the pokemon is an appropriate string, the generation can be converted to a valid string, and the learnset is marked
    if (pokemonIsString && generationIsStringNumber && learnsetBool) { // pokemondb

        var base_url = "https://pokemondb.net/pokedex/";

        pokemon = getPokemon().toLowerCase();
        generation = getGeneration(); // automatically string dtype

        // generation can be an integer (e.g. 4) or a string (e.g. IV) and we need a consistent output
        if (romanNums.includes(generation.toLowerCase())) { // roman numeral
            generation = String(convertRomanNumeral(generation.toLowerCase())); // numeral conversion is int - needs further String conversion
        }

        pokemon_url = base_url.concat(pokemon);
        pokemon_url = pokemon_url.concat("/moves/")

        whole_url = pokemon_url.concat(generation);

        window.open(whole_url, '_blank');
    }
    // if pokemon is the appropriate string and the pokedex is marked
    // whether generation is provided or not is irrelevant
    else if (pokemonIsString && pokedexEntryBool) { // veekun or marriland, depending on national or galar

        if (getDexType() == "national") {
            var base_url = "https://veekun.com/dex/pokemon/"
        }
        else if (getDexType() == "galar") {
            var base_url = "https://marriland.com/pokedex/"
        }

        pokemon = getPokemon().toLowerCase();

        whole_url = base_url.concat(pokemon);
        // change from window.location.href = whole_url; to window.open() - opens up a new tab
        window.open(whole_url, '_blank');
    }
    // pokemon is not a string or generation is not a number or both - wait for proper input
    else {
        document.getElementById("reminder").textContent = "Please enter either a Pokémon or generation as a number or Roman numeral!";
    }
}
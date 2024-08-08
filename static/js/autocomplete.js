console.log("WHATTTTTTT")

function findExpansions(game, input) {
    const expansions = {
        'Dominion': ['Dominion', 'Seaside', 'Intrigue', 'Prosperity', 'Promo'],
        'Moonrakers': ['Binding Ties', 'Nomad', 'Overload', 'The Shard', 'The Endless', 'Dark Matter', 'Starfall'],
        'Lords of Waterdeep': ['Scoundrels of Skullport'],
        'Clank!': ['Sunken Treasure', "The Mummy's Curse", 'Adventuring Party', 'Expeditions: Gold and Silk', 'Expeditions: Temple of the Ape Lords'],
        'Catan': ['Cities & Knights', 'Seafarers']
    };
    let gameExpansions = expansions[game];
    if (input == '') {
        return [];
    }
    var reg = new RegExp(input,'i')
    return gameExpansions.filter(function(term) {
        if (term.match(reg)) {
        return term;
        }
    });
}

function showExpansions(val, game) {
    let res = document.querySelector('.expansionResults');
    res.innerHTML = '';
    let list = '';
    if (val === '') {
        res.classList.add("Hide");
        return;
    } else {
        if(res.classList.contains('Hide')){
            res.classList.remove("Hide");
        }
    }
    let terms = findExpansions(game, val);
    let selectedExpansions = document.querySelectorAll('.selectedExpansion');

    let selectedExpansionsArray = Array.from(selectedExpansions).map(el => el.textContent.trim());
    let filteredTerms = terms.filter(term => !selectedExpansionsArray.includes(term));
    for (i = 0; i < filteredTerms.length; i++) {
        let resultItem = document.createElement('div');
        resultItem.textContent = filteredTerms[i];
        resultItem.classList.add('result-item')
        //list += '<li>' + terms[i] + '</li>';
        res.appendChild(resultItem);
    }

    // Add event listener to each li element
    let liElements = document.querySelectorAll(`.result-item`);
    liElements.forEach(function(li) {
        li.addEventListener('click', function() {
            createExpansion(li);
            res.innerHTML = '';
            res.classList.add("Hide");
            let expansions = document.querySelector('#expansions');
            expansions.value = '';
            
            let expansionnames = document.querySelector("#expansionnames");
            expansionnames.value = '';
            let usedExpansions = document.querySelectorAll('.selectedExpansion')
            for (let i = 0; i < usedExpansions.length; i++) {
                expansionnames.value += `${usedExpansions[i].innerHTML}`;
                if (i < usedExpansions.length - 1) {
                    expansionnames.value += ', ';
                }
            }
        });
    });

    document.addEventListener('click', function(event) {
        if (!event.target.closest('#expansions') && !event.target.closest('.expansionResults')) {
            res.classList.add("Hide");
        }
    });
}

function createExpansion(expansionName){
    let taggedExpansions = document.querySelector("#taggedExpansions");
    let tagContainer = document.createElement('div');
    let name = document.createElement('Span');
    let close = document.createElement('Span');
    name.innerHTML = `${expansionName.innerText}`;
    name.classList.add("selectedExpansion");
    close.innerHTML = ' X';
    close.classList.add('removeExpansion');

    close.addEventListener('click', () => {
        close.parentNode.remove();
    })

    tagContainer.appendChild(name);
    tagContainer.appendChild(close);
    taggedExpansions.appendChild(tagContainer);
}

function addExpansion(){
    console.log("adding expansion")
    let gameid = 59;
    let strings = 'Seaside, Intrigue';
    fetch(`/addExpansion?gameid=${gameid}&expansionsString=${strings}`)
    .then(response => response.json())
    .then(data => {
        search_terms = data;
        console.log(search_terms);
    })
    .catch(error => console.error(error));

}

function showExpansion(){
    let gameid = 59;
    fetch(`/retrieveExpansion?gameid=${gameid}`)
    .then(response => response.json())
    .then(data => {
        if (data.expansions) {
            console.log("Expansions:", data.expansions);
            // Handle the expansions data here
        } else {
            console.log("No expansions found for this game");
        }
    })
    .catch(error => console.error(error));

}

function autocompleteMatch(input) {
    if (input == '') {
        return [];
    }
    var reg = new RegExp(input,'i')
    return search_terms.filter(function(term) {
        if (term.match(reg)) {
        return term;
        }
    });
}

function showResults(val, id) {
    console.log("SHOW reSULTS")
    console.log("SHOW reSTS")

    let parts = id.split(/(\d+)/);
    let part = parts[0];
    let gameName = part.slice(0, -6);
    let index = id.search(/\d/);
    let num = id.substring(index);
    
    results = document.querySelector(`#${id}Results`);
    results.classList.remove("Hide");
    let res = results;
    res.innerHTML = '';
    let list = '';
    if (val === '') {
        res.classList.add("Hide");
        return;
    }
    let terms = autocompleteMatch(val);
    for (i=0; i<terms.length; i++) {
        list += '<li>' + terms[i] + '</li>';
    }
    res.innerHTML = '<ul>' + list + '</ul>';

    // Add event listener to each li element
    let liElements = document.querySelectorAll(`.res li`);
    liElements.forEach(function(li) {
        li.addEventListener('click', function() {
            console.log('hellooooo world')
            document.querySelector(`#${gameName}Player${num}`).value = li.innerText;
            res.innerHTML = '';
            res.classList.add("Hide");
        });
    });

    document.addEventListener('click', function(event) {
        if (!event.target.closest(`#${gameName}Player${num}`) && !event.target.closest(`.${gameName}results`)) {
            res.classList.add("Hide");
        }
    });

}

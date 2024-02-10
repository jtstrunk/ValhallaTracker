/* 
    Functionality for form 1 -- setting player number
*/

let submitBtn = document.querySelector("#formOneSubmit");
let firstForm = document.querySelector("#formy");
let secondForm = document.querySelector("#formt");

submitBtn.addEventListener('click', function submitForm1() {
    
    firstForm.classList.remove("Hide");
    secondForm.classList.add("Hide");

    let Players = document.querySelector("#playerCount").value;
    let numPlayers = parseInt(Players);

    let nameOne = document.querySelector("#playerOne");
    let nameTwo = document.querySelector("#playerTwo");
    let nameThree = document.querySelector("#playerThree");
    let nameFour = document.querySelector("#playerFour");
    let nameFive = document.querySelector("#playerFive");
    let nameSix = document.querySelector("#playerSix");


    if(numPlayers === 2) {
        nameOne.classList.remove("Hide");
        nameTwo.classList.remove("Hide");
    } 
    if(numPlayers === 3) {
        nameOne.classList.remove("Hide");
        nameTwo.classList.remove("Hide");
        nameThree.classList.remove("Hide");
    }
    if(numPlayers === 4) {
        nameOne.classList.remove("Hide");
        nameTwo.classList.remove("Hide");
        nameThree.classList.remove("Hide");
        nameFour.classList.remove("Hide");
    } 
    if(numPlayers === 5) {
        nameOne.classList.remove("Hide");
        nameTwo.classList.remove("Hide");
        nameThree.classList.remove("Hide");
        nameFour.classList.remove("Hide");
        nameFive.classList.remove("Hide");
    } 
    if(numPlayers === 6) {
        nameOne.classList.remove("Hide");
        nameTwo.classList.remove("Hide");
        nameThree.classList.remove("Hide");
        nameFour.classList.remove("Hide");
        nameFive.classList.remove("Hide");
        nameSix.classList.remove("Hide");
    }
    
})


let gardensBTN = document.querySelector("#gardens");
let islandBTN = document.querySelector("#island");
let Gchecker = false;
let Ichecker = false;
const stats = document.querySelectorAll('.stats');
const total = document.querySelectorAll('.total');
const gard = document.querySelectorAll('.gardens');
const card = document.querySelectorAll('.cards');
const isla = document.querySelectorAll('.island');

gardensBTN.addEventListener('click', function(){
    if (Gchecker === false) {
        gardensBTN.classList.add("selected");
        gardensBTN.classList.remove("deselected");
        gard.forEach(gardens => {
            gardens.classList.remove("Hide");
        })
        card.forEach(cards => {
            cards.classList.remove("Hide");
        })
        Gchecker = true;
    }
    else {
        gardensBTN.classList.remove("selected");
        gardensBTN.classList.add("deselected");
        gard.forEach(gardens => {
            gardens.classList.add("Hide");
        })
        card.forEach(cards => {
            cards.classList.add("Hide");
        })
        Gchecker = false;
    }
    stats.forEach(stats => {
        stats.style.width = '350px';
        stats.style.marginTop = '0px';
        stats.style.marginLeft = '15px';

    });
    total.forEach(total => {
        total.style.width = '4em';
    })
    

})

islandBTN.addEventListener('click', function(){
    if (Ichecker === false) {
        islandBTN.classList.add("selected");
        islandBTN.classList.remove("deselected");
        isla.forEach(island => {
            island.classList.remove("Hide");
        })
        Ichecker = true;
    }
    else {
        islandBTN.classList.remove("selected");
        islandBTN.classList.add("deselected");
        isla.forEach(island => {
            island.classList.add("Hide");
        })
        Ichecker = false;
    }
    stats.forEach(stats => {
        stats.style.width = '350px';
        stats.style.marginTop = '0px';
        stats.style.marginLeft = '15px';
    });
    total.forEach(total => {
        total.style.width = '5em'; 
    })
      

})

let scoreBoardsBTN = document.querySelector("#scoreboards");
let count = document.querySelector("#Counters");

let player1 = document.querySelector("#Player1");
let player2 = document.querySelector("#Player2");
let player3 = document.querySelector("#Player3");
let player4 = document.querySelector("#Player4");
let player5 = document.querySelector("#Player5");
let player6 = document.querySelector("#Player6");


player1Name = document.querySelector("#player1Name");
player2Name = document.querySelector("#player2Name");
player3Name = document.querySelector("#player3Name");
player4Name = document.querySelector("#player4Name");
player5Name = document.querySelector("#player5Name");
player6Name = document.querySelector("#player6Name");


scoreBoardsBTN.addEventListener('click', function(){
    firstForm.classList.add("Hide");
    count.classList.remove("Hide");
    let Players = document.querySelector("#playerCount").value
    let numPlayers = parseInt(Players);
    if(Ichecker === true && Gchecker === false) {
        stats.forEach(stats => {
        stats.style.width = '300px';
        });
    }


    if(numPlayers === 2) {
        player1Name.textContent = document.querySelector("#playerOne").value;
        player2Name.textContent = document.querySelector("#playerTwo").value;
        player1.classList.remove("Hide");
        player2.classList.remove("Hide");

        
    } 
    if(numPlayers === 3) {
        player1Name.textContent = document.querySelector("#playerOne").value;
        player2Name.textContent = document.querySelector("#playerTwo").value;
        player3Name.textContent = document.querySelector("#playerThree").value;
        player1.classList.remove("Hide");
        player2.classList.remove("Hide");
        player3.classList.remove("Hide");
    }
    if(numPlayers === 4) {
        player1Name.textContent = document.querySelector("#playerOne").value;
        player2Name.textContent = document.querySelector("#playerTwo").value;
        player3Name.textContent = document.querySelector("#playerThree").value;
        player4Name.textContent = document.querySelector("#playerFour").value;
        player1.classList.remove("Hide");
        player2.classList.remove("Hide");
        player3.classList.remove("Hide");
        player4.classList.remove("Hide"); 
    }
    if(numPlayers === 5) {
        player1Name.textContent = document.querySelector("#playerOne").value;
        player2Name.textContent = document.querySelector("#playerTwo").value;
        player3Name.textContent = document.querySelector("#playerThree").value;
        player4Name.textContent = document.querySelector("#playerFour").value;
        player5Name.textContent = document.querySelector("#playerFive").value;
        player1.classList.remove("Hide");
        player2.classList.remove("Hide");
        player3.classList.remove("Hide"); 
        player4.classList.remove("Hide");
        player5.classList.remove("Hide"); 
    }
    if(numPlayers === 6) {
        player1Name.textContent = document.querySelector("#playerOne").value;
        player2Name.textContent = document.querySelector("#playerTwo").value;
        player3Name.textContent = document.querySelector("#playerThree").value;
        player4Name.textContent = document.querySelector("#playerFour").value;
        player5Name.textContent = document.querySelector("#playerFive").value;
        player6Name.textContent = document.querySelector("#playerSix").value;
        player1.classList.remove("Hide");
        player2.classList.remove("Hide");
        player3.classList.remove("Hide");
        player4.classList.remove("Hide");
        player5.classList.remove("Hide");
        player6.classList.remove("Hide");  
    }

    if(Ichecker === true) {

    }


})
/*
    The break to functions
*/
function minusNum(vari, changing) {
    vari = vari - 1;
    changing.textContent = vari;
    return vari;
}

function plusNum(vari, changing) {
    vari = vari + 1
    changing.textContent = vari;
    return vari;
}

function calcScore(score, estate, duchy, province, gardens, cards, island, fscore) {
    score = (estate * 1) + (duchy * 3) + (province * 6) + (gardens * Math.floor(cards / 10)) + (island * 2);
    fscore.textContent = score;
}

let cards = 10, score = 0, estate = 3, duchy = 0, province = 0, island = 0, gardens = 0;
let p1Score = document.querySelector("#p1Score");

let eMinus = document.querySelector("#eMinus");
let ePlus = document.querySelector("#ePlus");
let startEstatesAmount = document.querySelector("#estateAmount");

eMinus.addEventListener('click', function(){
    estate = minusNum(estate, startEstatesAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

ePlus.addEventListener('click', function(){
    estate = plusNum(estate, startEstatesAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

let dMinus = document.querySelector("#dMinus");
let dPlus = document.querySelector("#dPlus");
let startDuchyAmount = document.querySelector("#duchyAmount");

dMinus.addEventListener('click', function(){
    duchy = minusNum(duchy, startDuchyAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

dPlus.addEventListener('click', function(){
    duchy = plusNum(duchy, startDuchyAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

let pMinus = document.querySelector("#pMinus");
let pPlus = document.querySelector("#pPlus");
let startProvinceAmount = document.querySelector("#provinceAmount");

pMinus.addEventListener('click', function(){
    province = minusNum(province, startProvinceAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

pPlus.addEventListener('click', function(){
    province = plusNum(province, startProvinceAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

let gMinus = document.querySelector("#gMinus");
let gPlus = document.querySelector("#gPlus");
let startGardensAmount = document.querySelector("#gardensAmount");

gMinus.addEventListener('click', function(){
    gardens = minusNum(gardens, startGardensAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

gPlus.addEventListener('click', function(){
    gardens = plusNum(gardens, startGardensAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

let cMinus = document.querySelector("#cMinus");
let cPlus = document.querySelector("#cPlus");
let startcardsAmount = document.querySelector("#cardAmount");

cMinus.addEventListener('click', function(){
    cards = minusNum(cards, startcardsAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

cPlus.addEventListener('click', function(){
    cards = plusNum(cards, startcardsAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

let iMinus = document.querySelector("#iMinus");
let iPlus = document.querySelector("#iPlus");
let startIslandAmount = document.querySelector("#islandAmount");

iMinus.addEventListener('click', function(){
    island = minusNum(island, startIslandAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})

iPlus.addEventListener('click', function(){
    island = plusNum(island, startIslandAmount);
    calcScore(score, estate, duchy, province, gardens, cards, island, p1Score);
})


/* 
    The break to player two functionality
*/

let cardsP2 = 10, scoreP2 = 0, estateP2 = 3, duchyP2 = 0, provinceP2 = 0, gardensP2 = 0, islandP2 = 0;
let p2Score = document.querySelector("#p2Score");

let estaMinusP2 = document.querySelector("#estaMinusP2");
let estaPlusP2 = document.querySelector("#estaPlusP2");
let startEstatesAmountP2 = document.querySelector("#estateAmountP2");

estaMinusP2.addEventListener('click', function(){
    estateP2 = minusNum(estateP2, startEstatesAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

estaPlusP2.addEventListener('click', function(){
    estateP2 = plusNum(estateP2, startEstatesAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

let duchMinusP2 = document.querySelector("#duchMinusP2");
let duchPlusP2 = document.querySelector("#duchPlusP2");
let startDuchyAmountP2 = document.querySelector("#duchyAmountP2");

duchMinusP2.addEventListener('click', function(){
    duchyP2 = minusNum(duchyP2, startDuchyAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

duchPlusP2.addEventListener('click', function(){
    duchyP2 = plusNum(duchyP2, startDuchyAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

let provMinusP2 = document.querySelector("#provMinusP2");
let provPlusP2 = document.querySelector("#provPlusP2");
let startProvinceAmountP2 = document.querySelector("#provinceAmountP2");

provMinusP2.addEventListener('click', function(){
    provinceP2 = minusNum(provinceP2, startProvinceAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

provPlusP2.addEventListener('click', function(){
    provinceP2 = plusNum(provinceP2, startProvinceAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

let gardMinusP2 = document.querySelector("#gardMinusP2");
let gardPlusP2 = document.querySelector("#gardPlusP2");
let startGardensAmountP2 = document.querySelector("#gardensAmountP2");

gardMinusP2.addEventListener('click', function(){
    gardensP2 = minusNum(gardensP2, startGardensAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

gardPlusP2.addEventListener('click', function(){
    gardensP2 = plusNum(gardensP2, startGardensAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

let islaMinusP2 = document.querySelector("#islaMinusP2");
let islaPlusP2 = document.querySelector("#islaPlusP2");
let startIslandAmountP2 = document.querySelector("#islandAmountP2");

islaMinusP2.addEventListener('click', function(){
    islandP2 = minusNum(islandP2, startIslandAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

islaPlusP2.addEventListener('click', function(){
    islandP2 = plusNum(islandP2, startIslandAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

let cardMinusP2 = document.querySelector("#cardMinusP2");
let cardPlusP2 = document.querySelector("#cardPlusP2");
let startcardsAmountP2 = document.querySelector("#cardAmountP2");

cardMinusP2.addEventListener('click', function(){
    cardsP2 = minusNum(cardsP2, startcardsAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

cardPlusP2.addEventListener('click', function(){
    cardsP2 = plusNum(cardsP2, startcardsAmountP2);
    calcScore(scoreP2, estateP2, duchyP2, provinceP2, gardensP2, cardsP2, islandP2, p2Score);
})

/* 
    The break to player three functionality
*/

let cardsP3 = 10, scoreP3 = 0, estateP3 = 3, duchyP3 = 0, provinceP3 = 0, gardensP3 = 0, islandP3 = 0;
let p3Score = document.querySelector("#p3Score");

let estaMinusP3 = document.querySelector("#estaMinusP3");
let estaPlusP3 = document.querySelector("#estaPlusP3");
let startEstatesAmountP3 = document.querySelector("#estateAmountP3");

estaMinusP3.addEventListener('click', function(){
    estateP3 = minusNum(estateP3, startEstatesAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

estaPlusP3.addEventListener('click', function(){
    estateP3 = plusNum(estateP3, startEstatesAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

let duchMinusP3 = document.querySelector("#duchMinusP3");
let duchPlusP3 = document.querySelector("#duchPlusP3");
let startDuchyAmountP3 = document.querySelector("#duchyAmountP3");

duchMinusP3.addEventListener('click', function(){
    duchyP3 = minusNum(duchyP3, startDuchyAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

duchPlusP3.addEventListener('click', function(){
    duchyP3 = plusNum(duchyP3, startDuchyAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

let provMinusP3 = document.querySelector("#provMinusP3");
let provPlusP3 = document.querySelector("#provPlusP3");
let startProvinceAmountP3 = document.querySelector("#provinceAmountP3");

provMinusP3.addEventListener('click', function(){
    provinceP3 = minusNum(provinceP3, startProvinceAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

provPlusP3.addEventListener('click', function(){
    provinceP3 = plusNum(provinceP3, startProvinceAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

let gardMinusP3 = document.querySelector("#gardMinusP3");
let gardPlusP3 = document.querySelector("#gardPlusP3");
let startGardensAmountP3 = document.querySelector("#gardensAmountP3");

gardMinusP3.addEventListener('click', function(){
    gardensP3 = minusNum(gardensP3, startGardensAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

gardPlusP3.addEventListener('click', function(){
    gardensP3 = plusNum(gardensP3, startGardensAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

let islaMinusP3 = document.querySelector("#islaMinusP3");
let islaPlusP3 = document.querySelector("#islaPlusP3");
let startIslandAmountP3 = document.querySelector("#islandAmountP3");

islaMinusP3.addEventListener('click', function(){
    islandP3 = minusNum(islandP3, startIslandAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

islaPlusP3.addEventListener('click', function(){
    islandP3 = plusNum(islandP3, startIslandAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

let cardMinusP3 = document.querySelector("#cardMinusP3");
let cardPlusP3 = document.querySelector("#cardPlusP3");
let startcardsAmountP3 = document.querySelector("#cardAmountP3");

cardMinusP3.addEventListener('click', function(){
    cardsP3 = minusNum(cardsP3, startcardsAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

cardPlusP3.addEventListener('click', function(){
    cardsP3 = plusNum(cardsP3, startcardsAmountP3);
    calcScore(scoreP3, estateP3, duchyP3, provinceP3, gardensP3, cardsP3, islandP3, p3Score);
})

/* 
    The break to player four functionality
*/

let cardsP4 = 10, scoreP4 = 0, estateP4 = 3, duchyP4 = 0, provinceP4 = 0, gardensP4 = 0, islandP4 = 0;
let p4Score = document.querySelector("#p4Score");

let estaMinusP4 = document.querySelector("#estaMinusP4");
let estaPlusP4 = document.querySelector("#estaPlusP4");
let startEstatesAmountP4 = document.querySelector("#estateAmountP4");

estaMinusP4.addEventListener('click', function(){
    estateP4 = minusNum(estateP4, startEstatesAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

estaPlusP4.addEventListener('click', function(){
    estateP4 = plusNum(estateP4, startEstatesAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

let duchMinusP4 = document.querySelector("#duchMinusP4");
let duchPlusP4 = document.querySelector("#duchPlusP4");
let startDuchyAmountP4 = document.querySelector("#duchyAmountP4");

duchMinusP4.addEventListener('click', function(){
    duchyP4 = minusNum(duchyP4, startDuchyAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

duchPlusP4.addEventListener('click', function(){
    duchyP4 = plusNum(duchyP4, startDuchyAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

let provMinusP4 = document.querySelector("#provMinusP4");
let provPlusP4 = document.querySelector("#provPlusP4");
let startProvinceAmountP4 = document.querySelector("#provinceAmountP4");

provMinusP4.addEventListener('click', function(){
    provinceP4 = minusNum(provinceP4, startProvinceAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

provPlusP4.addEventListener('click', function(){
    provinceP4 = plusNum(provinceP4, startProvinceAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

let gardMinusP4 = document.querySelector("#gardMinusP4");
let gardPlusP4 = document.querySelector("#gardPlusP4");
let startGardensAmountP4 = document.querySelector("#gardensAmountP4");

gardMinusP4.addEventListener('click', function(){
    gardensP4 = minusNum(gardensP4, startGardensAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

gardPlusP4.addEventListener('click', function(){
    gardensP4 = plusNum(gardensP4, startGardensAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

let islaMinusP4 = document.querySelector("#islaMinusP4");
let islaPlusP4 = document.querySelector("#islaPlusP4");
let startIslandAmountP4 = document.querySelector("#islandAmountP4");

islaMinusP4.addEventListener('click', function(){
    islandP4 = minusNum(islandP4, startIslandAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

islaPlusP4.addEventListener('click', function(){
    islandP4 = plusNum(islandP4, startIslandAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

let cardMinusP4 = document.querySelector("#cardMinusP4");
let cardPlusP4 = document.querySelector("#cardPlusP4");
let startcardsAmountP4 = document.querySelector("#cardAmountP4");

cardMinusP4.addEventListener('click', function(){
    cardsP4 = minusNum(cardsP4, startcardsAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

cardPlusP4.addEventListener('click', function(){
    cardsP4 = plusNum(cardsP4, startcardsAmountP4);
    calcScore(scoreP4, estateP4, duchyP4, provinceP4, gardensP4, cardsP4, islandP4, p4Score);
})

/* 
    The break to player five functionality
*/

let cardsP5 = 10, scoreP5 = 0, estateP5 = 3, duchyP5 = 0, provinceP5 = 0, gardensP5 = 0, islandP5 = 0;
let p5Score = document.querySelector("#p5Score");

let estaMinusP5 = document.querySelector("#estaMinusP5");
let estaPlusP5 = document.querySelector("#estaPlusP5");
let startEstatesAmountP5 = document.querySelector("#estateAmountP5");

estaMinusP5.addEventListener('click', function(){
    estateP5 = minusNum(estateP5, startEstatesAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

estaPlusP5.addEventListener('click', function(){
    estateP5 = plusNum(estateP5, startEstatesAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

let duchMinusP5 = document.querySelector("#duchMinusP5");
let duchPlusP5 = document.querySelector("#duchPlusP5");
let startDuchyAmountP5 = document.querySelector("#duchyAmountP5");

duchMinusP5.addEventListener('click', function(){
    duchyP5 = minusNum(duchyP5, startDuchyAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

duchPlusP5.addEventListener('click', function(){
    duchyP5 = plusNum(duchyP5, startDuchyAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

let provMinusP5 = document.querySelector("#provMinusP5");
let provPlusP5 = document.querySelector("#provPlusP5");
let startProvinceAmountP5 = document.querySelector("#provinceAmountP5");

provMinusP5.addEventListener('click', function(){
    provinceP5 = minusNum(provinceP5, startProvinceAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

provPlusP5.addEventListener('click', function(){
    provinceP5 = plusNum(provinceP5, startProvinceAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

let gardMinusP5 = document.querySelector("#gardMinusP5");
let gardPlusP5 = document.querySelector("#gardPlusP5");
let startGardensAmountP5 = document.querySelector("#gardensAmountP5");

gardMinusP5.addEventListener('click', function(){
    gardensP5 = minusNum(gardensP5, startGardensAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

gardPlusP5.addEventListener('click', function(){
    gardensP5 = plusNum(gardensP5, startGardensAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

let islaMinusP5 = document.querySelector("#islaMinusP5");
let islaPlusP5 = document.querySelector("#islaPlusP5");
let startIslandAmountP5 = document.querySelector("#islandAmountP5");

islaMinusP5.addEventListener('click', function(){
    islandP5 = minusNum(islandP5, startIslandAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

islaPlusP5.addEventListener('click', function(){
    islandP5 = plusNum(islandP5, startIslandAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

let cardMinusP5 = document.querySelector("#cardMinusP5");
let cardPlusP5 = document.querySelector("#cardPlusP5");
let startcardsAmountP5 = document.querySelector("#cardAmountP5");

cardMinusP5.addEventListener('click', function(){
    cardsP5 = minusNum(cardsP5, startcardsAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

cardPlusP5.addEventListener('click', function(){
    cardsP5 = plusNum(cardsP5, startcardsAmountP5);
    calcScore(scoreP5, estateP5, duchyP5, provinceP5, gardensP5, cardsP5, islandP5, p5Score);
})

/*
    The break to player six functionality
*/

let cardsP6 = 10, scoreP6 = 0, estateP6 = 3, duchyP6 = 0, provinceP6 = 0, gardensP6 = 0, islandP6 = 0;
let p6Score = document.querySelector("#p6Score");

let estaMinusP6 = document.querySelector("#estaMinusP6");
let estaPlusP6 = document.querySelector("#estaPlusP6");
let startEstatesAmountP6 = document.querySelector("#estateAmountP6");

estaMinusP6.addEventListener('click', function(){
    estateP6 = minusNum(estateP6, startEstatesAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

estaPlusP6.addEventListener('click', function(){
    estateP6 = plusNum(estateP6, startEstatesAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

let duchMinusP6 = document.querySelector("#duchMinusP6");
let duchPlusP6 = document.querySelector("#duchPlusP6");
let startDuchyAmountP6 = document.querySelector("#duchyAmountP6");

duchMinusP6.addEventListener('click', function(){
    duchyP6 = minusNum(duchyP6, startDuchyAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

duchPlusP6.addEventListener('click', function(){
    duchyP6 = plusNum(duchyP6, startDuchyAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

let provMinusP6 = document.querySelector("#provMinusP6");
let provPlusP6 = document.querySelector("#provPlusP6");
let startProvinceAmountP6 = document.querySelector("#provinceAmountP6");

provMinusP6.addEventListener('click', function(){
    provinceP6 = minusNum(provinceP6, startProvinceAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

provPlusP6.addEventListener('click', function(){
    provinceP6 = plusNum(provinceP6, startProvinceAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

let gardMinusP6 = document.querySelector("#gardMinusP6");
let gardPlusP6 = document.querySelector("#gardPlusP6");
let startGardensAmountP6 = document.querySelector("#gardensAmountP6");

gardMinusP6.addEventListener('click', function(){
    gardensP6 = minusNum(gardensP6, startGardensAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

gardPlusP6.addEventListener('click', function(){
    gardensP6 = plusNum(gardensP6, startGardensAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

let islaMinusP6 = document.querySelector("#islaMinusP6");
let islaPlusP6 = document.querySelector("#islaPlusP6");
let startIslandAmountP6 = document.querySelector("#islandAmountP6");

islaMinusP6.addEventListener('click', function(){
    islandP6 = minusNum(islandP6, startIslandAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

islaPlusP6.addEventListener('click', function(){
    islandP6 = plusNum(islandP6, startIslandAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

let cardMinusP6 = document.querySelector("#cardMinusP6");
let cardPlusP6 = document.querySelector("#cardPlusP6");
let startcardsAmountP6 = document.querySelector("#cardAmountP6");

cardMinusP6.addEventListener('click', function(){
    cardsP6 = minusNum(cardspP6, startcardsAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})

cardPlusP6.addEventListener('click', function(){
    cardsP6 = plusNum(cardsP6, startcardsAmountP6);
    calcScore(scoreP6, estateP6, duchyP6, provinceP6, gardensP6, cardsP6, islandP6, p6Score);
})
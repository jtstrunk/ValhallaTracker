// let airplane = document.querySelectorAll(".airplane");

// for(let i = 0; i < airplane.length; i++){
//     if(airplane[i].innerText == ''){
//         airplane[i].parentElement.remove();
//     }
// }

// let carrots = document.querySelectorAll(".carrot");

// for(let i = 0; i < carrots.length; i++){
//     carrots[i].addEventListener('click', () => {
//         carrotParent = carrots[i].parentElement;
//         mainParent = carrotParent.parentElement;
//         carrotChildren = mainParent.children;

//         if(!carrotChildren[1].classList.contains("DrawerHide")) {
//             if(carrotChildren[1].classList.contains("DrawerShow")) {
//                 carrotChildren[1].classList.remove('DrawerShow'); 
//             }
//             carrotChildren[1].classList.add("DrawerHide");
//             carrots[i].classList.add("flipped");
//         } else {
//             carrots[i].classList.remove("flipped");
//             carrotChildren[1].classList.add('DrawerShow'); 
//             carrotChildren[1].classList.remove('DrawerHide'); 
//         }
//     })
// }

// let wrappers = document.querySelectorAll(".gameWrapper");
// wrappers[0].classList.add("topWrapper");

// let selectGame = document.querySelector("#gameSelect");

// selectGame.addEventListener('change', () => {
//     let val = selectGame.value;
//     console.log(val);
//     let games = document.querySelectorAll(".gameWrapper");

//     if(val !== "allGames"){
//         for(let i = 0; i < games.length; i++){
//             console.log("removing")
//             console.log(val);
//             console.log(games[i].id)
//             if(val !== games[i].id) {
//                 games[i].classList.add("Hide");
//             } else {
//                 games[i].classList.remove("Hide");
//             }
//         }
//     } else {
//         console.log("whaha  ")
//         for(let i = 0; i < games.length; i++){
//             games[i].classList.remove("Hide");
//         }
//     }
// })
let userscore = 0;
let compscore = 0;

const choices = document.querySelectorAll(".choices");
const msg = document.querySelector("#msg")
const userscorepara = document.querySelector("#userscore")
const compscorepara = document.querySelector("#compscore")


const gencomputerchoice = ()=>{
    const options =["rock","paper","scissors"]
    const randindx = Math.floor(Math.random()*3)
    return options[randindx]
}

const drawgame = ()=>{
    console.log("DrawGame")
    msg.innerText= "Game Was Draw !"
    msg.style.backgroundColor = "#808080"
}

const showWinner = (userWin , userchoice , compchoice)=>{
    if(userWin){
        console.log("You Won !")
        userscore++
        userscorepara.innerText = userscore
        msg.innerText= `You Won ! ${userchoice} beats ${compchoice}`
        msg.style.backgroundColor = "#05ED98"
    }else {
        console.log("You Lose !")
        compscore++
        compscorepara.innerText = compscore
        msg.innerText= `You lose ! ${compchoice} beats ${userchoice}`
        msg.style.backgroundColor = "#FF0000"
    }
}

const playgame=(userchoice) => {
    console.log("A choice was clicked = " , userchoice)
    const compchoice = gencomputerchoice()
    console.log("Comp Chocie = ",compchoice)

    if(userchoice == compchoice){
        drawgame()

    }else{
        let userWin =true;
        if(userchoice === "rock"){
            userWin = compchoice === "paper"? false : true;

        }else if(userchoice === "paper") {
            userWin = compchoice === "scissors" ? false : true;
        }else {
            userWin = compchoice === "rock" ? false : true;
        }
        showWinner(userWin);
    }
}


choices.forEach((choice) => {
    choice .addEventListener("click",() =>{
        const userchoice = choice.getAttribute("id")
        
        playgame(userchoice)
    })
})



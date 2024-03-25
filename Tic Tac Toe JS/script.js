let boxes = document.querySelectorAll(".box");
let reset = document.querySelector(".reset_but")
let msgg = document.querySelector(".msgContainer")
let msg = document.querySelector("#msg")
let new_game = document.querySelector("#new-game")
let newGame = document.querySelector("#new-game")
let turnO = true;
let count = 0


const winpatterns = [   
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8],
];

const reset_game = () =>{
    enable_boxes()
    msgg.classList.add("hide");

}

boxes.forEach(box => {
    box.addEventListener("click",()=>{
        console.log("box was clicked")
        if (turnO){
            box.innerText = "O";
            turnO = false

        }else {
            box.innerText = "X";
            turnO = true
        }
        box.disabled = true;
        count ++
        let iswinner = checkwinner()
        
        if(count == 9 && !iswinner){
            gameDraw()
        }
    })
});


const gameDraw =() => {
    msg.innerText = `The Game is Draw`;
    msgg.classList.remove("hide");
    disbale_boxes();
}

const disbale_boxes = () =>{
    for (let box of boxes){
        box.disabled = true;
    }
}


const enable_boxes = () =>{
    for (let box of boxes){
        box.disabled = false;
        box.innerText = ""
    }
}

const showwinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgg.classList.remove("hide");
    disbale_boxes();
};

const checkwinner = () => {
    for (let pattern of winpatterns) {
        let pos1Val = boxes[pattern[0]].innerText;
        let pos2Val = boxes[pattern[1]].innerText;
        let pos3Val = boxes[pattern[2]].innerText;

        if (pos1Val != "" && pos2Val != "" && pos3Val != ""){
            if(pos1Val===pos2Val && pos2Val===pos3Val){
                console.log("Winner" , pos1Val)
                showwinner(pos1Val);
                return true
            }
        }

    }
}

newGame.addEventListener("click", reset_game)
reset.addEventListener("click", reset_game)
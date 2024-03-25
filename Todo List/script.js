submit.addEventListener("click", (e)=>{
    e.preventDefault()
    titlec=title.value
    descc=desc.value
    localStorage.setItem(JSON.stringify([titlec]),JSON.stringify([descc]))
    
    console.log(e)
    todo.innerHTML = `
    <h2>${titlec}</h2>
    <p>${descc}</p>
    `
    title.value=""
    desc.value=""

})


deletebtn.addEventListener("click", (e)=>{
    e.preventDefault()
    localStorage.removeItem("todo")
    todo.innerHTML=""

})

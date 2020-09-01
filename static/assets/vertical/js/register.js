$(document).ready(function(){
    var account = document.getElementById("account")
    var accounterr = document.getElementById("accounterr")
    var checkerr = document.getElementById("checkerr")

    var pass = document.getElementById("pass")
    var passerr = document.getElementById("passerr")

    var passwd = document.getElementById("passwd")
    var passwderr = document.getElementById("passwderr")

    account.addEventListener("focus", function(){
        accounterr.style.display="none"
        checkerr.style.display="none"
    }, false)

    account.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 20) {
            accounterr.style.display="block"
            return
        }

        $.post("/checkuserid/", {"userid": instr}, function(data){
            if (data.status == "error") {
                checkerr.style.display="block"
            }
        })
    }, false)


    pass.addEventListener("focus", function(){
        passerr.style.display="none"
    }, false)

    pass.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 20) {
            passerr.style.display="block"
            return
        }
    }, false)

    passwd.addEventListener("focus", function(){
        passwderr.style.display="none"
    }, false)

    passwd.addEventListener("blur", function(){
        instr = this.value
        if (instr != pass.value) {
            passwderr.style.display="block"
            return
        }
    }, false)

})
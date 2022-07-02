
const value = JSON.parse(localStorage.getItem('user'))
console.log(value);
if(value.length > 0 && value != 'null' ) {
    if(value[0][3] == 'ROLE_ADMIN'){
        window.location.replace(`${location.origin}/ROLE_ADMIN`)
    }
    else if (value[0][3] == 'ROLE_COUNSELLOR'){
        window.location.replace(`${location.origin}/ROLE_COUNSELLOR`)
    }
    else{
        $('.b1').hide()
        $('.b2').hide()
    }
    
}
else{
    $('.b1').show()
    $('.b2').hide()

}

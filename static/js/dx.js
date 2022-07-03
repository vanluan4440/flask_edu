$('#dx').click(()=>{
    
    window.localStorage.clear()
    window.location.replace(`${window.origin}`)
})


const localvale = window.localStorage.getItem('user')
if(localvale == null){
    window.location.replace(`${window.origin}`)
}
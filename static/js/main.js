$(document).ready(()=>{
    const timeOut = setTimeout(()=>{
        $('#loader').addClass('loader-hide');
        clearTimeout(timeOut)
    },3000);
})
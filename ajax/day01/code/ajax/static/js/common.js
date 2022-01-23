function createXhr(){
    if (window.XMLHttpRequest){
        return new XMLHttpRequest();
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP');
    }
    //print xhr
    console.log(xhr);
}
a=0
t=0
s=0
function sleep(milliseconds) {  
    return new Promise(resolve => setTimeout(resolve, milliseconds));  
 } 
async function spin(){
    t=t+360
    for(i=1;i<=t;i++){
    a=a+1
    s=s+.001
    await sleep(s); 
    document.getElementById("base").style.rotate = a+"deg";
}
for(i=1;i<=t;i++){
    a=a+1
    s=s+.01
    await sleep(s); 
    document.getElementById("base").style.rotate = a+"deg";
}
for(i=1;i<=180;i++){
    a=a+1
    s=s+.1
    await sleep(s); 
    document.getElementById("base").style.rotate = a+"deg";
}
t=0
s=0
}

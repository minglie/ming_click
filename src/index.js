var fs = require('fs');
var c = require('child_process');

let C={};

C.watch=function (watch) {

    let t1=new Date().getTime();
    let t2=new Date().getTime();

	console.log("watch on "+watch)
    fs.watch(watch, (event, file) => {
        if (file) {
            if(event==="change"){
                t2=new Date().getTime();
                if(t2-t1>100){
                    t1=t2;
                    console.log("run ...."+file+new Date().getTime())
                    c.exec(`a "index - Google Chrome" 116`);
                }
            }
        }
    });
}

if(process.argv[2]){
    C.watch(process.argv[2])
}

module.exports=C;
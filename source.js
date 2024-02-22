


function main() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    var date = getDate()
    var amount = 0;
    var reason = "";

    rl.question(`What's gooood, me! How much did you make today? (Today's Date: ${date}) >>`, getAmount => {
        console.log(`You made ${getAmount}!`);
        amount = getAmount;
        rl.close();
    });

    console.log(amount);
}

function getDate() {
    var date = Date();
    var newDate = "";
    // console.log(date);

    // 16 cuz on 17th char, that's when the time starts coming in and
    // idc about that. i just want like "Thu Feb 22 2024"
    for (var i = 0; i < 16; i++) {
        //console.log("works right " + i)
        newDate += date[i];
    }

    // console.log(newDate);

    return newDate;
}


function logData(date, amount, where) {

}


main();

function main() {
    var date = getDate();
    // console.log(date);
    var income = prompt("\nWhat's goood, me! How much did you make today?")

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

main();
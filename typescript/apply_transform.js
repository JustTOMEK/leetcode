function map(arr, fn) {
    var return_array = [];
    for (var i = 0; i < arr.length; i++) {
        return_array.push(fn(arr[i], i));
    }
    return return_array;
}
;
